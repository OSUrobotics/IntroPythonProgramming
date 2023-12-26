#!/usr/bin/env python3

# ---------------------- Numeric differentiation ------------------------
# Feel free to change the function

# A generic function that we want to find the derivative of
def my_func(x):
    """A quadratic function
    @param x the input x value
    @returns f(x)"""
    return (x-2)**2 - 3


# The analytical derivative for the function, since we can
def my_func_deriv(x):
    """A linear function
    @param x the input x value
    @returns f(x)"""
    return 2 * x - 4


if __name__ == '__main__':
    # Do derivatives at x = 0.2
    x = 0.2

    # TODO: Try different values of h - what is the largest value of h you can use where the approximate derivatives
    #   are close to the analytic solution?
    #  Which is more accurate? Forward, backward, or central?
    # BEGIN SOLUTION
    for h in [1.0, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005]:
        print(f"h {h}")
        # Forward difference
        deriv_forward = (my_func(x + h) - my_func(x)) / h
        # Backwards
        deriv_backwards = (my_func(x) - my_func(x-h)) / h
        # Central
        deriv_central = (my_func(x+h) - my_func(x-h)) / (2.0 * h)

        # Analytic
        deriv_actual = my_func_deriv(x)

        print(f"Forward { deriv_forward:0.6f}")
        print(f"Backwards { deriv_backwards:0.6f}")
        print(f"Central { deriv_central:0.6f}")
        print(f"Analytic { deriv_actual:0.6f}\n")
    # END SOLUTION

    # ---------------------answers ------------------
    # Central is more accurate, and it's always about right (why? remember this is a quadratic, so it's bowl shaped...)
    #  forward/backward don't converge until closer to h = 0.001
    for h in [1.0, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005]:
        print(f"h {h}")
        # Forward difference
        deriv_forward = (my_func(x + h) - my_func(x)) / h
        # Backwards
        deriv_backwards = (my_func(x) - my_func(x-h)) / h
        # Central
        deriv_central = (my_func(x+h) - my_func(x-h)) / (2.0 * h)

        # Analytic
        deriv_actual = my_func_deriv(x)

        print(f"Forward { deriv_forward:0.6f}")
        print(f"Backwards { deriv_backwards:0.6f}")
        print(f"Central { deriv_central:0.6f}")
        print(f"Analytic { deriv_actual:0.6f}\n")
