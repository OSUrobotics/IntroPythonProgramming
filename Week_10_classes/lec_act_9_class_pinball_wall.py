#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
# YOUR CODE HERE

# You can import classes just like you do functions
from pinball_wall import PinballWall

# ---------------------------- Class Example (walls) ---------------------------------
#
# See pinball_wall.py
#
# Slides:


# A plot function to check that the walls all look ok
def plot_check():
    nrows = 1
    ncols = 1
    fig, axs = plt.subplots(nrows, ncols, figsize=(4, 4))

    # The values we calculated in calculate_n_time_steps
    left = -4.0
    right = 4.0
    height = 10.0

    axs.plot([left, right], [height, height], color='grey', linestyle="dotted")
    axs.plot([left, right], [0, 0], color='grey', linestyle="dotted")
    axs.plot([left, left], [0, height], color='grey', linestyle="dotted")
    axs.plot([right, right], [0, height], color='grey', linestyle="dotted")

    walls = []
    walls.append(PinballWall("Vertical", -3.0))
    walls.append(PinballWall("Vertical", 3.0))
    walls.append(PinballWall("Horizontal", 8.0))
    walls.append(PinballWall("General", a_b_c=[0.5, 0.5, 1.0]))
    walls.append(PinballWall("General", a_b_c=[-0.5, 0.5, 1.0]))
    for w in walls:
        w.plot(axs, left, right, height)

    axs.axis('equal')
    axs.set_title(f"Pinball walls")


if __name__ == '__main__':

    plot_check()

    print("Done")
