#!/usr/bin/env python3

from scipy.optimize import fmin
from functools import partial
import matplotlib.pyplot as plt
import numpy as np

# -------------------------- Optimization -------------------------------
#
#  There are many engineering problems that can be expressed as an optimization of parameters to minimize/maximize some
# function. Cute trick: You can turn any maximization problem into a minimization one by multiplying by -1...
#   For example, what angle should you put the wind turbine blades if the wind is blowing at 30 mph if you
# want to maximize energy output? This assumes you have some function/simulation you can run that will output the
# amount of energy produced given the angle and the wind speed. Then it's a "search" for the angle that maximizes the
# energy produced. The simplest form of search is gradient descent.
#
# In this tutorial we'll focus on the mechanics of setting up the search using a quadratic function (find x given f(x))
#  and a 2D parameter search (find x,y given f(x,y)). The f is just a generic function that you could solve for
#  analytically; but pretend it's some complicated bit of code that simulates some system.

# A generic function that we want to find the minimum of
def my_func(x):
    """A quadratic function
    @param x the input x value
    @returns f(x)"""
    return (x-2)**2 - 3


# A fancier quadratic-y type function (but in 2D)
def elliptic_paraboloid(x, y, x0=0, y0=0, a=1, b=1):
    """ x,y -> f(x) in the shape of a 'bowl'
    @param x - x value in the plane
    @param y - y value in the plane
    @param x0 - amount to shift the bottom of the bowl by in x
    @param y0 - amount to shift the bottom of the bowl by in y
    @param a - scale the bowl's side in x
    @param b - scale the bowl's side in y
    @returns - f(x,y) the bowl's height over the point x,y
    """
    return (x-x0)**2 / a**2 + (y-y0)**2 / b**2


if __name__ == '__main__':
    # Use fmin to find the minimum of my_func
    # The _ says ignore that returned value
    #   See https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin.html
    #   for what the remaining values are
    # Note that x_at_min is a list - in this case, a list of dimension 1
    #    The full_output=True prints out the optimization result to the console
    x_at_min, f_at_x_min, _, _, _ = fmin(my_func, 0.2, maxfun=100, full_output=True)
    # Notice the [0] to get the first element out of the x list
    print(f"Minimum of f is {f_at_x_min}, happens at x={x_at_min[0]}")
    print(f"Checking fmin result {f_at_x_min} against func eval {my_func(x_at_min[0])}")

    # Plot the function and the result
    fig, axs = plt.subplots(1, 1, figsize=(4, 4))
    ts = np.linspace(-1.0, 3.0)
    axs.plot(ts, my_func(ts), '-k', label='Quadratic')
    axs.plot(x_at_min, f_at_x_min, 'Xr')
    axs.set_xlabel('x')
    axs.set_ylabel('y')
    axs.axis('equal')
    axs.set_title("Minimum of quadratic")

    # Now going to do the 2 dimensional version of a parabaloid
    # Because the function definition has all these extra parameters that
    #  control the shape of the function (x0, etc), we have do what's called
    #  "binding" the variables to values, in this case x0 = 3, y0 = 2, a = 4, b=16
    # partial is a functools method to do this, which has the advantage over a lambda
    #  function of creating a python function that is more "efficient" because it
    #  "freezes" the constant parameters
    # partial takes the function elliptic_paraboloid and "binds" all of the named
    #   parameter arguments
    my_paraboloid = partial(elliptic_paraboloid, x0=3, y0=2, a=8, b=16)
    print(f"My parabaloid at 3,4: {my_paraboloid(3, 4)}, check {elliptic_paraboloid(3, 4, x0=3, y0=2, a=8, b=16)}")

    # Almost done - fmin takes a function that takes in one argument (a list of dimension d)
    #  and outputs one number. Our my_paraboloid function currently takes in x,y, not [x,y].
    # Lambda functions fix that: In this case, it says make a new (temporary, unnamed function)
    #  that takes in one parameter (array) and calls my_paraboloid with array[0] and array[1]
    # Notice this time we saved the returned tuple to result, rather than unpacking it
    result = fmin(lambda array: my_paraboloid(array[0], array[1]), [0, 0], maxfun=200, full_output=True)
    print(result)
    print(f"Function minimum is {result[1]}, found at x,y {result[0]}")

    # Notice the subplot_kw argument - this lets matlab know we want to plot in 3D and how to set the camera
    fig2, axs2 = plt.subplots(subplot_kw={"projection": "3d"})
    xs, ys = np.meshgrid(np.linspace(2.5, 4.0), np.linspace(0.0, 3.0))
    axs2.plot_surface(xs, ys, my_paraboloid(xs, ys))
    axs2.plot(result[0][0], result[0][1], result[1], 'Xr', markersize=20)
    axs2.set_xlabel('x')
    axs2.set_ylabel('y')
    axs2.set_title("Minimum of ellipsoid")

    # You shouldn't really do this, because lambda functions are suppose to be unnamed,
    #  but this will show you what the lambda did
    my_lambda_func_2D = lambda array: my_paraboloid(array[0], array[1])
    # Notice that my_func_2D takes a list of two numbers, my_parabaloid takes 2 numbers
    print(f"Call my_parabaloid with 3, 4: {my_lambda_func_2D([3, 4])} {my_paraboloid(3, 4)}")
