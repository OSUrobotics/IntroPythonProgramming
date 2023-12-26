#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt

# --------------------------- Matrix routines -------------------------
#
# This will be our first example of making a .py file that is imported into the jupyter notebook/other .py file
# This is so that the basic matrix functions - making matrices, checking them, plotting - can be in one place.
#
# The code is organized as
#   Making scaling, rotation, translation matrices
#   Extracting information (translation, rotation, axes) from a generic matrix
#  Plotting with matrices

# These first few functions are just convenience functions for making specific transformation matrices (translation,
#  rotation, scale). Also a way to refresh your memory with the mechanics of building a specific matrix... Normally,
#  you would never write these (numpy has versions of them - in particular, use scipy's rotation/quaternion class to handle
#  rotations in 3D)
#
# A reminder that all matrices are 3x3 (even though we are in 2d) so that we can do translations (the upper left is the 2x2 matrix)

# Lecture slides: https://docs.google.com/presentation/d/12p3VOVT5yL14-1z5T20hTscpVC0hsxjtvMLHmQLFITk/edit?usp=sharing

# -------------------- Creating specific types of matrices ---------------------
def make_scale_matrix(scale_x=1.0, scale_y=1.0):
    """Create a 3x3 scaling matrix
    @param scale_x - scale in x. Should NOT be 0.0
    @param scale_y - scale in y. Should NOT be 0.0
    @returns a 3x3 scaling matrix"""
    if np.isclose(scale_x, 0.0) or np.isclose(scale_y, 0.0):
        raise ValueError(f"Scale values should be non_zero {scale_x}, {scale_y}")

    # Set the diagonal elements to the scale values
    mat = np.identity(3)
    mat[0, 0] = scale_x
    mat[1, 1] = scale_y

    return mat


def make_translation_matrix(d_x=0.0, d_y=0.0):
    """Create a 3x3 translation matrix that moves by dx, dy
    @param d_x - translate in x
    @param d_y - translate in y
    @returns a 3x3 translation matrix"""

    # Set the last column to the amount to move
    mat = np.identity(3)
    mat[0, 2] = d_x
    mat[1, 2] = d_y

    return mat


def make_rotation_matrix(theta=0.0):
    """Create a 3x3 rotation matrix that rotates counter clockwise by theta
    Note that it is convention to rotate counter clockwise - there's no mathematical reason for it
    @param theta - rotate by theta (theta in radians)
    @returns a 3x3 rotation matrix"""

    # x rotated = cos(theta) * x - sin(theta) * y
    # y rotated = sin(theta) * x + cos(theta) * y
    mat = np.identity(3)
    mat[0, 0] = np.cos(theta)
    mat[0, 1] = -np.sin(theta)
    mat[1, 1] = np.cos(theta)
    mat[1, 0] = np.sin(theta)

    return mat


# ------------------------------- What kind of matrix is it? What does it do? -------------------------------------

def get_dx_dy_from_matrix(mat):
    """Where does the matrix translate 0,0 to?
    @param mat - the matrix
    @returns dx, dy - the transformed point 0,0"""

    # Don't forget to turn origin into a homogenous point...
    #   Multiply the origin by the matrix then return the x and y components
    # Reminder: @ is the matrix multiplication
    origin = np.zeros(shape=(3,))
    origin[2] = 1.0

    xy_one = mat @ origin
    return xy_one[0], xy_one[1]


# Doing this one in two pieces - first, get out how the axes (1,0) and (0,1) are transformed, then in the mext
#  method get theta out of how (1,0) is transformed
def get_axes_from_matrix(mat):
    """Where does the matrix rotate (1,0) (0,1) to?
    @param mat - the matrix
    @returns x_rotated_axis, y_rotated_axis - the transformed vectors"""

    # What do (1,0) and (0,1) get transformed to?
    #  1) Set x_axis to be a unit vector pointing down the x axis
    #  2) Set y_axis to be a unit vector pointing down the y axis
    #  Multiply by the matrix to get the new "x" and "y" axes
    x_axis = np.zeros(shape=(3,))
    y_axis = np.zeros(shape=(3,))

    x_axis[0] = 1.0
    y_axis[1] = 1.0

    x_axis_rotated = mat @ x_axis
    y_axis_rotated = mat @ y_axis
    return x_axis_rotated[0:2], y_axis_rotated[0:2]


