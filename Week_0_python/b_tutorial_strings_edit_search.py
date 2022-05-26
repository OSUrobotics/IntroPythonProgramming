#!/usr/bin/env python3

# ------------------------------------------------------------------------------
# Editing strings - sometimes you have to take a string and edit it. Strings are IMMUTABLE - that means, you can't
#  edit them in place. So all editing looks like copying over the pieces you want to keep.
# There are a TON of existing routines for editing and searching and taking apart strings.
#   Upper/lower case, is it a letter, number or a white space, take out special characters
#   Find a character or a substring in a string, does the string contain these characters?
#   Split up a string into a list of strings
# See https://docs.python.org/2.5/lib/string-methods.html

# Upper to lower case
my_string_upper_case = "SOUNDS LIKE I'M YELLING!"

# convert to lower case - lower makes a copy of the string, converts it, then returns the copy
my_string_lower_case = my_string_upper_case.lower()
print(f"This is yelling: {my_string_upper_case}, this is not: {my_string_lower_case}")

# Oops, should capitalize first letter:
my_string_cap = my_string_lower_case.capitalize()
print(my_string_cap)

# ... and replace the lower-case i with an upper case
my_string_with_i_fixed = my_string_cap.replace("i'm", "I'm")
print(my_string_with_i_fixed)

# add in the "not" by finding the last space
index_last_space = my_string_with_i_fixed.rfind(" ")
# List indexing to get out the left and right half
#   0:index gets 0, through index -1
#   index: gets from index through end
my_not_yelling_string = my_string_with_i_fixed[0:index_last_space] + " not" + my_string_with_i_fixed[index_last_space:]
print(my_not_yelling_string)

# ... without the ! at the end - use :-1 to only copy up to the last element
my_not_yelling_string_better = my_string_with_i_fixed[0:index_last_space] + " not" + my_string_with_i_fixed[index_last_space:-1]
print(my_not_yelling_string_better)

# ERRORS
# You can't directly edit a string. You'll get a very confusing error message that says
#   TypeError: 'str' object does not support item assignment
# Translate that as: You can't assign to an individual character in a string
# UNCOMMENT
# my_not_yelling_string[1] = 's'

# END ERRORS

# ------------------------------------------------------------------------------
# Splitting up strings
# Often when you read in strings from files (or people type in strings) you'll get strings that you have to "split up",
#  for example, by getting all the numbers separated by commas OR ignoring a descriptor at the beginning
# For these examples we'll have strings "typed in" (rather than reading them from a file) just to keep things simple.
# In reality, you usually have to do this when you can't edit the files directly.

#-----------------------------
# Split example

# Make a list of numbers
list_of_numbers = [0.3 + 0.1 * n for n in range(0, 10)]
# Put a random number in the middle
list_of_numbers.insert(3, "3.3e-3")

# Turn it into a string with a tab at the beginning (the \t)
str_list_of_numbers = "\t" + ", ".join(["{:.2}"] * len(list_of_numbers)).format(*list_of_numbers)
print(str_list_of_numbers)

# Take it back apart again using split - note that split is smart enough to take out ALL white space
my_list_back_as_strs = str_list_of_numbers.split(',')

# Convert back to a list of numbers
recover_list = [float(item) for item in my_list_back_as_strs]
print(recover_list)

# if that is confusing to you, this is the same code
recover_list = []
for item in my_list_back_as_strs:
    recover_list.append(float(item))

#-----------------------------
# Find example
# We have a list of strings, which consist of a descriptive name followed by a colon followed by a number
#  Find the end of the line (the \n) then split up each line.
#  If the line has a : then get out the number, otherwise, ignore it
#  Note that there is a more complete example of this (for building a dictionary) in the dictionary tutorial
my_str_to_parse = "# This is a header\nItem 1: 0.3\nBlank line\nItem 2: 1.3\n"

# First, split the line into strings separated by \n
my_lines = my_str_to_parse.split('\n')

# An empty list of numbers
my_numbers = []
# Now loop through each line and look for a colon
for l in my_lines:
    # You can use this notation to see if the string ":" is in the string "l"
    if ":" in l:
        # split again - you could also use find and the resulting index
        two_parts = l.split(":")
        # Don't forget to convert the string to the number
        the_number = float(two_parts[-1])
        my_numbers.append(the_number)
print(my_numbers)

#-----------------------------
# Editing file name(s)
# This is pretty common - take the last 4 characters off and replace them with a different file type
file_name_orig = "my_file.txt"
file_name_new = file_name_orig[0:-4] + ".csv"
print(file_name_new)


