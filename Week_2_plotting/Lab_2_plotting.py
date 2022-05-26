#!/usr/bin/env python3

# Anything numpy-ish will start with np.
# Don't forget to add in matplotlib
import numpy as np
import json as json
import matplotlib.pyplot as plt

# Read in the data from lab 1 (or Homework 1)
# Read the data in
pick_data = np.loadtxt("../Week_1_arrays/Data/proxy_pick_data.csv", dtype="float", delimiter=",")

try:
    with open("../Week_1_arrays/Data/week1_check_results.json", "r") as fp:
        pick_data_description = json.load(fp)
except FileNotFoundError:
    print(f"The file was not found; check that the data directory is in the current one and the file is in that directory")

data_channels = pick_data_description["Data channels"]

# Create the plotting window - make sure there are enough subplot areas to plot all of the data channels
nrows = 2
ncols = 4
fig, axs = plt.subplots(nrows, ncols, figsize=(6, 4))

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
time_step = 1.0 / 30   # Seconds
# Create a numpy array that starts at 0, ends at number of time steps * time_step, and has step size time_step
#   See np.arange
ts = np.arange(start=0, stop=pick_data_description["n_time_steps"] * time_step, step=time_step)

# Get the channel data
wrist_force_channel_data = pick_data_description["Data channels"][2]

# Plot the x, y, z channels
channel_labels = ['x', 'y', 'z']
color_choices = ['lime', 'aqua', 'orange']  #  OR
fmt_choices = ['-b', '.g', '--k']
for i in range(0, wrist_force_channel_data["dimensions"]):
    start_index = wrist_force_channel_data["index_offset"] + i
    y_data = pick_data[0, start_index::pick_data_description["n_total_dims"]]

    # Now actually plot the data
    axs[0, 0].plot(ts, y_data, color=color_choices[i], label=channel_labels[i])

# Don't forget the labels
axs[0, 0].set_xlabel('Time (seconds)')
axs[0, 0].set_ylabel('Force (N)')
axs[0, 0].set_title(wrist_force_channel_data["name"])
axs[0, 0].legend('upper left')


# --------------------------- Part 2 -------------------------------
# Plot the Wrist torque data in the second window.
#
# You can do this one of three ways; note that in the hwk you'll need to do the 3rd option (with some help), but
#   if you want to try it now, feel free.
#
# Option 1: Copy and paste the code from above and change the relevant data/lines of code (axs[], names/titles, start index)
# Option 2: Write a for loop that loops over all the data channels and plots all of them (swipe from HW 1)
#   Note: You will need a second for loop for the dimensions (see HW 1)
#   Note: For the axes, you'll need row-column indexing to convert from the channel number back to a row column
# Option 3: Encapsulate the plotting part in a function then call that function in a for loop
#   - pass in the axes to plot in, along with t values (or create them within the function)
#   - do the x,y,z loop inside of the plot

def plot_channel(axs, ts, data, channel_info, n_total_dims):
    """ Plot all of the dimensions for a given channel
    @param axs - the place to pot in
    @param ts - the time steps to use
    @param data - the numpy array from the csv file (pick_data)
    @param channel_info - a dictionary with the channel info, eg, Wrist force (from the json file)
    @param n_total_dims - total number of columns per one time step
    @returns - nothing """

    channel_labels = ['x', 'y', 'z']
    color_choices = ['lime', 'aqua', 'orange']
    for i in range(0, channel_info["dimensions"]):
        start_index = d["index_offset"] + i
        y_data = data[0, start_index::n_total_dims]

        # Now actually plot the data
        axs.plot(ts, y_data[:len(ts)], color=color_choices[i], label=channel_labels[i])

    # Label the plot; use unit from the data description
    axs.set_xlabel('Time (seconds)')
    axs.set_ylabel(channel_info["units"])
    axs.set_title(channel_info["name"])
    axs.legend(loc='upper left')

axs[0, 0].clear()

# If you want to do the for-loop option, this is what it looks like. The i // ncols and i % ncols get the
#   row and column out. Enumerate generates 0, 1, etc
ts = np.arange(start=0, stop=pick_data_description["n_time_steps"] * time_step, step=time_step)
for i, d in enumerate(pick_data_description["Data channels"]):
    plot_channel(axs[i // ncols, i % ncols], ts, pick_data, d, pick_data_description["n_total_dims"])

plt.close()
