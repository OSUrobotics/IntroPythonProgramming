#!/usr/bin/env python3

import numpy as np

# --------------------
# Lecture goals
#  1) Understand the benefit of numpy (over lists) for operating over lists of numbers
#  2) Introduction to numpy-style array operations
#  3) Dictionaries for data encapsulation
#  4) Functions for functionality encapsulation

# Functions: Functions enable encapsulation of, well, functionality.
# They're also a useful mental tool for organizing and structuring your thoughts on how to solve a given problem
#  1) Clearly define a bit of code that takes in some inputs, does some computation, then outputs some data
#  2) Makes it easier to test that code with different inputs
#  3) Practicalities: Prevents one of the most common sources of errors - re-using variable names
#
# It's almost never wrong to encapsulate a bit of code in a function. It can slow down (a tiny bit) computation
#  time, but can greatly reduce debugging time, so it's usually worth it.
# Python's function syntax is beautifully designed to make it easy to set default values for parameters and pass
#  back as much data as you want. We'll see more of that later; for this assignment we'll use the power of dictionaries
#  to pass back "labeled" data.

# Function calc_stats_from_list, fill in: Calculate stats when the input variable is a list
def calc_stats_from_list(in_list):
    """ Calculate mu of positive numbers, mu of negatives numbers
    Separate the list into positive and negative numbers. Calculate the mu of each. Return those means, along with
     how many positive/negative numbers there were
    @param in_list : any list type
    @return - A dictionary with the desired stats"""

    # These are the stats we're calculating. This is more elegant/useful than creating four variables - it keeps all
    #  of the values in the same place and assigns a meaningful label (key) to them
    dict_ret_stats = {"Mean positive": 0, "Mean negative": 0, "Count positive": 0, "Count negative": 0}

    # TODO:
    #   Calculate the means and the counts and store them in the dictionary with the keys given above in dict_ret_stats
    #   You'll need a for loop to go over the list and an if statement to separate into positive and negative
# YOUR CODE HERE
    return dict_ret_stats


# Function 2 to fill in: Calculate stats when the input variable is a numpy array
#   NO if statements or for loops - do this all with numpy operations
#     You might find "count_nonzero" useful
def calc_stats_from_nparray(in_list):
    """ Calculate mu of positive numbers, mu of negatives numbers
    Separate the list into positive and negative numbers. Calculate the mu of each. Return those means, along with
     how many positive/negative numbers there were
    @param in_list : numpy array
    @return - A dictionary with the desired stats"""

    # These are the stats we're calculating. This is more elegant/useful than creating four variables - it keeps all
    #  of the values in the same place and assigns a meaningful label (key) to them
    dict_ret_stats = {"Mean positive": 0, "Mean negative": 0, "Count positive": 0, "Count negative": 0}

    # TODO
    #   Calculate the means and the counts and store them in the dictionary with the keys given above in dict_ret_stats.
    #   Do NOT use a for loop
# YOUR CODE HERE
    return dict_ret_stats


# Create the arrays and test them. Here's another advantage of functions - you can create test data for yourself to
#  make sure the code is working right. Encapsulating the code in a function means you don't 1) accidentally change
#  the code when switching from the test data to the real data, and 2) you can make more than one test and 3) run
#  them more than once/all the time to double check that you didn't "break" the code
test_list_one = [-0.75, -0.25, 1.0 / 3.0, 2.0 / 3.0, 3.0 / 3.0]
test_list_res = calc_stats_from_list(test_list_one)
if not np.isclose(test_list_res["Mean positive"], 2.0 / 3.0):
    print(f"Mean positive is not correct, should be {2.0/3.0}, got {test_list_res['Mean positive']}")

if not np.isclose(test_list_res["Mean negative"], -0.5):
    print(f"Mean negative is not correct, should be -0.5, got {test_list_res['Mean negative']}")

if test_list_res["Count positive"] is not 3:
    print(f"Count positive numbers, should be 3, got {test_list_res['Count positive']}")

if test_list_res["Count negative"] is not 2:
    print(f"Count positive numbers, should be 2, got {test_list_res['Count negative']}")

print("Done tests list")

# There is a "fancy" way to do this test with the second function without duplicating code, but it's confusing, so
#  ... we'll just duplicate it here
test_nparray_one = np.array(test_list_one)  # Convert the previous test list to a numpy array
test_list_res = calc_stats_from_nparray(test_nparray_one)
if not np.isclose(test_list_res["Mean positive"], 2.0 / 3.0):
    print(f"Mean positive is not correct, should be {2.0/3.0}, got {test_list_res['Mean positive']}")

if not np.isclose(test_list_res["Mean negative"], -0.5):
    print(f"Mean negative is not correct, should be -0.5, got {test_list_res['Mean negative']}")

if test_list_res["Count positive"] is not 3:
    print(f"Count positive numbers, should be 3, got {test_list_res['Count positive']}")

if test_list_res["Count negative"] is not 2:
    print(f"Count positive numbers, should be 2, got {test_list_res['Count negative']}")

print("Done tests numpy array")

# Ok, now do it for real. This bit of code will generate a list or numpy array with random positive and negative
#   values.
def create_data(n_data=10, b_ret_numpy=True):
    """ Create a random mix of positive and negative numbers
    @param n_data - how big to make the list/array
    @param b_ret_numpy - return a list or a numpy array
    @return the list or numpy array"""
    my_data = np.random.random_sample(n_data)

    n_to_convert = np.random.randint(low=1, high=n_data-1)
    n_convert = np.random.randint(low=0, high=n_data-1, size=n_to_convert)
    my_data[n_convert] *= -1.0

    if b_ret_numpy is False:
        return list(my_data)
    return my_data


# This bit of code makes sure that the tests will only be run when you run this python file
if __name__ == '__main__':
    # Check by comparing results against each other (doesn't guarantee it's right, but...)
    #  Try 10 times. We don't care what the iteration is so use _ to say "we don't need a variable"
    for _ in range(0, 10):
        # Get some random data
        test_data = create_data()
        test_data_list = list(test_data)

        # Call the two functions - notice cast to a list type
        res_list = calc_stats_from_list(test_data_list)
        res_np = calc_stats_from_nparray(test_data)

        # For all four stored values...
        for k, v in res_list.items():
            # Use isclose instead of == because two of these are floating point values - and == never works with
            #  floating point values
            # Since we used the same keys (names) in the two different dictionaries, we can pass that key to the other
            #   dictionary
            if not np.isclose(res_np[k], v):
                print(f"Returned different values {k}, {v} and {res_np[k]}")

        print("Done test")
