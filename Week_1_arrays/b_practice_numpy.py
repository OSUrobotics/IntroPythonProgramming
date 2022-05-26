#!/usr/bin/env python3


# Anything numpy-ish will start with np.
import numpy as np

# This is a handful of low-level numpy tasks that are, well, silly, but will give you practice with creating, editing
#   and accessing numpy arrays.

# -------------------------- Creating numpy arrays -------------------------
# Create a 1x10 array of numbers that starts at 0, goes to 1, and is evenly spaced (linspace)
my_linspace_array = None

# Create a new array from the previous one by multiplying by 2 and adding 1 (NO for loops allowed)
...

# Create a 2x10 numpy array with the two arrays as the first and second row
#   There are two ways to do this; create a blank array using zeros and assign the two rows to those arrays OR
#   use one of numpy's functions to concatenate array methods (google numpy concatenate array and look both at
#   concatenate and look for a method that is specifically designed to stack two arrays vertically...)
# NOTE: Make sure this works even if you change the number of elements in the linspace array...
# Common error 1 - forgetting the []
#   my_new_matrix_from_zeros = np.zeros(2, my_linspace_array.size)
# Common error 2 - forgetting the :
my_new_matrix = None

print(f"My matrix shape: {my_new_matrix.shape}, should be (2, size of linspace array)")

# Now do the same thing again, but add padding by making the first column -1 and the last column 2
#   I.e, the new numpy array should be 2 x (size of linspace array + 2)
my_new_padded_matrix = None

print(f"My matrix shape: {my_new_padded_matrix.shape}, should be (2, size of linspace array + 2)")
print(f"First column is: {my_new_padded_matrix[:, 0]}, should be [-1. -1.]")
print(f"Last column is: {my_new_padded_matrix[:, -1]}, should be [2. 2.]")

# Now go back and make the original linspace array size 20 and see if it all still works
print(f"Size of my_new_matrix should be 2, 20, is {my_new_matrix.shape}")

# -------------------------- min, max, etc on numpy arrays -----------

# Calculate the mean, min, and max of the linspace array
#  Answers are in the current print out
# Change to printing out the answers using numpy mean, min, max
print(f"From array: Mean: {0.5}, min: {0.0}, max: {1.0}")

# Calculate the mean of each row of the matrix (without padding)
#   Make sure this works no matter how many rows the matrix has...
# There are two ways to do this; the first is to manually loop over the rows, calculate the mean, and assign it
#   to the my_means array.
# The second is to use np.mean parameters to tell numpy to calculate the mean for each row (should return a num rows x 1
#   array)
my_means = None
print(f"My means: {my_means}, should be a 2x1 array, with 0.5, 2 in it (10 elements in linspace array)")

# -------------------------- Boolean indexing on arrays -----------
#  In the padded matrix set all of the values that are bigger than 1 to be -1
#   Check: The max should now be 1
my_clipped_matrix = None
# Now count how many values in the clipped matrix are -1
#  Can use np.sum OR np.count_nonzero - the latter is somewhat faster
count_minus_1 = 0

print(f"Count: {count_minus_1}, should be 13 if linspace array size 10, 23 if linspace array size is 20")

# Now count how many are between 0.1 and 0.5 (Note: () & () is how to combine two conditionals)
#  If you get the following error:
#    TypeError: ufunc 'bitwise_and' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
#  See the solutions below - you need parenthesis around the individual conditionals
count_between = 0
print(f"Count between: {count_between}, should be 4 if linspace array size 10, 8 if linspace array size is 20")

# ------------------- Answers -----------------------------
# Create a 1x10 array of numbers that starts at 0, goes to 1, and is evenly spaced (linspace)

# You don't have to do the num=20 - it's just a good idea to make sure you don't accidentally set a bounds to 20 instead
#   of the number of elements
my_linspace_array = np.linspace(0, 1, num=20)

# Create a new array from the previous one by multiplying by 2 and adding 1
#   Look, ma, no for loops! You should NOT use a for loop here
my_new_array = my_linspace_array * 2.0 + 1.0

# Create a 2x10 numpy array with the two arrays as the first and second row
#   There are two ways to do this; create a blank array using zeros and assign the two rows to those arrays OR
#   use one of numpy's functions to concatenate array methods (google numpy concatenate array and look both at
#   concatenate and look for a method that is specifically designed to stack two arrays vertically...)
# NOTE: Make sure this works even if you change the number of elements in the linspace array...
# Common error 1 - forgetting the []
#   my_new_matrix_from_zeros = np.zeros(2, my_linspace_array.size)
# Common error 2 - forgetting the :
my_new_matrix_from_zeros = np.zeros([2, my_linspace_array.size])
# This works, although really it shouldn't:
my_new_matrix_from_zeros[0] = my_linspace_array
my_new_matrix_from_zeros[1] = my_new_array
# This is cleaner/clearer
my_new_matrix_from_zeros[0, :] = my_linspace_array
my_new_matrix_from_zeros[1, :] = my_new_array

