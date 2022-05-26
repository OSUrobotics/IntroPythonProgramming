#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# ------------- Making a figure using plot, use case 1 -----------------------------
# Here's the data from the tutorial
#
t_values = np.linspace(-np.pi, np.pi, num=200)
y1_values = np.sin(t_values)
y2_values = np.cos(t_values)

# Here's the two original plot commands
plt.plot(t_values, y1_values, '-b', label='sin', marker='x')
plt.plot(t_values, y2_values, '--r', label='cos', linewidth=2)

# Here's the add labeling stuff
plt.xlabel("t value")
plt.ylabel("y value")
plt.title('Sin and Cos example')
plt.legend(loc='upper right')

# Get out the cheat sheet and try a few things https://matplotlib.org/cheatsheets/_images/cheatsheets-2.png
#   Plot tan as well as sin and cos
#   Change the colors of the lines
#   Move the legend somewhere else
#   Reduce the number of data points to 10 and draw just markers (no lines)

# ----------- Use-case 2: More than one plot in a window -------------------
# Code from the tutorial

# I like to do this so I don't have to change all of the subplots later if I decide to add another row...
nrows = 1
ncols = 2

# Things to notice: 1) it made a new window. That's because subplots makes a new window. 2) The size of the window -
#   short and wide. You can re-size the window in the usual way
fig, axs = plt.subplots(nrows, ncols, figsize=(3, 6))

# Add a title to the window
fig.suptitle("Trigonometry")

axs[0].plot(t_values, y1_values, '-b', label="Sin")
axs[0].plot(t_values, y2_values, '-g', label="Cos")
axs[0].set_title('Sin and cos')
axs[0].set_xlabel('t values')
axs[0].set_ylabel('y values')
# Notice that THIS one doesn't have a set.
axs[0].legend()   # Without explicit instructions it will put it wherever it deems best

# Now do a SECOND plot that is a circle. Notice axs[1] instead of axs[0]
axs[1].plot(y1_values, y2_values, '--b', label='circle')
axs[1].set_title('Circle')

# Notice that the circle does not look like a circle - this fixes it, by making the axes equal size.
axs[1].axis('equal')

# Edit this code to
#  1) Make 3 subplots, cos+sin, tan, and a circle
#  2) Be wider instead of tall when created

#  ------------------------- Use case 1, answers ---------------------------

# To simplify things, I made a second t values for the markers
t_values = np.linspace(-np.pi, np.pi, num=200)
t_values_markers = np.linspace(-np.pi, np.pi, num=10)
y1_values = np.sin(t_values)
y2_values = np.cos(t_values)
y3_values = np.tan(t_values)
y_marker_values = np.sin(t_values_markers)

# Clear out the old drawing - note that plt.figure(1) gets the first figure made above
plt.figure(1)
plt.clf()

# Here's the three plot commands with the different color/linestyle options
#   Note that order doesn't matter, except for t, y, and the format string, as long as you use the
#   foo= syntax
plt.plot(t_values, y1_values, color='aqua', label='sin', linestyle='-')
plt.plot(t_values, y2_values, label='cos', linewidth=2)
plt.plot(t_values, y3_values, linestyle='--', color='green', label='tan', linewidth=1)
#  red and no line - these two commands are identical, btw
plt.plot(t_values_markers, y_marker_values, 'rD')
plt.plot(t_values_markers, y_marker_values, linestyle='none', color='red', marker='D')

# Here's the add labeling stuff
plt.xlabel("t value")
plt.ylabel("y value")
plt.title('Sin and Cos example')

#  Notice that, because we didn't label the markers, they don't show up in the legend.
plt.legend(loc='upper left')


# --------------------------- Use case 2, answers --------------------------
# I like to do this so I don't have to change all of the subplots later if I decide to add another row...
nrows = 1
ncols = 3

# Change both ncols and figsize to be 3 and the wider shape
fig, axs = plt.subplots(nrows, ncols, figsize=(6, 3))

# Add a title to the window
fig.suptitle("Trigonometry")

axs[0].plot(t_values, y1_values, '-b', label="Sin")
axs[0].plot(t_values, y2_values, '-g', label="Cos")
axs[0].set_title('Sin and cos')
axs[0].set_xlabel('t values')
axs[0].set_ylabel('y values')
# Notice that THIS one doesn't have a set.
axs[0].legend(loc='upper left')   # Without explicit instructions it will put it wherever it deems best

axs[1].plot(t_values, y3_values, '-b', label="tan")
axs[1].set_title('Tangent')
axs[1].set_xlabel('t values')
axs[1].set_ylabel('y values')

# Change this to be axs[2] so it'll be the 3rd window
axs[2].plot(y1_values, y2_values, '--b', label='circle')
axs[2].set_title('Circle')

# Notice that the circle does not look like a circle - this fixes it, by making the axes equal size.
axs[2].axis('equal')

# Close all the windows - put a break-point here
plt.close('all')
