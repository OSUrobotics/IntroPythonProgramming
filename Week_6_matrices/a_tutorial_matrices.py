#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt

# All of the matrix routines are in here - we can import the Python (.py) file just like the imports above
#  All of the functions in there will be accessed as mr.
import matrix_routines as mr

# --------------------------- Matrices -------------------------
#
# Matrices are, fundamentally, about moving rigid objects around in space. This tutorial builds a couple matrices
# (in 2D), then uses them to plot a circle in different positions.
#
# The major tricky part of this is that the object - the circle - is ALSO represented as a matrix (a 3xn matrix,
#  n being the number of points used to represent the circle).
#
# Some other tricky parts with matrices
#  1) Order matters. Doing m1 then m2 is NOT the same as m2 then m1. We will use the convention that
#     pts_new = m1 @ m2 @ m3 pts_orig
#   means multiply pts_orig by m3, then m2, then m1. Yes, that feels backwards. But that is the convention (left multiply)
#   in most software that uses matrices
#  2) You'll notice I used @ and not *. numpy decided to use @ instead of * for matrix multiply (* means item
#     by item multiplication a) will only work if the two matrics are the same size and b) probably isn't what you want).
#
# This example puts all of the code into functions, rather than just writing it in-line.
# The code is organized as
#   Making scaling, rotation, translation matrices (in matrix_routines.py)
#   Multiplying matrices together (in example_*)
#  Using matrices to place objects in the world

# A reminder that all matrices are 3x3 (even though we are in 2d) so that we can do translations (the upper left is the 2x2 matrix)

# First, look at matrix_routines.py. Look for code that:
#   Creates matrices
#   Creates a circle as a list of points
#   Multiplies points by a matrix and plots the before and after
#     Where are the points made/created?
#     Where does the multiplicaiton happen?
#
# There is an example here that shows swapping the order of the matrices. Try drawing what the rotations/translations
#  would look like on a piece of paper and try to match up the transformations with the code.


# --------------------------------- What happens if you swap the order of two matrices? -----------------------
def example_order_matters():
    """ Make the plot for rotation-translation versus translation-rotation"""
    # Make the plot that shows the difference between rotate-translate and translate-rotate
    fig, axs = plt.subplots(2, 2, figsize=(8, 8))

    # Rotate the object then translate it - notice that the rotation goes on the right
    mat_rot_trans = mr.make_translation_matrix(1, 2) @ mr.make_rotation_matrix(np.pi / 4.0)   # pts go here

    axs[0, 0].set_title("Rot trans")
    mr.plot_axes_and_circle(axs[0, 0], mat_rot_trans)

    # Reverse the order of operations
    # Now create the matrix in the reverse order - try to predict what this will look like
    #   Set mat to be a translation, rotation matrix (same params as above)
    axs[0, 1].set_title("Trans rot")

    # Translate first, then rotate
    mat_trans_rot = mr.make_rotation_matrix(np.pi / 4.0) @ mr.make_translation_matrix(1, 2)   # pts go here
    mr.plot_axes_and_circle(axs[0, 1], mat_trans_rot)

    # Now do a matrix that is a scale 0.5,2.0, rotate pi/4, translate (1,2)
    mat_scl_rot_trans = mr.make_translation_matrix(1, 2) @ \
                        mr.make_rotation_matrix(np.pi / 4.0) @ \
                        mr.make_scale_matrix(0.5, 2.0)   # pts go here

    axs[1, 0].set_title("Scl rot trans")
    mr.plot_axes_and_circle(axs[1, 0], mat_scl_rot_trans)

    # Reverse the order of operations
    # Now do a matrix (mat) that is the REVERSE of the scale, rotate, translate
    mat_trans_rot_scl = mr.make_scale_matrix(0.5, 2.0) @ \
                        mr.make_rotation_matrix(np.pi / 4.0) @ \
                        mr.make_translation_matrix(1, 2)   # pts go here

    axs[1, 1].set_title("Trans rot scl")

    mr.plot_axes_and_circle(axs[1, 1], mat_trans_rot_scl)


if __name__ == '__main__':
    # Order of matrices matters
    example_order_matters()

    # Depending on if your mac, windows, linux, and if interactive is true, you may need to call this to get the plt
    # windows to show
    plt.show()
    print("Done")

