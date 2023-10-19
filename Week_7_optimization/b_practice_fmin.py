#!/usr/bin/env python3

from scipy.optimize import fmin
from functools import partial
import matplotlib.pyplot as plt
import numpy as np


# ------------------------ Optimization, practice ---------------
#
# This is practice setting up fmin with a 1D function that has several parameters "bound" to specific values - this
#  lets us re-use code and solve for a "family" of similar functions

# A generic quadratic function that we want to find the minimum of ax^2 + bx + c
def my_quad_func(x, a=0, b=1, c=0):
    """A quadratic function
    @param x the input x value
    @param a - scale x^2
    @param b - scale x
    @param c - add c
    @returns ax^2 + bx + c"""
    # TODO: calculate, and return, the function
    return 0


if __name__ == '__main__':
    # Use fmin to find the minimum of my_quad_func for several values of a, b, and c

    # Plot the function and the result
    fig, axs = plt.subplots(1, 1, figsize=(4, 4))
    ts = np.linspace(-3.0, 6.0)

    a_list = [0.5, 0.5, 1.0]
    b_list = [-1.0, 0.25, 0.2]
    c_list = [-2.0, 0.0, 2.0]
    cols = ['red', 'blue', 'grey']
    for a, b, c in zip(a_list, b_list, c_list):
        # TODO
        #  Use partial to create a function from my_quad_func that sets a to a, b to b, and c to c
        #  Pass that function into fmin to find the minima (x_at_min and f_at_x_min)

        x_at_min = 0
        f_at_x_min = 0
        # BEGIN SOLUTION
        my_fn = partial(my_quad_func, a=a, b=b, c=c)
        x_at_min, f_at_x_min, _, _, _ = fmin(my_fn, 0.2, maxfun=100, full_output=True)
        # END SOLUTION

        print(f"Minimum of f is {f_at_x_min}, happens at x={x_at_min[0]}")

        axs.plot(ts, my_fn(ts), linestyle='-', label=f"{a} x^2 + {b}x + c")
        axs.plot(x_at_min, f_at_x_min, 'Xr')

    axs.set_xlabel('x')
    axs.set_ylabel('y')
    axs.axis('equal')
    axs.set_title("Minimum of quadratic")


# Answer for my_quad_func
#     return a * x**2 + b * x + c
