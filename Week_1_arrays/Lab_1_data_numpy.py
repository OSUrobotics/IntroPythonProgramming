#!/usr/bin/env python3

# Anything numpy-ish will start with np.
import numpy as np
import json as json

# Overall objectives, weeks 1 & 2
#   Simple statistical analysis of data
#
# Motivation: Whether you're in engineering or business or health care - almost any field nowadays - you need to be
#  able to work with data. Just about every thing that touches a computer now has the ability to store data. Most
#  of this data will be numbers, but sometimes it will be qualitative data (think 3 people like this, 10 people don't).
#  You can do a lot of data analysis with spreadsheets, but at some point it's almost always easier to write some code
#  to either *put* data into a spread sheet in a form that's useful, to *pull* specific data from one (or more)
#  spreadsheets, or to automate some processes (like creating six custom plots from this month's data showing price
#  trends). Being able to write a bit of code to clean up or re-purpose data is really useful, and not too difficult.
#
# Lab week 1:
#   Read in data, re-arrange it, and use it to do (text-based) statistical analysis
# Lab week 2:
#   Plot the data you worked with in lab week 1
# Homework weeks 1 & 2:
#   Use a separate file to read in information about the first file in order to do more complicated re-arrangement of data
#   Plot that data
#
# Some notes on the data you'll be working with. This is real data captured by a robotic hand designed to pick fruit.
#  The hand is instrumented with a couple sensors (IMUs in the three fingers, force and torque information at the wrist and
#  information from the motors driving the three fingers). More information here:
#
# Big picture: We want to know if we can detect if the apple was picked or not from the sensor data. Each row of
#  the Data/proxy_pick_data.csv file is data from a single picking trial. Each group of n columns represents one
#  time step. We want to plot/analyze data from different data channels to see if there is a difference between
#  the successful and unsuccessful picks.
#
# For this lab the goal is to pull out one data channel (the wrist force-torque sensor) and print out statistics for
#  failed versus successful picks. Yes, you could do all of this by manually going into the spreadsheet, sorting
#  columns, and setting up some spreadsheet formulas. That works for one data channel... but what if you want to do a
#  different one? Or the data file format changes because someone added another sensor? Or you're asked to throw
#  out the biggest n samples?
#
# Yes, this is going to be frustrating/seem like a lot of work for nothing the first time you do it. The point is not
#  to do this particularly task, but to learn how to access data in dictionaries, lists, and numpy arrays to "pull out"
#  data that you're interested in. Yes, I could just tell you to use numpy slicing to pull out every 15th column,
#  starting with the 3rd column, and sort by the last column, but where would the fun be in that?

# Read in the data. First step, read in the data from Data/proxy_pick_data.csv and put it in a numpy array
#  - see numpy loadtxt and a_tutorial_numpy.py
#

# Read the data in and put it in the pick_data variable (see tutorial - don't forget to set the delimiter)
# YOUR CODE HERE
pick_data = ...

# Print out the number of rows in pick_data (should be 660)
# YOUR CODE HERE
print(f"Number of picks: {}")

# The format of the spreadsheet data is given in Data/data_format.json. Open up the file using any text editor and
#   look through it to see if it makes sense. Also open up proxy_pick_data.csv in a spread sheet editor and make
#   sure you understand the data format.

# This reads in the json data
try:
    with open("data/proxy_data_description.json", "r") as fp:
        pick_data_description = json.load(fp)
except FileNotFoundError:
    print(f"The file was not found; check that the data directory is in the current one and the file is in that directory")

# Figure out how many data channels there are, total, for one time step
#  Step 1: Figure out how to get the "Data channels" list out of pick_data_description
#   Note: pick_data_description is a dictionary.
# YOUR CODE HERE
data_channels = ...

# Step 2: Loop over the data channels and add up the total number of dimensions
#   for each channel
#      add in the number of dimensions
# Check in proxy_pick_data.csv that the number of dimensions you found was where the data repeats itself
# Should be 17, 33
n_total_dims = 0
# YOUR CODE HERE
#. for each item in data channels
#.    Get the number of dimmensions in that element and add it to n_total_dims
#.  Note that each item in data channels is a dictionary
print(f"Number of data channels items in list: {}, total summed number of dimensions: {n_total_dims}")

