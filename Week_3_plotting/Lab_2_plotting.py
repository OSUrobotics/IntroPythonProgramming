#!/usr/bin/env python3

# Anything numpy-ish will start with np.
# Don't forget to add in matplotlib
import numpy as np
import json as json
import matplotlib.pyplot as plt

# Read in the data from lab 1 (or Homework 1)
# Read the data in
# YOUR CODE HERE
pick_data = ...

data_channels = pick_data_description["Data channels"]

# --------------------------- Part 1 -------------------------------
# Read in the data and plot it for each of the x, y, and z channels. I recommend doing this in the following order
# Copy in your pre_lecture code and do that plot first - make sure it's working and the titles/labels etc are correct
#   Note: You'll need to change axs to axs[0, 0]
# Once that's working, add a for loop to loop over x, y, z
#   If doing a for loop is confusing, then start with just copying the code over, twice, and changing the dimension
#   you're using.
#
# [optional]
# For setting the colors and the data labels, you can either do it by hand, or setup a list and use that
#    ... and you might revisit strings to see how you can make the label from the channel's name and s

# YOUR CODE HERE


time_step = 1.0 / 30   # Seconds
# Create a numpy array that starts at 0, ends at number of time steps * time_step, and has step size time_step
#   See np.arange
ts = np.arange(start=0, stop=pick_data_description["n_time_steps"] * time_step, step=time_step)

# Get the channel data
wrist_force_channel_data = pick_data_description["Data channels"][1]

nrows = 1
ncols = 1
fig, axs = plt.subplots(nrows, ncols, figsize=(6, 4))

# YOUR CODE HERE

# --------------------------- Part 2 -------------------------------
# Plot the Wrist torque data in the second window.
#
# You can do this one of two ways; note that in the hwk you'll need to do the 2nd option (with some help), but
#   if you want to try it now, feel free.
#
# Option 1: Copy and paste the code from above (twice) and change the relevant data/lines of code (axs[], names/titles, start index) in the second copy
# Option 2: Encapsulate the plotting part in a function then call that function twice
#   - pass in the axes to plot in, along with t values (or create them within the function)
#   - do the x,y,z loop inside of the plot

# There is a way to add subplots to the current figure, but for this assignment, just close the current figure and
#  call subplots again with 1 row and 2 columns

# YOUR CODE HERE

# This ensures that the titles are not inside the other plots
fig.set_tight_layout(tight=True)

plt.close()
