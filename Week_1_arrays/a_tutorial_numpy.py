#!/usr/bin/env python3


# What is numpy?
#
# Numpy (and scipy) are python libraries for doing numerical and scientific calculations. Pretty much any mathematical
#   or signal processing operation you would find in a text book is implemented in one of those libraries. Much of the
#   functionality of MatLab is here, along with plotting (see matplotlib and the tutorial on matplotlib)
#
# The heart of numpy is the numpy array data structure. These are n-dimensional arrays, all of the same data type with
#   every element in a dimension the same size (unlike python lists, which can mix and match data types and array
#   dimension sizes),
#
# Because numpy arrays are all of the same type/size, it's possible to do the same operation to all of the elements
#   of an array really, really fast. This is the heart of using numpy; instead of explicitly writing for loops,
#   numpy "overrides" operations (like *, +, <, > ==) so that they happen to the entire array (all n dimensions of it)
#   all at once, in one line of code. There's still for loops in there, it's just Python is doing it for you. If you
#   find yourself writing a for loop with a numpy array, btw, chances are you shouldn't be. Not that it's wrong, it's
#   just really, really slow.
#
# Finally, there are all of the operations (min, max, sum, filter, etc) in numpy/scipy that use numpy arrays as input.
#  These are very powerful, but it can be challenging to set up data and function parameters correctly to get them
#  to work the way you want. We'll cover basics here, and more in-depth later.

# This is the way I like to import numpy. All numpy operations will start with np. I just find it easier (when reading
#   the code) to have this visual cue that this function/operation came from numpy. It also prevents name conflicts -
#   for example, if you accidentally name a variable "min" you won't "overwrite" numpy's min. Also, if you cut and
#   paste your code somewhere else, it's easier to get it working without name conflicts.
import numpy as np

# If you use this import, then you don't need the np. in front. Saves typing, but it means that ALL of the names/
#   functions etc in numpy are now in your list of variables.
# import numpy

# If you want to do a mix of the above, but just bring in the variables/data structures that you need, you can
#   use one of the following. If you're using a lot of numpy operations/variables than it can get annoying to have to
#   include all of them, though
# from numpy import array as nparray
# from numpy import array

# ------------- Making a numpy array -----------------------------
#
# There are three main approaches to/reasons for making a numpy array
#  1) You have data in a file - spreadsheet, csv, image, etc
#  2) You need a "blank" array of data that you fill in with some default value
#  3) You're combining data from existing numpy arrays
#
# We will go over each in turn
#  See also: https://numpy.org/doc/stable/user/basics.creation.html
#  if you don't see a construction method here that meets your needs

#  From a file
# There are two cases here
#   1) a single file with all the data (and no extra stuff like headers), eg, a csv file of numbers, an image
#   2) a spreadsheet with headers and other data that you don't necessarily need
#
#  For 1) there's almost always a numpy function that will do the data reading and return a numpy array. For 2),
#   the best approach is to read the data into a python list and then create the numpy array from the list. This avoids
#   the problem of needing to know the data sizes in advance.
#    If you know the data size in advance then you can use the "blank" approach above to create the numpy array and
#    read data into it.
#  Whatever you do, avoid creating and destroying numpy arrays over and over again (think list append); list data
#    structures are setup to handle this a lot better than numpy arrays.

# Example 1: Reading in a csv file of numbers directly into a numpy array
file_name = "Data/proxy_test_grasp.csv"
# This is a first example of the fun of numpy/scipy function parameters. Google numpy loadtxt to get a list of
#   all possible parameters - all of which have default values, except the file name.
#   Here, we override specific parameters (what type of data it is and what the delimiter is)
data_from_csv = np.loadtxt(file_name, dtype="float", delimiter=",")

print("Example 1: Data from a csv file")
print(f"Data dimensions: {data_from_csv.shape}, total number of elements: {data_from_csv.size}")

# Example 2: Converting a list to a numpy array (note, we'll cover advanced file reading later)
my_list = [[0, 1], [2.0, 4.0], [5.0, 10.0]]
data_from_list = np.array(my_list)

print("Example 2: Create a list then convert a list to a numpy array")
print("Original list, notice flat format")
print(my_list)
print("List as numpy array, notice matrix format")
print(data_from_list)
print(f"Data dimensions: {data_from_list.shape}, total number of elements: {data_from_list.size}")

