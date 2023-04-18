#!/usr/bin/env python3

# Make a "picture" by drawing multiple copies of an object using matrices to move/scale/rotate the object
#
# Requirements:
#  1) Must include at least one for loop OR
#  2) Multiple uses of rotations/translations
#  3) At least one compound transformation (eg, a scale and a translation)
#
# Given to you:
#  functions to make matrices of the three different types
#  Plotting code
#  Read/write "objects" code
#  A square and a wedge and a star object
#
# Optional:
#  You can use the function make_object_by_clicking in object_routines to make a novel object
#  make sure to include that object's file when you hand in


import numpy as np
import matplotlib.pyplot as plt
# Slightly different import format here - this gets just those routines by name (no mr.)
from matrix_routines import make_scale_matrix, make_translation_matrix, make_rotation_matrix
from object_routines import read_object, make_object_by_clicking, plot_object_in_world_coord_system


if __name__ == '__main__':
    # initial "scene"
    sq = read_object("Square")
    star = read_object("Star")

    fig, axs = plt.subplots(1, 1)

    plot_object_in_world_coord_system(axs, sq)
    # Option 1: Store the matrix in the object before calling plot
    cols = ["azure", "aqua", "cyan", "skyblue", "dodgerblue"]
    for col, dt in zip(cols, np.linspace(0, 2 * np.pi, 5)):
        star["Color"] = col
        star["Matrix"] = make_translation_matrix(np.cos(dt), np.sin(dt))
        plot_object_in_world_coord_system(axs, star)

    # Option 2: Use the global matrix to move the object around
    star["Color"] = "red"
    star["Matrix"] = np.identity(3)
    for ds in [0.25, 0.5, 1.0, 1.25]:
        plot_object_in_world_coord_system(axs, star, make_scale_matrix(ds, 1.0))

    print("done")
