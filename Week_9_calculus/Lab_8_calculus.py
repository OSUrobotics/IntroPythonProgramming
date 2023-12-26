#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from functools import partial


# -------------- Area under an elliptic paraboloid ----------------------
#
# Use the monte carlo technique in the tutorial to estimate the area under the 2D elliptic parabaloid
# Your code should work even if the center and scale values shift (provided the parabaloid is still above the z = 0
#  plane)
#
# TODO 1: Create a function with the center/scale parameters bound to the given values.
#
# You might find it useful to go back to **a_tutorial_fmin** to remember how to bind parameters to create a simple function to use using **partial**.
#
# Also get the plotting code from that file#
#
#  TODO 2: Creating the "box"
#   1) Use x0 +- 2.0 and y0 +- 2.0 as the bounds
#   2) You can assume the parabola is bowl-shaped and above the z = 0 plane
#   3) The box will be a 3D box; get the z dimension by taking the maximum value of the function in that x,y range
#
#  TODO 3: Generating samples (see tutorial)
#    1) Samples need to be in the box
#    2) You need to generate x, y, and z samples - 3D points in the box
#        - I suggest generating the points, drawing them, then do the next part
#
#  TODO 4: Are the samples above or below the surface?
#    1) Compare to f(x,y) - is the z sample above or below?
#
#  TODO: Calculate the area (area of box * percentage of points in the box)
#
# Slides https://docs.google.com/presentation/d/1sq3ERLBET1ourJZJzXMtJe6-cN8Tlt-GLEzSDOxrd0M/edit?usp=sharing


# A fancier quadratic-y type function (but in 2D)
def elliptic_paraboloid(x, y, x0=0, y0=0, sclx=1, scly=1):
    """ x,y -> f(x) in the shape of a 'bowl'
    @param x - x value in the plane
    @param y - y value in the plane
    @param x0 - amount to shift the bottom of the bowl by in x
    @param y0 - amount to shift the bottom of the bowl by in y
    @param sclx - scale the bowl's side in x
    @param scly - scale the bowl's side in y
    @returns - f(x,y) the bowl's height over the point x,y
    """
    return (x-x0)**2 / sclx**2 + (y-y0)**2 / scly**2


if __name__ == '__main__':
    sclx = 1.5
    scly = 0.75
    x0 = 1.0
    y0 = 2.0

    # TODO: Use partial to create a function with the parameters bound to the above values
# YOUR CODE HERE

    # Notice the subplot_kw argument - this lets matlab know we want to plot in 3D and how to set the camera
    fig, axs = plt.subplots(subplot_kw={"projection": "3d"})
    # Doing the meshgrid for you - notice the +- 2.0 from x0 and y0
    # These are NOT the random samples you want - this is a grid of samples to use for creating the surface
    # ... you can also use it to find the min/max values of the function
    xs_grid, ys_grid = np.meshgrid(np.linspace(x0 - 2.0, x0 + 2.0), np.linspace(y0 - 2.0, y0 + 2.0))
    ellipse_max = np.max(my_func(xs_grid, ys_grid))

    # Make it easy to change the number of samples
    n_samples = 1000
    # TODO: Generate samples in x, y, and z inside the "box" using np.random.uniform
# YOUR CODE HERE

    # TODO See which samples are above/below the bowl
    area_under = 0.0
# YOUR CODE HERE
    print(f"Box area is {area_box}, expected 142.2222")

    # Plot the surface
    axs.plot_surface(xs_grid, ys_grid, my_func(xs_grid, ys_grid))

    # TODO: Plot the samples in two colors
# YOUR CODE HERE

    axs.set_xlabel('x')
    axs.set_ylabel('y')
    axs.set_title("Ellipsoid")

    print(f"Area under surface {area_under}")
    print("Done")
