#!/usr/bin/env python3
# W26

import numpy as np
from matplotlib import pyplot as plt

# --------------------------- Matrix routines -------------------------
#
# This will be our first example of making a .py file that is imported into the jupyter notebook/other .py file
# This is so that the basic matrix functions - making matrices, checking them, plotting - can be in one place,
# the re-used in multiple places using "import". 
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
    # Throw an error if a zero scale
    if np.isclose(scale_x, 0.0) or np.isclose(scale_y, 0.0):
        raise ValueError(f"Scale values should be non_zero {scale_x}, {scale_y}")

    # Set the diagonal elements to the scale values
    mat = np.identity(3)   # Always use identity to make the initial 3x3 matrix
    mat[0, 0] = scale_x
    mat[1, 1] = scale_y

    return mat


def make_translation_matrix(d_x=0.0, d_y=0.0):
    """Create a 3x3 translation matrix that moves by dx, dy
    @param d_x - translate in x
    @param d_y - translate in y
    @returns a 3x3 translation matrix"""

    # Set the last column to be the amount to move
    mat = np.identity(3)
    mat[0, 2] = d_x
    mat[1, 2] = d_y

    return mat


def make_rotation_matrix(theta=0.0):
    """Create a 3x3 rotation matrix that rotates counter clockwise by theta
    Note that it is convention to rotate counter clockwise - there's no mathematical reason for it
    @param theta - rotate by theta (theta in radians)
    @returns a 3x3 rotation matrix"""

    # If you multiply [x y 1]^t by the matrix, this is what you get
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
    """Where does the matrix translate 0, 0 to?
    @param mat - the matrix
    @returns dx, dy - the transformed point 0,0"""

    # Create a point for the origin (0,0) ... don't forget that the 3rd component should be 1
    #   Multiply the origin by the matrix then return the x and y components
    # Reminder: @ is the matrix multiplication
    origin = np.zeros(shape=(3,))
    origin[2] = 1.0

    xy_ret = mat @ origin
    #  Ditch the 1 at the end and return a tuple (x,y)
    return xy_ret[0], xy_ret[1]


# Doing this one in two pieces - first, get out how the axes (1,0) and (0,1) are transformed, then in the next
#  method get theta out of how (1,0) is transformed
def get_axes_from_matrix(mat):
    """Where does the matrix rotate (1,0) (0,1) to?
    @param mat - the matrix
    @returns x_rotated_axis, y_rotated_axis - the transformed vectors"""

    # What do (1,0) and (0,1) get transformed to?
    #  1) Set x_axis to be a unit vector pointing down the x axis
    #  2) Set y_axis to be a unit vector pointing down the y axis
    #  Multiply by the matrix to get the new "x" and "y" axes
    #    Reminder: zeros in the third row, not ones, because vectors can't translate
    x_axis = np.zeros(shape=(3,))
    y_axis = np.zeros(shape=(3,))

    x_axis[0] = 1.0   # 1, 0, 0
    y_axis[1] = 1.0   # 0, 1, 0

    x_axis_rotated = mat @ x_axis
    y_axis_rotated = mat @ y_axis
    # Get out the first two values. This is a tuple with a 2 dimensional array for each vector
    return x_axis_rotated[0:2], y_axis_rotated[0:2]


def get_theta_from_matrix(mat):
    """ Get the actual rotation angle from how the x-axis transforms
    @param mat - the matrix
    @return theta, the rotation amount in radians"""

    # Step 1) Use get_axes_from_matrix to get the x_axis,
    # Step 2) use arctan2 to turn the rotated x axis vector into an angle
    #   Use the x axis because theta for the x axis is 0 (makes the math easier)
    # Reminder: arctan2 takes (y, x)
    x_axis_rotated, _ = get_axes_from_matrix(mat)  # The _ says ignore the second returned vector

    # arctan2 takes y, x and returns the angle in the range -pi to pi
    theta = np.arctan2(x_axis_rotated[1], x_axis_rotated[0])
    return theta


