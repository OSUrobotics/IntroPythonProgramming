#!/usr/bin/env python3

# -------------------HW 1: Statistical analysis of data using numpy and matplotlib
# Resources: Lecture slides describing the homework: https://docs.google.com/presentation/d/1ef0msC9XIT37_Yg94Cf4TL9VBgbIIfkKik8jgshskjE/edit?usp=sharing
#
# Please do lab 1 before starting this homework, and do lab 2 before tackling problem 4 on (the plotting part).
#
# In this homework the focus is on code design. Most of the functionality of the code will be what you did in the labs. I don't expect you to do the code design; I've provided that. Just pay attention to how a couple of tools (functions, dictionaries) can make your code a little more re-usable, cleaner, and less prone to error.
#
# Learning to read code is also as important as writing code. This is (hopefully) a gentle introduction to using/interacting with more advanced concepts/syntax/semantics.

# Where you're going with Problems 1, 2, and 3: Take a look in the Data directory at the week_1_check_results.json file. This is what your code should produce after those problems.

# Make sure numpy and json load are available (see lab 1)

# YOUR CODE HERE
# TODO: put the numpy and json imports here so you can use those libraries (see the top of Lab 1 & 2)

# Week 1: Problem 1: Read data ------------------------------------------------
#  Read in both the data file and the file that describes what's *in* the data file. See lab 1

# YOUR CODE HERE
pick_data = ...
# Code to read in pick_data_description
pick_data_description = ...
# Code to get data_channels out of pick_data_description
data_channels = ...

# Calculate the number of time steps and number of data dimensions as before, but this time, store the values
#  back in pick_data_descriptions for safe-keeping
#
# Why: Two reasons. First, that information, conceptually, belongs there. As we'll see in later homeworks, having all
#  related data in a dictionary means you just have to pass around the dictionary, not all of the individual variables.
#  Second, it's always a good idea to minimize the number of loose variables floating around.

# Drawbacks: There's a tiny overhead for accessing values from a dictionary (eg, d["foo"]) and you have to remember
#  what key you used when you put the data in.
# YOUR CODE HERE
pick_data_description["n_total_dims"] = ...
pick_data_description["n_time_steps"] = ...

# Week 1: Problem 2: Prints stats for each sensor channel ------------------------------------------------
#
# This is almost entirely copying your code from lab 1 into a new structure that makes it easier to generalize
#   your code. I've provided the structure, and broken the process up into 3 steps.
#
# - Generalization 1: Put the code that calculates the statistics into a function
# - Generalization 2: Store the results in a dictionary so it's labeled and you don't have to worry about variable name re-use
#
# Note: You should not use pick_data and pick_data_description inside your function
# I've set this up so that you can write the function, then check it, then incrementally add in the for loops.
#  You're free to jump straight to step 3 if you want, but if it doesn't work, please go through steps 1 and 2 before asking the TA for help.
#

def get_stats_for_channel(data, channel_info, xyz_dim, n_total_dims):
    """ Get the min, max, mean, sd for the given channel
    @param data - the numpy array from the csv file (pick_data)
    @param channel_info - a dictionary with the channel info, eg, Wrist torque (from the json file)
    @param xyz_dim - 0, 1, or 2 for x, y, z
    @param n_total_dims - total number of columns per one time step
    @returns - A dictionary with the statistics values """

# YOUR CODE HERE
    # This is index_wrist_torque_offset from lab 1 - the start index from the dictionary plus the dimension (xyz_dim)
    # Do the same thing you did in lab 1 (get the index_offset from channel_info) then add in the x,y,z offset
    index_offset = ... 
    
    # The np.min(data[:, start:end:stop]) code from lab replaces the 0 
    ret_stats = {"Min": 0,
                 "Max": 0,
                 "Mean": 0,
                 "SD": 0}
    return ret_stats

# Step 1 - check get_stats with the first channel of the data, first xyz dim
# You do not have to write any code here; this is for you to see if your code in the function above is correct. If it is,
#  the print statement should print out: {'Min': -11.99637522, 'Max': 8.516101548, 'Mean': -0.776128891779453, 'SD': 2.109234072491527}
#
# This is a pretty standard way to approach transitioning code into a function. Write the function header,
#  deciding what you need to pass in to the function and what it should return, then call that function with "known" data.
# Once you're sure the function is working, go to the next step
ret_stats = get_stats_for_channel(pick_data, data_channels[0], 0, pick_data_description["n_total_dims"])
print(ret_stats)

