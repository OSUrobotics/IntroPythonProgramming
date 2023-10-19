#!/usr/bin/env python3

from scipy.optimize import fmin
import matplotlib.pyplot as plt
import numpy as np


# ------------------------ Optimization, problems ---------------
#
# This is practice dealing with what can go "wrong" with fmin - local minima, multiple answers, setting the stopping
#  criteria
#
# Slides: https://docs.google.com/presentation/d/1xKhWyquiP-_wM9AnJJ57BBtF0eitEqSdODq34ttMZgk/edit?usp=sharing

# This function has several local minima - how to find the best one?
def my_multiple_minima_func(x):
    """A function with multiple minima
    @param x the input x value
    @returns ax^2 + bx + c"""
    return (3.0 * x - 4.0) * (0.5 * x + 0.2) * (x - 3.0) * (x - 3.0) + 2.0 * x + 0.5


if __name__ == '__main__':
    # Use fmin to find the minimum of my_multiple_minima_func
    #---------------- Local minima example ------------------

    # Plot the function and the result
    fig, axs = plt.subplots(1, 1, figsize=(4, 4))
    ts = np.linspace(-2.0, 5.0)
    axs.plot(ts, my_multiple_minima_func(ts), linestyle='-', label="Local minima")

    x_at_min, f_at_x_min, _, _, _ = fmin(my_multiple_minima_func, 4.0, full_output=True)
    axs.plot(x_at_min, f_at_x_min, 'Xr')
    print(f"Minimum of f is {f_at_x_min}, happens at x={x_at_min[0]}")

    x_at_real_min = 0.0
    f_at_real_min = 0.0
# YOUR CODE HERE
    axs.plot(x_at_real_min, f_at_real_min, 'Xg')

    axs.set_xlabel('x')
    axs.set_ylabel('y')

    axs.set_title("Minimum of quartic: Local minima")

    #---------------- Search parameters example ------------------
    fig2, axs2 = plt.subplots(1, 1, figsize=(4, 4))
    ts = np.linspace(2.6, 2.9)
    axs2.plot(ts, my_multiple_minima_func(ts), linestyle='-', label="Zoom in on curve")

    x_at_min, f_at_x_min, _, _, _ = fmin(my_multiple_minima_func, 4.0, full_output=True)
    axs2.plot(x_at_min, f_at_x_min, 'Xr', label="Accurate minima")
    print(f"Minimum of f is {f_at_x_min}, happens at x={x_at_min[0]}")

    # TODO: Change xtol and ftol until the number of iterations is under 10
    # (Also play around with the values to see how LONG you can make it run...
    x_not_as_accurate_min, f_not_as_accurate_min, iters, _, _ = fmin(my_multiple_minima_func, 4.0, xtol=0.0001, ftol=0.0001, full_output=True)
# YOUR CODE HERE
    print(f"Not accurate minimum of f is {f_not_as_accurate_min}, happens at x={x_not_as_accurate_min[0]}")

    axs2.plot(x_not_as_accurate_min, f_not_as_accurate_min, 'Xg', label="Not Accurate minima")

    axs2.set_xlabel('x')
    axs2.set_ylabel('y')
    axs2.legend()

    axs2.set_title("Minimum of quartic: Zoom in on Local minima")
