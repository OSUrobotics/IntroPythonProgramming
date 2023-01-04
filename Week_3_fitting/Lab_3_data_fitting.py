#!/usr/bin/env python3

import numpy as np
import json as json
import matplotlib.pyplot as plt
import csv
from numpy.polynomial import polynomial


# ------------------------- Part 1: Pick y/n ----------------------
# Can you use the finger 1 stop time and max value to tell the difference between successful and not?
# Lab instructions: https://docs.google.com/presentation/d/1NtoXYbl2nq1dkIU0KQE8ogjSCfb22wgLigY3JJpHHGI/edit?usp=sharing

# Read the same data in as for pre_lecture_3.py data in and put it in the data_ variables

# YOUR CODE HERE
# Read in week3_Motor position f1_success and failed
data_successful = ...  # week3_Motor position f1_successful.csv
data_failed = ...  # week3_Motor position f1_failed.csv

#----------------------------- Box plot of fitted lines for all data
# In the pre-lecture you fitted the line to just one row each of the successful/failed picks. In this lab you'll fit
#   the line to ALL of the picks. For each pick, save the end point (time and y_max value of the motor). You'll be
#   making a box plot of this data to see if it looks different for successful versus failed picks.
#
# Why a box plot? Box plots are better for visually showing multiple distributions in the same plot, where they can be compared side-by-side
#
# See lab slides for what this should look like when you're done

# ---------------------- Fit line code ---------------------------
# You'll need your fit_line_to_middle_bit function - two choices
#   1) Just copy it over here
#   2) Use an import statement: from [file name] import fit_line_to_middle_bit

# YOUR CODE HERE

# -------------------- Box plot ---------------------
#  Use a box plot to show the range of means for the successful versus the failed
#
# Suggested order of implementation:
# 1) create a function that loops over all the data and accumulates the end points in an nx2 numpy array
# 2) Use that function to do both the successful and the failed data
# 3) For plotting, try calling box plot with just one column of data. Then add the others.
#   Note that boxplot uses labels instead of label and you can say where on the x axis to put the box plot using positions
#
# Left window: t values of max point
# Right window: y values of max point

# YOUR CODE HERE

# -------------------- Part 2: Fit a curve to the summed wrist force data ---------------------

# Data to plot: sqrt (sum x,y,z (wrist force data)^2)
#
# First step: Calculate the data
#
# Read in wrist force data, sum it, and (optional) write it out to two csv files (one for successful, one for failed)
#   Feel free to swipe code from Lecture_3_data_analysis.py to do this
#   The data files are also in the directory, so you can read them in if you're having trouble doing it yourself


# YOUR CODE HERE
data_wrist_force_successful = ...
data_wrist_force_failed = ,,,

# Second step: Fit a cubic to the first rows of the successful and failed plots
# I've copied over the code from Lecture 3 - you just need to fit the polynomial and plot that, too
n_rows = 6
n_cols = 6
fig, axs = plt.subplots(n_rows, n_rows, figsize=(10, 10))
for p in range(0, (n_rows // 2) * n_cols):
    r, c = p // n_cols, p % n_cols
    axs[r, c].plot(ts, data_wrist_force_successful[p])
# YOUR CODE HERE
    axs[r, c].set_title(f"{ch_name} summed" + f" suc {p}", fontsize=10)

for p in range(0, (n_rows // 2) * n_cols):
    r, c = 3 + p // n_cols, p % n_cols
    axs[r, c].plot(ts, data_failed[p])
# YOUR CODE HERE
    axs[r, c].set_title(f"{ch_name} summed" + f" fail {p}", fontsize=10)

plt.tight_layout()
plt.close(fig)