# Step 2 - Loop over all of the channels, calculating the stats for each channel, zero dimension
#   In this version, we're going to store the data back into the channel data info
# In this step, add in JUST looping over all of the channels - and leaving the dimension "hard-wired" at 0. Yes, you can jump to step 3, but then you have to debug TWO changes at the same time. It often feels a little slower to do one change, check that it's right, then do the next, but usually saves time in the long run.
#
# The check here is that you get the right min/max values for the other channels, dimension 0.
#  You're free to look at week1_check_results.json to makes sure you got it right. You should see every channel, dimension zero.

# YOUR CODE HERE
#. for each item in data channels
#.    Print the channel name
#.    Get the stats m_stats = get_...
#     print(f"  minimum: {my_stats['Min']}, maximum: {my_stats['Max']}, mean: {my_stats['Mean']}, SD: {my_stats['SD']}")

# Step 3 - Now add in a second loop that loops over the number of dimensions in the channel
#  You'll need to use a list plus an append to store the x, y, z dimensions
#   Double check that the min/max values for the x,y,z channels are all different (i.e., you got the indexing right)
#   Remember that not all channels have 3 dimensions...
#  You might find range() useful
# Store the resulting statistics back into the data channel using "stats" as the key. Note that if you do this correctly,
#  the json write in the next cell will print out a file that is identical to week1_check_results.json.

# Cute trick to map 0-2 to letters
map_to_xyz = ['x', 'y', 'z']

# YOUR CODE HERE
#. for each item in data channels
#.    Print the channel name
#.    Create an empty list d["stats"] = [] 
#.    for each dimension in channel
#.       Get the stats m_stats = get_...
#.       ... and store them in d["stats"]
#        print(f"  minimum: {my_stats['Min']}, maximum: {my_stats['Max']}, mean: {my_stats['Mean']}, SD: {my_stats['SD']}")

# Write the results back out to a text file you can read in a text editor
# I'll write the data back out for you. If you've done the steps above correctly, the file "week1_student_results.json"
#   should be exactly the same as "week1_check_results.json"

# Write the results back out to a text file you can read in a text editor

# YOUR CODE HERE
with open('Data/week1_student_results.json', 'w') as f:
    json.dump(pick_data_description, f, indent=4)

# Use this to compare your file to the check_results file
def compare_files():
    with open("data/week1_student_results.json", "r") as fp:
        student = json.load(fp)
    with open("data/week1_check_results.json", "r") as fp:
        check = json.load(fp)

    for k, v in check.items():
        try:
            if k == "Data channels":
                # The data channels list
                for i, d in enumerate(student[k]):
                    if not d == v[i]:
                        print(f"miss-match {d} {v[i]}")
                        return False
            else:
                if not v == student[k]:
                    print(f"Miss-match key-item {k} {v} {student[k]}")
                    return False
        except KeyError:
            print(f"Missing key {k}")
            return False
    return True

b_ret = compare_files()
print(f"Comparison result: {b_ret}")

# Week 1: Problem 3: Find the row(s) with the maximum peak in the Wrist torque Z channel ------------------------------
#  This is the optional problem from lab 1.
#
# Notes for problem 3
#   No for loops - do this with np.where.
#   We should be able to change channel_to_search to a different text string and it still works.
#      i.e., no "hard-wiring" the channel name/index
#
# Optional: Do this for all channels and dimensions (which DOES require a loop over the data channels)
# Recommended order of implementation:
#  Write the code for one channel
#  Create a function just like the one above (it will take the same input parameters)
#    The return value will be different - I suggest a list of tuples with [(r, c), (r, c)]
#  Copy your code for one channel into the function, and change it to take in the
#    function's input parameters
#  For the output, I suggest making an empty list, and then, in the for loop, append all valid r,c pairs onto
#    the list. Return the list.
#  Copy your for loop from above (that goes over all channels, all dimensions) and replace the function call
#    with the new one.