# Example 3: Creating a "blank" array, either of zeros, ones, a range of numbers, or random numbers
#  dtype is optional - you can set it to int for integers, bool for booleans, etc
#  A 3 X 5 X 2  array of zeros
print("Example 3: Zeros, ones, and random - making numpy arrays from scratch")
# shape/dimensions can be a list OR a tuple (3, 5, 2) - doesn't matter
#   Note: One of the most common errors is to forget the [] or the () around the list of dimensions - you don't need
#   it for one dimensional arrays, but you will for more than one - otherwise, you get a TypeError: data type not understood
data_zeros = np.zeros([3, 5, 2], dtype=float)
print(f"Number of dimensions: {data_zeros.ndim}, dimension sizes: {data_zeros.shape}, total number of elements: {data_zeros.size}")

# Making an array of ones of the same size as data_from_list
#  .shape contains the dimensions of the array - number of rows, columns, etc
#  It is a tuple, so you can't change it
data_ones = np.ones(data_from_csv.shape)
print(f"Data dimensions: {data_ones.shape}, total number of elements: {data_ones.size}")

# Making an array of numbers starting and stopping at given values (linspace)
#  15 numbers, starting at -1 and going to 1
data_evenly_spaced_numbers = np.linspace(-1.0, 1.0, 15)
print(f"Linspace dimensions: {data_evenly_spaced_numbers.shape}, total number of elements: {data_evenly_spaced_numbers.size}")
print(f"First value: {data_evenly_spaced_numbers[0]}, last value: {data_evenly_spaced_numbers[-1]}")

# Making an array of random numbers
#  Don't be confused by the parameter being called size - it can take a tuple of dimensions
data_random = np.random.uniform(low=-1, high=1, size=(3, 10))
print(f"Random uniform data, size {data_random.shape}")
print(data_random)

# Operations with numpy arrays
# There are two concepts here, one easy, one hard
#  Concept 1: operators (+, -, <, etc) are all automatically done on all elements (for loops)
#     All arrays in the equation have to have the same dimensions
#  Concept 2: If statements are accomplished using boolean indexing [if statement]
#     Using [] selects a part of the array - so the dimensions may be different
#  Operations usually create new arrays.

# Simplest example - apply 2 * x + 1 to all elements of the array, and store in a new array
data_new_csv = 2 * data_from_csv + 1
#  min/max are numpy operations that do the min/max across ALL of the dimension - see below for how to do min/max
#    across just one dimension
print(f"Original minimum: {np.min(data_from_csv)} and maximum: {np.max(data_from_csv)}")
print(f"New minimum: {np.min(data_new_csv)} and maximum: {np.max(data_new_csv)}")

# A more complicated example - shift and scale the entire data set so that the min is zero, the max is one
min_all_data = np.min(data_from_csv)
max_all_data = np.max(data_from_csv)
shift_amount = min_all_data
scale_amount = 1.0 / (max_all_data - min_all_data)
data_new_csv = scale_amount * (data_from_csv - shift_amount)
print(f"Shifted minimum: {np.min(data_new_csv)} and maximum: {np.max(data_new_csv)}")

# Now for the if statement. There are a handful of places in the data where there are zeros. These are places where
#  there wasn't any valid data, so they shouldn't be included when doing a mean calculations.
mean_including_zeros = np.mean(data_from_csv)
# The [data_from_csv != 0] selects all of the data that is not 0.0
#   Note: You should use isclose() for most floating point comparisons, not == 0
mean_not_including_zeros = np.mean(data_from_csv[data_from_csv != 0])
print(f"Means with {mean_including_zeros} and without {mean_not_including_zeros} zeros")

