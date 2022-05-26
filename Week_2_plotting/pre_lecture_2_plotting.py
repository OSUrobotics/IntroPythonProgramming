#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import json as json

# Using your code from lab 1/hwk 1, read in the pick data, the pick data description, and plot the Wrist force z
#  channel for the first row. See the Lab lecture slides for this week for the correct answer.
#   https://docs.google.com/presentation/d/1IiGGUNet-4Nj07x2cTXU6IOYXy9TSdAF5OUWCCKIYEM/edit?usp=sharing
# I recommend using the subplots approach (rather than just plot) because eventually we'll be plotting in more than
#  one plotting area

# Read the data in
#   Note the ../Week_1_arrays/ part in front - this tells the file manager to go up one directory, then
#    into the Week_1_arrays directory, which is where the data is
pick_data = np.loadtxt("../Week_1_arrays/Data/proxy_pick_data.csv", dtype="float", delimiter=",")

# Reminder: You need to change the directory when reading in the pick data description, too
# YOUR CODE HERE


# Plot the Wrist force z channel for the first row.
#
# For the t values, assume the data is sampled at 30 Hz, i.e., the time sampling is 1/30th of a second
#  Step 1: How big does the t array have to be? (hint: How many data samples are there for the wrist force data?)
#  Step 2: How do you make an array of that size with that spacing (hint: np.arange)
#


# YOUR CODE HERE
time_step = ...
# Array holding the time values
ts = ...
wrist_torque_channel_data = ...
y_data = ...

# Create the plotting window
nrows = 1
ncols = 1

# YOUR CODE HERE
fig, axs = ...

# Put a break point here to stop the code from exiting
plt.close(fig)