# ------------------------------- Plot code -------------------------------------
# Note - these are the same as the ones in tutorial/practice
def plot_pts(axs, pts, fmt='-k'):
    """ plot the points in the window
    @param axs - the window to draw into
    @param pts - the 3xn array of points
    @param fmt - optional format parameter"""

    # This gets the x values (in row 0) and the y values and just does a regular plot
    #    
    axs.plot(pts[0, :], pts[1, :], fmt)

    # We have to do this get the line to go from the last point to the first
    #   (Not necessary if you duplicate the first point as the last point in pts)
    pts_close = np.zeros((2, 2))
    pts_close[:, 0] = pts[0:2, 0]
    pts_close[:, 1] = pts[0:2, -1]
    # and close the polygon
    axs.plot(pts_close[0, :], pts_close[1, :], fmt)


def plot_transformed_axes(axs, mat):
    """Plot where the coordinate system (0,0 and x,y axes) goes to when transformed by mat
    @param axs - figure axes
    @param mat - the matrix"""

    # Moved coordinate system - draw the moved coordinate system and axes
    #  The x axis as a vector - notice that the 3rd coordinate is a zero because vectors can't translate
    x_axis = np.array([1, 0, 0]).transpose()
    x_axis_moved = mat @ x_axis

    y_axis = np.array([0, 1, 0]).transpose()
    y_axis_moved = mat @ y_axis

    # The origin, however, is a point and it has a 1 in that third column
    origin = np.array([0, 0, 1]).transpose()

    origin_moved = mat @ origin

    # Put a blue X at the placd the origin moved to
    axs.plot(origin_moved[0], origin_moved[1], 'Xb', markersize=5)
    # Draw an arrow from there to the end of the moved x axis
    axs.arrow(x=origin_moved[0], y=origin_moved[1], dx=x_axis_moved[0], dy=x_axis_moved[1], color='red', linestyle="--")
    # Draw a blue arrow for the y axis
    axs.arrow(x=origin_moved[0], y=origin_moved[1], dx=y_axis_moved[0], dy=y_axis_moved[1], color='blue', linestyle="--")


def plot_axes_and_big_box(axs, box_size=5):
    """Plot the origin and x,y axes with a box at -5, -5 to 5, 5
    @param axs - figure axes"""

    # Put a black + at the origin
    axs.plot(0, 0, '+k')

    arrow_length = 1.0
    if box_size < 1.0:
        arrow_length = box_size * 0.9
    # Draw one red arrow for the x axis (x,y, dx, dy)
    axs.arrow(x=0, y=0, dx=arrow_length, dy=0, color='red')
    # Draw a blue arrow for the y axis
    axs.arrow(x=0, y=0, dx=0, dy=arrow_length, color='blue')

    # Draw a box around the world to make sure the plots stay the same size
    axs.plot([-box_size, box_size, box_size, -box_size, -box_size], [-box_size, -box_size, box_size, box_size, -box_size], '-k')

    # This makes sure the x and y axes are scaled the same
    axs.axis('equal')



""" Everything after __name__ is NOT imported when you import matrix_routines.py. However, if you run
     this file - by using the triangle in the upper right - this code will get executed. It's usually used
     to hold test code"""
if __name__ == '__main__':
    # Create a matrix that has one of each type and call the plot code
    fig, axs = plt.subplots(1, 1, figsize=(6, 3))

    mat_scl_rot_trans = make_translation_matrix(2, 1) @ \
                        make_rotation_matrix(np.pi / 6.0) @ \
                        make_scale_matrix(1.3, 2.0)   # pts go here

    n_points = 3
    pts_triangle = np.ones((3, n_points))
    # Make a right-sided triangle with the center of the origin in the middle
    pts_triangle[0:2, 0] = [-2.0, 1.25]  # Upper left corner
    pts_triangle[0:2, 1] = [2.0, -0.5]   # Pointy bit at the right
    pts_triangle[0:2, 2] = [-2.0, -0.5]   # 90 degree angle part

    axs.set_title("Scl rot trans with triangle")
    plot_axes_and_big_box(axs)
    plot_pts(axs, pts_triangle)
    plot_pts(axs, mat_scl_rot_trans @ pts_triangle, fmt=":g")
    plot_transformed_axes(axs, mat_scl_rot_trans)

    # Depending on if your mac, windows, linux, and if interactive is true, you may need to call this to get the plt
    # windows to show

    plt.show()

    # If it exits on you then put a break point at the line below and run in the debugger
    print("Done")