# [Optional] This is an example where you DO need to use a for loop - because you're doing something different for
#   each column of the data.
# What this code does: Does a similar shift/scale as above, but this time, on each column of the data individually
# The idea is that each row is one run from an experiment, each column represents a single data value that you're
#     capturing. You want to "normalize" the data for each value so that the mean is zero and the data has a standard
#     deviation of 1
# Pre-alloc the matrix to put the data back into - since we know the size of the data, it's easiest to make a new
#  numpy array of the right size and then copy data in and edit it after it's copied in
data_new_csv = np.zeros(data_from_csv.shape)
# for each column in the data
for c in range(0, data_from_csv.shape[1]):
    # Copy the data from the old array to the new one
    #   Note the : and the ,  and the [r,c] - array indexing/slicing for numpy arrays is pretty much the same as for lists
    #   Unlike lists, this actually copies the data over
    data_new_csv[:, c] = data_from_csv[:, c]  # All rows, column c

    # Making a variable of this here so you can see it/use it
    non_zero_data_in_col = data_new_csv[:, c] != 0  # A boolean array that is false for all zero elements
    mean_column = np.mean(data_new_csv[non_zero_data_in_col, c])  # Use only those row elements that are non-zero
    std_column = np.std(data_new_csv[non_zero_data_in_col, c])
    # Shift and scale - but only the non-zero (valid) numbers
    #  We'll do this in-place - on the RHS we calculate the new values, then the = sign assigns them to the appropriate
    #     values on the LHS. Similar to
    #  for all r in column c
    #     if non_zero_data_in_col[r] is True
    #          non_zero_data[r,c] = (non_zero_data[r,c] - shift) / std_column
    data_new_csv[non_zero_data_in_col, c] = (data_new_csv[non_zero_data_in_col, c] - mean_column) / std_column

# Because we've normalized all the columns individually, the mean and standard deviation of the ENTIRE data
#  set should be close to 0, +=1
print(f"Mean {np.mean(data_new_csv)} and std {np.std(data_new_csv)} for ALL data")

# ... but is we ask for the mean, std for one row it is NOT
print(f"Mean {np.mean(data_new_csv[0, :])} and std {np.std(data_new_csv[0, :])} for one row")


# ------------------ Numpy gotchas ----------------------------

# Size and Shape are often confused for each other, and doubly so when the numpy array is one dimensional (in which
#   case there is an additional confusion between row-column and column row). This confusion doesn't usually result
#   in an Python error, but is usually some version of "I thought that array would be bigger (or smaller)", or "I
#   thought I made a matrix nxm", and occasionally as a mis-matched size array or invalid index error.
#
# One quick check (for both this error and the next one) is to print out (or check in the debugger) BOTH
#   print(f"Size {a.size} and shape {a.shape} of array a"). That way, you don't have to remember which is which..
#
# Shape is the dimensions of the array, Size is the number of elements. Shape is a tuple, Size is an integer
#   So an np array with shape (3, 6) will have 18 = 3*6 size. 1 dimensional arrays will usually have shape (1, size),
#   although sometimes (for example, grabbing a column out of a matrix) you may end up with (size, 1).
#
# Here are some common errors/examples

# Make a 3x6 matrix
my_orig_matrix = np.ones((3, 6))

# Accidental use of size instead of shape
my_incorrect_size_matrix = np.ones(my_orig_matrix.size)
# Correct way to create a matrix of the same dimensions
my_correct_size_matrix = np.zeros(my_orig_matrix.shape)

print(f"Orig shape {my_orig_matrix.shape} and size {my_orig_matrix.size}")
print(f"Incorrect matrix shape {my_incorrect_size_matrix.shape} and size {my_incorrect_size_matrix.size}")
print(f"Correct matrix shape {my_correct_size_matrix.shape} and size {my_correct_size_matrix.size}")

# This generates an error because the two matrices are different shapes (but same size)
# generates ValueError: operands could not be broadcast together with shapes (3,6) (18,)
# oops = my_orig_matrix + my_same_size_matrix

# This is even worse: this creates a 1x1 array set to the value 18:
my_oops_matrix = np.array(my_orig_matrix.size)
# This also doesn't work - this creates a 1x2 array set to the value (3,6):
my_oops2_matrix = np.array(my_orig_matrix.shape)
# ... This creates an array of the same dimensions and values (use zeros(m.shape) if you want just zeros)
my_correct_assign_matrix = np.array(my_orig_matrix)

print(f"Oops matrix shape {my_oops_matrix.shape} and size {my_oops_matrix.size}")
print(f"Oops matrix 2 shape {my_oops2_matrix.shape} and size {my_oops2_matrix.size}, values {my_oops2_matrix}")
print(f"Correct matrix shape {my_correct_assign_matrix.shape} and size {my_correct_assign_matrix.size}")

