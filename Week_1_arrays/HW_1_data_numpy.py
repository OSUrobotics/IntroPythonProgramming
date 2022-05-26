#!/usr/bin/env python3

# Make sure numpy and json load are available (see lab 1)

# YOUR CODE HERE
# TODO: put the numpy and json imports here so you can use those libraries (see the top of Lab 1 & 2)

# Week 1: Problem 1: Read data
#  Read in both the data file and the file that describes what's *in* the data file. See lab 1

# YOUR CODE HERE
pick_data = ...
# Code to read in pick_data_description
pick_data_description = ...
# Code to get data_channels out of pick_data_description
data_channels = ...

# Calculate the number of time steps and number of data dimensions as before, but this time, store the values
#  back in pick_data_descriptions for safe-keeping

# YOUR CODE HERE
pick_data_description["n_total_dims"] = ...
pick_data_description["n_time_steps"] = ...

# Week 1: Problem 2: Prints stats for each sensor channel
#
# This is almost entirely copying your code from lab 1 into a new structure that makes it easier to generalize
#   your code. I've provided the structure, and broken the process up into 3 steps.
#
# - Generalization 1: Put the code that calculates the statistics into a function
# - Generalization 2: Store the results in a dictionary so it's labeled and you don't have to worry about variable name re-use
#
# Note: You should not use pick_data and pick_data_description inside your function
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
ret_stats = get_stats_for_channel(pick_data, data_channels[0], 0, pick_data_description["n_total_dims"])
print(ret_stats)

# Step 2 - Loop over all of the channels, calculating the stats for each channel, zero dimension
#   In this version, we're going to store the data back into the channel data info

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
with open('Data/week1_check_results.json', 'w') as f:
    json.dump(pick_data_description, f, indent=4)


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

# Week 1: Problem 3: Find the row(s) with the maximum peak in the Wrist torque Z channel
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


# Problem 3: Extra credit - deal correctly when there are multiple places with the same min value (use data channel ??)
#