# YOUR CODE HERE
# This should be of the form (r,c)
row_max_wrist_torque_z = ...

# For comparing output
my_res = get_row_with_max_peak(pick_data, data_channels[1], 2, pick_data_description["n_total_dims"])
row_max_wrist_torque_z = my_res[0]


# Week 2: Problem 1a: Plot Wrist force/torque for two rows ------------------------------
#
# Plot the wrist force/torque data for the first and second row. The plots should have in them:
#   Left-hand-side: The wrist force (x,y,z), with horizontal lines for the minimum and maximum z force values
#     Title should include which pick/row this is, and if it is successful or not
#   Right-hand-side: THe wrist torque (x,y,z), with horizontal lines for the minimum and maximum z force values
#     Title should include which pick/row this is, and if it is successful or not
# Top row: row 0
# Bottom row: row 1
# See https://docs.google.com/presentation/d/1ef0msC9XIT37_Yg94Cf4TL9VBgbIIfkKik8jgshskjE/edit?usp=sharing for what
#  this should look like

# I'm going to give you a function definition for the plot. There are a lot of ways you could do this; I chose this
#  one for two reasons:
# 1) It "makes sense" that the input should be x and y values, along with information on how to label the plot
# 2) It's a look-ahead to problem 2, where we will re-factor the data into something a little more manageable
# Some observations
#   This pushes the data slicing out of this function and into the calling one
#   Your choice on how you pass the last parameter
#   The function parameters also act as "documentation" for the data slicing/extracting the pick channel
#   For this problem you can assume that the y values are 3xn (x, y, z)
#     Optional: handle the case when it's just 1 dimensional data
#   To create the horizontal lines, do a plot with (t0, tlast), (max, max)  OR use axhline
#
# Don't forget to import matplotlib
def plot_channel_row(axs, ts, ys, channel_info, which_row, pick_successful_yn):
    """ Plot a specific channel, all dimensions
    @param axs - the axes of the plot to use
    @param ts - t values of the data [1 x n time steps]
    @param ys - y values of the data [3 x n time steps] OR [1 x n time steps] (supporting the OR is optional)
    @param channel_info - the channel info from your week1_student_results.json file (which has the min and max)
    @param which_row - which row this is
    @param pick_successful_yn - was this a successful pick, y/n?"""


# YOUR CODE HERE
    # Example plot command
    axs.plot(ts, ys[0], label="x")

# Now the code to call the function. See the slides for how to do this in pieces. Start with your lab 2 code
#


# YOUR CODE HERE
n_rows = 2
n_cols = 2
fig, axs = plt.subplots(n_rows, n_cols)

# Extract data and call plot_channel_row
fig.set_tight_layout(tight=True)

# Week 2: Problem 1b: Plot Wrist force/torque for min/max wrist torque z------------------------------
#
# Find the row that has the maximum (minimum) wrist torqu z value. Plot the minimum one in the top row, the maximum
#  one in the bottom row
# Your actual plotting code (the function) shouldn't have to change, btw. Just what data you send it.
#
# Starting point: the function you wrote in the first week, get_row_with_max_peak

# YOUR CODE HERE

# Week 2: Problem 2: (optional) use reshape to make slicing not needed------------------------------
#
# np.reshape is the method you want; rearrange the data into rows, data channels, time series in each data channel (a 3 dimensional array)


# YOUR CODE HERE
n_rows = 2
n_cols = 2
fig, axs = plt.subplots(n_rows, n_cols)

# Re-organize the data into an n_picks * n_channel_dims * n_time_steps (3 dimensional) array
pick_data_reorg = ...   # Use reshape, with the correct "order" option
# ... and another array that stores just the success/fail data
pick_data_success_fail = ...

# Then this plot call should plot the wrist force data for row zero
row = 0
plot_channel_row(axs[0, 0], ts, pick_data_reorg[row, 0:3, :], data_channels[0], which_row=row, pick_data_success_fail[row] == 1)

# ... and for wrist torque data
plot_channel_row(axs[0, 1], ts, pick_data_reorg[row, 3:6, :], data_channels[1], which_row=row, pick_data_success_fail[row] == 1)