def get_theta_from_matrix(mat):
    """ Get the actual rotation angle from how the x-axis transforms
    @param mat - the matrix
    @return theta, the rotation amount in radians"""

    # Step 1) Use get_axes_from_matrix to get the x_axis,
    # Step 2) use arctan2 to turn the rotated x axis vector into an angle
    #   Use the x axis because theta for the x axis is 0 (makes the math easier)
    # Reminder: arctan2 takes (y, x)
    x_axis_rotated, _ = get_axes_from_matrix(mat)
    theta = np.arctan2(x_axis_rotated[1], x_axis_rotated[0])
    return theta


# ------------------------------- Plot code -------------------------------------
def make_pts_representing_circle(n_pts=25):
    """Create a 3xn_pts matrix of the points on a circle
    @param n_pts - number of points to use
    @return a 3xn numpy matrix"""

    ts = np.linspace(0, np.pi * 2, n_pts)
    # Make a 3 x n_pts array of points for the circle
    #   These are the x,y points of a unit circle centered at the origin
    #   These are the points that we will draw, both in their original location and in their transformed location
    # Step 1: Make a 3 x n_pts numpy array - I like to use np.ones, because it sets the homogenous coordinate for me
    # Step 2: Set the x values of the array to be cos(t) for the ts given above (you don't need a for loop for this,
    #   see numpy array math
    # Step 3: Do the same for the y values, but set to sin(t)
    pts = np.ones(shape=(3, n_pts))
    pts[0, :] = np.cos(ts)
    pts[1, :] = np.sin(ts)
    return pts


def plot_axes_and_box(axs, mat):
    """Plot the original coordinate system (0,0 and x,y axes) and transformed coordinate system
    @param axs - figure axes
    @param mat - the matrix"""

    # Initial location - center of coordinate system
    axs.plot(0, 0, '+k')
    axs.plot([0, 1], [0, 0], '-r')
    axs.plot([0, 0], [0, 1], '-b')

    # Draw a box around the world to make sure the plots stay the same size
    axs.plot([-5, 5, 5, -5, -5], [-5, -5, 5, 5, -5], '-k')

    # Moved coordinate system - draw the moved coordinate system and axes
    dx, dy = get_dx_dy_from_matrix(mat)
    x_axis, y_axis = get_axes_from_matrix(mat)

    axs.plot(dx, dy, 'Xb', markersize=5)
    axs.plot([dx, dx + x_axis[0]], [dy, dy + x_axis[1]], '-r', linewidth=2)
    axs.plot([dx, dx + y_axis[0]], [dy, dy + y_axis[1]], '-b', linewidth=2)

    # This makes sure the x and y axes are scaled the same
    axs.axis('equal')


def plot_axes_and_circle(axs, mat):
    """Plot the original coordinate system (0,0 and x,y axes) and transformed coordinate system and transformed circle
    @param axs - figure axes
    @param mat - the matrix"""

    # The axes and the box around the world
    plot_axes_and_box(axs, mat)

    # Make a circle
    pts = make_pts_representing_circle(25)

    # Draw circle
    axs.plot(pts[0, :], pts[1, :], ':g')

    # Transform circle by mat and put new points in pts_moved
    pts_moved = mat @ pts
    axs.plot(pts_moved[0, :], pts_moved[1, :], ':g')


def plot_zigzag(axs, mat):
    """Plot a zigzag before and after the transform
    @param axs - figure axes
    @param mat - the matrix"""

    # The axes and the box around the world
    plot_axes_and_box(axs, mat)

    # zigzag geometry
    pts = np.ones((3, 5))
    for i in range(0, 5):
        if i // 2:
            pts[0, i] = -1
        if i % 2:
            pts[1, i] = -1

    # Draw zigzag
    axs.plot(pts[0, :], pts[1, :], linestyle='dashed', color='grey')

    # Draw moved zigzag
    pts_moved = mat @ pts
    axs.plot(pts_moved[0, :], pts_moved[1, :], linestyle='dashed', color='grey')
    return pts


if __name__ == '__main__':
    # Create a matrix that has one of each type and call the plot code
    fig, axs = plt.subplots(1, 2, figsize=(6, 3))

    mat_scl_rot_trans = make_translation_matrix(2, 1) @ \
                        make_rotation_matrix(np.pi / 6.0) @ \
                        make_scale_matrix(1.3, 2.0)   # pts go here

    axs[0].set_title("Scl rot trans with circle")
    plot_axes_and_circle(axs[0], mat_scl_rot_trans)

    axs[1].set_title("Scl rot trans with zig zag")
    plot_zigzag(axs[1], mat_scl_rot_trans)

    # Depending on if your mac, windows, linux, and if interactive is true, you may need to call this to get the plt
    # windows to show
    plt.show()
    print("Done")

