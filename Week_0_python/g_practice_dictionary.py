#!/usr/bin/env python3

import numpy as np

# ------------------------------------------------------------------------------
# Dictionary creation/accessing/editing practice
#

######## Dictionary as data storage
# One common use for dictionaries is to store related data; in this example, suppose you have a function that does
#   a lot of fancy statistical calculations on a numpy array. Rather than return each of those numbers in a
#   list or tuple, put them in a dictionary with a reasonable name. That way, you don't have to try to figure out
#   which element in the list belongs to which statistical element.
def make_stats_dict(in_list):
    """ Calculate some statistics on the list and store the values in a dictionary
    @param in_list - a numpy array
    @return dict_stats - a dictionary with various statistical values stored in it"""
    my_dict = {}

    # Do some stats calculations, store in dictionary
    return my_dict

# Now use the function
my_array_of_random_numbers = np.random.uniform(-5, 500, 20)
my_dict = make_stats_dict(my_array_of_random_numbers)

# Print out the values calculated in make_stats (use a for loop to print out all of them, don't hard-wire the answers)
print()

######### Dictionary to count number of characters
# Create a single dictionary that has in it each letter and the number of times that letter appears in any of the strings
a_list_of_strings = ["Hello world", "Cat got your tongue?", "The merry fox jumped over the I forget"]
my_count_char_dict = {}
for s in a_list_of_strings:
    for c in s:
        ... # Add character to dictionary, or increment count

print(my_count_char_dict)

# Tweak number 1: Change the above code to create one dictionary for each string
my_count_char_list_of_dict = []
for s in a_list_of_strings:
    # Make a new dictionary
    for c in s:
        ... # Add character to dictionary, or increment count
    # Add dictionary to list

# Tweak number 2: Use the dictionaries to find which string has the letter "C" in it
for d in my_count_char_list_of_dict:
    # See if C in dictionary
    ...

# ------------------ Answers -------------------

################ Example 1
print("#" * 20 + " ANSWERS Example make dict " + "#" * 20)
def make_stats_dict(in_list):
    """ Calculate some statistics on the list and store the values in a dictionary
    @param in_list - a numpy array
    @return dict_stats - a dictionary with various statistical values stored in it"""
    my_dict = {}
    my_dict["Sum"] = np.sum(in_list)
    my_dict["Min"] = np.min(in_list)
    my_dict["Mean"] = np.mean(in_list)

    # Do some stats calculations, store in dictionary
    return my_dict

# Now use the function
my_array_of_random_numbers = np.random.uniform(-5, 500, 20)
my_dict = make_stats_dict(my_array_of_random_numbers)
for k, v in my_dict.items():
    print(f"Stat type {k} has value {v}")

################ Example 2
print("#" * 20 + " ANSWERS Count chars" + "#" * 20)
a_list_of_strings = ["Hello world", "Cat got your tongue?", "The merry fox jumped over the I forget"]
my_count_char_dict = {}
for s in a_list_of_strings:
    for c in s:
        # Add character to dictionary, or increment count
        if c in my_count_char_dict:
            my_count_char_dict[c] += 1
        else:
            my_count_char_dict[c] = 1
print("Character counts:")
print(my_count_char_dict)

# Tweak number 1: Change the above code to create one dictionary for each string
my_count_char_list_of_dict = []
for s in a_list_of_strings:
    # Make a new dictionary
    my_str_dict = {}
    for c in s:
        # Add character to dictionary, or increment count
        if c in my_str_dict:
            my_str_dict[c] += 1
        else:
            my_str_dict[c] = 1
    # Add dictionary to list
    my_count_char_list_of_dict.append(my_str_dict)

print("Character counts by string:")
print(my_count_char_list_of_dict)

# Tweak number 2: Use the dictionaries to find which string has the letter "C" in it
for i, d in enumerate(my_count_char_list_of_dict):
    # See if C in dictionary
    if "C" in d:
        print(f"Found C in string {a_list_of_strings[i]}")