# ----------------------- Assignment errors/problems -----------------
# There are two common errors with numpy arrays: Indexing errors (index out of bounds, missing dimension) and
#  trying to do mathematical operations on arrays that have different dimensions
#
# Most common error - matrices are different sizes, usually because one is the transpose of the other or because
#  you grabbed a subset of a matrix and tried to set it to the original matrix
my_matrix = np.random.random([15, 15])
my_matrix_sub = my_matrix[2:-2, 2:-2]
# my_add_two_different_sizes = my_matrix + my_matrix_sub
# Generates this error
#   ValueError: operands could not be broadcast together with shapes (15,15) (11,11)
# Which should be read as: I have an 11x11 matrix that I tried to assign to a 15x15 matrix

# ... or, you thought my_matrix_sub was my_matrix and tried to get the last element
# Generates this error:
#   IndexError: index 14 is out of bounds for axis 0 with size 11
# which should be read as: The index I used for the first dimension (14) was too big (the matrix is 11x11)
# print(f"Generate an index error: {my_matrix_sub[14, 3]}")

# numpy is pretty good about lists - whether they're 15, 1x15, or 15x1 you can still add/multiply them together -
#  numpy can find a way to "line them up". It will not, however, line up a 3x5 with a 1x15. You can
#  use reshape to make this work, btw
my_list_v1 = np.linspace(-1, 1, 15)
my_list_v2 = np.ones([15, 1])
my_list_v3 = np.ones([1, 15])
my_list_v4 = my_matrix[:, 0]
my_list_v5 = my_matrix[0:3, 0:5]

all_lists = [my_list_v1, my_list_v2, my_list_v3, my_list_v4, my_list_v5]
# Print them all out
for i, l in enumerate(all_lists):
    print(f"my_list_v{i+1} shape {l.shape} and size {l.size}")
    for j, l2 in enumerate(all_lists):
        # try-except is an "if" statement but the if statement conditional is whether or not Python threw
        #  an error anywhere (in this case, a ValueError, which is what you get if the matrix sizes are mis-matchec)
        try:
            res = l + l2
            print(f"List {i+1} and list {j+1} can be added")
        except ValueError:
            print(f"List {i+1} and list {j+1} can NOT be added")
            print(f"Reshaping so it will work")
            res = l.reshape([1, 15]) + l.reshape(([1, 15]))

        print(f"res shape {res.shape} and size {res.size}")

# Sometimes you just forget to put in the index for some of the dimensions... unfortunately, this actually works
#  (does not cause an error) because my_matrix[3] is a single number, so numpy adds that single number to the
#  entire list
oops_wrong_thing_added = my_matrix[3] + my_list_v1

# This is what I actually meant to do - grab the 3rd row and add it to my_list_v1
#    Notice the 3, : which grabs the *entire* 3rd row
enough_dims = my_matrix[3, :] + my_list_v1
print(f"Enough dims {enough_dims.shape} and size {enough_dims.size}")

# One last one that is pretty common - rows and columns transposed, which can yield an index error or a value error
my_non_square_matrix = np.random.random([3, 6])
# Index error
# row_column_transposed_index = my_non_square_matrix[5, 2]
# Value error
my_non_square_matrix_transposed = np.random.random([6, 3])
# oops_wrong_dims = my_non_square_matrix + my_non_square_matrix_transposed
# Quick fix - transpose before adding
correct_dim = np.transpose(my_non_square_matrix_transposed) + my_non_square_matrix
print(f"Correct dims {correct_dim.shape} and size {correct_dim.size}")

# ... or transpose the matrix and assign it back to itself (or to a new variable - which is the safer approach)
my_non_square_matrix_fixed = my_non_square_matrix_transposed.transpose()
correct_dim = my_non_square_matrix_fixed + my_non_square_matrix

# The moral of this story is that there are lots of ways to create a numpy array that is NOT the dimensions you want OR
#   to have a bit of code that is working syntactically (is not generating an error) but is incorrect semantically.
# The best debugging tool for this is to just print out (or check in the debugger) the shape of the numpy array(s) at
#   each step. Don't assume that you have them correct.