# Creating a matrix from concatenate
my_new_matrix_from_concat = np.vstack([my_linspace_array, my_new_array])

print(f"My matrix shape: {my_new_matrix_from_zeros.shape}, should be (2, size of linspace array)")

# Now do the same thing again, but add padding by making the first column -1 and the last column 2
#   I.e, the new numpy array should be 2 x (size of linspace array + 2)
my_new_padded_matrix_from_zeros = np.zeros([2, 2 + my_linspace_array.size])
# This works, although really it shouldn't:
my_new_padded_matrix_from_zeros[0, 1:-1] = my_linspace_array
my_new_padded_matrix_from_zeros[1, 1:-1] = my_new_array

my_new_padded_matrix_from_zeros[:, 0] = -1
my_new_padded_matrix_from_zeros[:, -1] = 2

print(f"My matrix shape: {my_new_padded_matrix_from_zeros.shape}, should be (2, size of linspace array + 2)")
print(f"First column is: {my_new_padded_matrix_from_zeros[:, 0]}, should be [-1. -1.]")
print(f"Last column is: {my_new_padded_matrix_from_zeros[:, -1]}, should be [2. 2.]")

# Now go back and make the original linspace array size 20 and see if it all still works
print(f"Size of my_new_matrix should be 2, 20, is {my_new_matrix_from_zeros.shape}")

# -------------------------- min, max, etc on numpy arrays -----------

# Calculate the mean, min, and max of the linspace array
#  Answers are in the current print out
print(f"Answers: Mean: {np.mean(my_linspace_array)}, min: {np.min(my_linspace_array)}, max: {np.max(my_linspace_array)}")
# Change to printing out the answers using numpy mean, min, max
print(f"From array: Mean: {0.5}, min: {0.0}, max: {1.0}")

# Version 1 - make the array to put the values in first - note .shape[0] returns the number of rows
my_means = np.zeros([my_new_matrix_from_zeros.shape[0], 1])
for r in range(0, my_new_matrix_from_zeros.shape[0]):
    my_means[r] = np.mean(my_new_matrix_from_zeros[r, :])
print(f"My means v1: {my_means}")

# Fancy vesion - by setting axis = 0 I'm telling numpy to calculate the mean over the first axis (rows)
my_means_simple = np.mean(my_new_matrix_from_zeros, axis=0)
print(f"My means v2: {my_means_simple}")

# -------------------------- Boolean indexing on arrays -----------
#  In the padded matrix set all of the values that are bigger than 1 to be -1
#   Check: The max should now be 1
my_clipped_matrix = my_new_padded_matrix_from_zeros
# my_clipped_matrix returns an array of booleans of the same size as my_clipped_matrix
#   the = tells python to do a for loop over all values in my_clipped_matrix, and wherever that boolean array
#   is true, do the assigment to -1
my_clipped_matrix[my_clipped_matrix > 1] = -1
print(f"Max value in clipped matrix: {np.max(my_clipped_matrix)}")

# Now count how many values in the clipped matrix are -1
#  Can use np.sum OR np.count_nonzero - the latter is somewhat faster
#    Again, my_clipped_matrix == -1 returns an array that is True whenever the value is exactly -1
#    True == 1, False == 0, which is why sum works
count_minus_1 = np.sum(my_clipped_matrix == -1)
#  But this is better - directly looks for True/False
count_minus_1_v2 = np.count_nonzero(my_clipped_matrix == -1)

print(f"Count: {count_minus_1}, should be 13 if linspace array size 10, 23 if linspace array size is 20")

# Doing this in pieces so you can see how it works - all of the b_* variables are matrices that are of the
#   same size as my_clipped_matrix, with True/False set
# & is bit-wise and - same as and, but works on Boolean variables
b_array_1 = my_clipped_matrix > 0.1
b_array_2 = my_clipped_matrix < 0.5
b_combined_array = b_array_1 & b_array_2
# This, again, just counts the number of True values
count_between_v1 = np.count_nonzero(b_combined_array)
# Notice parenthesis to make sure it does the two comparisons before the &
#  - if you don't have those in there it tries to do the & first
count_between_v2 = np.count_nonzero((my_clipped_matrix > 0.1) & (my_clipped_matrix < 0.5))
print(f"Count between: {count_between_v1}, should be 4 if linspace array size 10, 8 if linspace array size is 20")
