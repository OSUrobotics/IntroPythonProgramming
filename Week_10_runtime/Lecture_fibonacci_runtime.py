#!/usr/bin/env python3

""" This script illustrates the following concepts:
      Caching - how to save calculations in a variable to speed up computation
      Timing comparisons - how to use time() to figure out how long
          a computation took
      Try-except to catch parameter errors and to determine if
          the caching variables exist
      Associating attributes (variables) with functions
         - using default function attributes, like __name__
    Four versions: Caching y/n and instrumented for timing y/n

    Note: If you were to do this "cleanly" you would put all this in a
          class.
      """


def fib_basic(n):
    """
    Simple Fibonacci function, defined recursively.
    :param n: A non-negative integer.
    :return: The Fibonacci number for n.
    """

    # Check to make sure the argument is valid.
    if n < 0:
        raise ValueError('Argument must be non-negative')

    # If n is 0 or 1, just return the Fibonacci number.  Otherwise return the sum of the previous two
    # Fibonacci numbers.
    if n < 2:
        return n
    else:
        return fib_basic(n - 1) + fib_basic(n - 2)


def fib_cached(n):
    """
    Adding caching to fib_basic
    :param n: The Fibonacci number to calculate.
    :return: The Fibonacci number
    """

    # Make sure the inputs are valid
    if n < 0:
        raise ValueError('Argument must be non-negative')

    # Try to return the value from the cache.
    try:
        #   Yes, you can do this - remember, functions are just dictionaries (stored
        #    in a dictionary of functions).
        #   So you can add an entry (variable) to that dictionary
        #   Note - we have to actually *declare* the cacge variable below, or it won't
        #    exist when we try to access it.
        return fib_cached.cache[n]
    except KeyError:
        # Calculate the new value
        retval = fib_cached(n - 1) + fib_cached(n - 2)

        # Add it to the cache
        fib_cached.cache[n] = retval

        # Return the value.
        return retval


# This attribute, associated with the function above,
# is a cache. Initialize the cache with the base case values.
# Note that in the JN version I moved this into the function with a try-except, which is cleaner
fib_cached.cache = {0: 0, 1: 1}


def fib_instrumented(n):
    """
    Simple Fibonacci function, defined recursively, instrumented to count calls.
    :param n: A non-negative integer.
    :return: The Fibonacci number for n.
    """

    # Increment the call count
    #   Yes, you can do this - remember, functions are just dictionaries (stored
    #    in a dictionary of functions).
    #   So you can add an entry (variable) to that dictionary
    #   Note - we have to actually *declare* this variable below, or it won't
    #    exist when we try to add 1 to it.
    fib_instrumented.call_count += 1

    # Check to make sure the argument is valid.
    if n < 0:
        raise ValueError('Argument must be non-negative')

    # If n is 0 or 1, just return the Fibonacci number.  Otherwise return the sum of the previous two
    # Fibonacci numbers.
    if n < 2:
        return n
    else:
        return fib_instrumented(n - 1) + fib_instrumented(n - 2)


# This attribute, associated with the function above, will let us keep track of the number of calls.
# Note that in the JN version I moved this into the function with a try-except, which is cleaner
fib_instrumented.call_count = 0


def fib_cached_instrumented(n):
    """
    This Fibonacci function uses caching to speed things up.
    It's also instrumented, to show how many function calls are taken
    :param n:
    :return:
    """
    # Increment the call count - see fib_instrumented for explanation
    fib_cached_instrumented.call_count += 1

    # Check to make sure the argument is valid.
    if n < 0:
        raise ValueError('Argument must be non-negative')

    # Try to return a number from the cache.  If that fails, then we have to calculate it (recursively) from scratch,
    # add it to the cache, and then return it.
    try:
        return fib_cached_instrumented.cache[n]  # Again, this is a variable defined on the function
    except KeyError:
        # Calculate the value recursively
        retval = fib_cached_instrumented(n - 1) + fib_cached_instrumented(n - 2)

        # Store it in the cache
        fib_cached_instrumented.cache[n] = retval

        # And, finally, return it
        return retval


# Initialize the cache with the two base cases and the counter with 0.
# Note that in the JN version I moved this into the function with a try-except, which is cleaner
fib_cached_instrumented.call_count = 0
fib_cached_instrumented.cache = {0: 0, 1: 1}


def time_fib(f, n):
    """
    A wrapper function to time the execution of a Fibonacci function.
    :param f: The function to time.
    :param n: The Fibonacci number to evaluate.
    :return: The Fibonacci number.
    """
    # You can put the import here - it will only happen if time_fib is called
    from time import time

    # Reset the call count
    #   For the functions that *don't* have instrumentation, this will
    #    create that variable
    f.call_count = 0

    # Time a call to the Fibonacci function
    start_time = time()
    f(n)
    stop_time = time()

    # Return the time and the call count.
    return stop_time - start_time, f.call_count


if __name__ == '__main__':
    # You can put the imports here
    import matplotlib.pyplot as plt

    # Do some tests to make sure fibonacci functions are working as expected
    #   This is a hard-coded set of correct answers to test against
    fib_tests = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13}
    #   This is an array of the functions we're going to test
    #     Notice we're not calling the functions (no ()) - we're just putting the
    #     function variables in the list
    functions = [fib_basic, fib_cached, fib_instrumented, fib_cached_instrumented]

    # Test each of the functions on all of the test cases.
    for func in functions:  # Yes, this works - func is one of the fib_* functions
        print('{0}():'.format(func.__name__))  # .__name__ is defined on every function

        # Since fib_tests is a dictionary, and we want both the key and
        #  the value, we use the .items() iteration method
        for number, value in fib_tests.items():
            # Call the function and compare it to the test value
            if func(number) != value:
                print('  failed for {0}: expected {1}, got {2}'.format(number, value, func(number)))

        # Make sure we catch the invalid cases.
        try:
            func(-1)
            print('  failed for negative value')
        except ValueError:
            # This is the error the functions should throw if given a -1 - so it
            #   passed the test, don't do anything
            pass

        print('  tests complete')

    # Do some timing tests to see how long things take.  We're going to look at wall clock time and also
    # at the number of calls we make to the fib() function.  To do that, we're going to make a new version
    # of the function that's instrumented to count the number of calls, which we will call fib2().
    N = 15   # test on 1 to 15
    times, counts = zip(*(time_fib(fib_instrumented, n) for n in range(N)))
    cached_times, cached_counts = zip(*(time_fib(fib_cached_instrumented, n) for n in range(N)))

    # Let's plot the times and the call counts
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    ax1.set_title('Fibonacci performance')

    # Plot the times
    time_plot, = ax1.plot(times)
    cached_time_plot, = ax1.plot(cached_times)
    ax1.set_ylabel('time (seconds)')
    ax1.legend([time_plot, cached_time_plot], ['Basic', 'Cached'])

    # Plot the call counts
    call_plot, = ax2.plot(counts)
    cached_call_plot, = ax2.plot(cached_counts)
    ax2.set_xlabel('n')
    ax2.set_ylabel('function calls')
    ax2.legend([call_plot, cached_call_plot], ['Basic', 'Cached'])

    # Display the graphs.
    plt.show()