# Now do a bit of math to figure out the total number of time steps (number of columns / number of dimensions)
#  Make sure this is an integer
# And remember that there is one extra column (the last one) that stores if the pick was successful or not
# YOUR CODE HERE
n_time_steps = ...

# Should be 40
print(f"Number of time steps: {n_time_steps}")

# Check your slicing - pull out the Z value of the Wrist torque for all picks
#  You are free to use the fact that the name of the data channel you want is Wrist torque, but you should get
#  the actual index value from the dictionary (suppose someone changed the order of the data...).
# There are several ways to do this; the simplest is to loop through all of the data channels looking for the one
#  that is called "Wrist torque" and then set the index offset value from that. It would be a good idea to check that you
#  actually found the right starting index by looking at the .json file
#    Note: Use ==, not is, for the string comparison
# The z channel is the 3rd one (the starting index field in the json file gives the x channel).
channel = "Wrist torque"
index_wrist_torque_offset = -1  #  Set it to a value that is NOT a valid index


# YOUR CODE HERE

# for each channel in data channels
#     if this channel's name is the one I'm looking for    
#.        Set index_wrist_torque_offset (don't forget the z offset)


# Check that you actually set the value somewhere in the loop - this is "defensive coding"
if index_wrist_torque_offset is -1:
    print(f"Error: No channel {channel} found")

print(f"Offset for wrist torque : {index_wrist_torque_offset}")

# Now use slicing to get out all of the wrist FT data and calculate the min and the max
# This is a pretty complicated slice. Steps to get there:
#  First, use the slice operator, selecting all rows and columns, [:, :] to calculate the minimum across the entire
#   matrix of data. This should be the same as np.min(pick_data)
#  Now change the column slice from all columns to starting at the offset value.
#  Now change the slice to take a step/stride of n_total_dims instead of 1
#  Note: You don't need to put an end value in - just leave it blank
# Remember: The data is in pick_data

# YOUR CODE HERE
min_wrist_torque = ...
max_wrist_torque = ...

print(f"Minimum {min_wrist_torque} and maximum {max_wrist_torque} value of wrist torque z channel")

# Now for the fun one - do the same but ONLY for successful (last column is 1) picks versus unsuccessful (last column
#   is 0)
# Note: Use == 1, not is 1
# It may be helpful here to explicitly create a boolean array that is # rows X 1 to use as the row index for the
#  pick_data, rather than trying to do it "in-place". Then you can check that the array is correct.
#
# This boolean array replaces the **:** row index: **data[boolean_array, start:end:step]**
#
# The boolean array is created by doing a comparison, for example, **data == 1**. In this case, you want to get out all rows,
#   but only the LAST column of the data, and compare it to 1.

# YOUR CODE HERE
min_wrist_torque_successful = ...
max_wrist_torque_successful = ...

min_wrist_torque_unsuccessful = ...
max_wrist_torque_unsuccessful = ...
print(f"Successful: Minimum {min_wrist_torque_successful} and maximum {max_wrist_torque_successful} value of wrist torque z channel")
print(f"Unsuccessful: Minimum {min_wrist_torque_unsuccessful} and maximum {max_wrist_torque_unsuccessful} value of wrist torque z channel")

# Optional: print out all of the indices where the maximum value was reached
#  np.where is the method you want; it returns a tuple (think list) with two lists, one for each dimension.
# To get out the pairs of indices, you want the first element of the first list and the first element of the second list,
#   and so on. You can do this with a for loop, using zip to zip together the two arrays.
#     for r, c in zip( ):
#
# Some gotchas: it's easiest to do where on the entire pick_data set, but then you'll get indices that are NOT the
#  ones you want (other data channels). If you do max on the sliced matrix, then you'll get indices on the sliced
#  matrix, not the original... So either you need to filter out indices that are not the channel you want with an
#  if statement (the modulo operator % is useful here) OR adjust the column index by doing offset + index * n_total_dims.
#
# A quick check to see if you got your indexing correct is to print out the value at the index and make sure it's the
#  max value you're looking for
# Use where to get out the indices. You can use == OR np.isclose() here; either works, but np.isclose will give
# you slightly more results

# YOUR CODE HERE
all_indices_from_where = ...
# for all row, column in all_indices_from_where
#.   if this is the column for wrist torque 
#.      print(f"Row: {r}, Time step: {c // n_time_steps} Successful y/n: {pick_data[r, -1] == 1}, value: {pick_data[r, c]}")
