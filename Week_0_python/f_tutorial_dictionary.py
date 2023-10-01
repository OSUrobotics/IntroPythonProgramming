#!/usr/bin/env python3

import numpy as np

# What are dictionaries?
#
# Dictionaries are values (pretty much any data structure/variable type you can think of) paired with keys (unique
#   identifiers). Common key types are integers and strings. The best mental image for dictionaries are: I have a bunch of
#   items that I can identify with a unique name. I want to be able to put them into the dictionary and get them back
#   out again quickly and efficiently.
#
# What you can do with a dictionary:
#   1) Check if an item is in the dictionary
#   2) Put an item in/take it out
#   3) Loop over all of the items (or the keys) - CAVEAT: Not guaranteed to be in the order you put them in...
#
# All of these operations are very fast - much faster than, say, searching through a list to see if an item is in the list

# There are two really common uses for dictionaries. The first is just as a way to store a collection of related data
#   with human-understandable names. The second use is as an "I've seen this, y/n" counting mechanism.
#
# For both of these examples we'll create the dictionaries from lists, since it's easier to make a self-contained
#   example that way. However, you should think of those "lists" as being data read in from a file, data created
#   by a function, etc
#
# BTW, The classical example use-case for dictionaries is storing student information using their student ID.
#
# Creating a dictionary: Like lists, you can create a dictionary "by hand", or by doing the equivalent of an append.

##################
# Example 1a: Store a collection of data, one dictionary, one data pile.
# Make-up some data
my_array_of_random_numbers = np.random.uniform(-5, 500, 20)

# The keys for this dictionary are the strings before the :, the values are the things on the right of the :
my_dict = {"Data": my_array_of_random_numbers,
           "Name": "Cool name",
           "Mean": np.mean(my_array_of_random_numbers),
           "Sum": np.sum(my_array_of_random_numbers),
           "Accessed": 0,
           "Date": "3/11/2022"}

# What does this look like if I print it out?
# Note that prints out pretty much with the same format you make it in
print(f"My dictionary:\n {my_dict}")

# We can add more items to the dictionary like this:
my_dict["Date analyzed"] = "4/11/2022"

# You can check if a key is in the dictionary like this
if "Sum" in my_dict:
    print(f"Sum is in the dictionary, value {my_dict['Sum']}")

# [For illustration purposes only - do not do this] Loop through all the keys and see if one of them is Sum
for k in my_dict.keys():
    if k == "Sum":
        print(f"Found sum, value {my_dict['Sum']}")

# And we can get out an element and edit it like this (add one to Accessed):
print(f"My dictionary, Accessed value before: {my_dict['Accessed']}")
my_dict["Accessed"] = my_dict["Accessed"] + 1
print(f" ... and after: {my_dict['Accessed']}")

##################
# Example 1b: Student record example
# Store the same data for a bunch of different companies. Using companies instead of student record, but same idea
# Two examples here, they do the same thing, just different ways to implement

# Make up some data
my_names = ["Amazon", "Google", "Meta", "Tiktoc"]
my_sales_figs = [1.1, 2.2, 1.3, 0.1]  # made up numbers
my_number_employees = [100, 20, 10, 1]

# Build a list with dictionary elements from those lists - version 1
my_company_list = [{} for _ in range(0, len(my_names))]  # Empty list of dictionaries
for i, n in enumerate(my_names):
    my_company_list[i]["name"] = n
    my_company_list[i]["sales"] = my_sales_figs[i]
    my_company_list[i]["employees"] = my_number_employees[i]

print("My company list, v1")
print(my_company_list)

# Build a list with dictionary elements from those lists - version 2
my_company_list_v2 = []  # Empty list
for i, n in enumerate(my_names):
    my_company_dict = {}  # Empty dictionary
    my_company_dict["name"] = n
    my_company_dict["sales"] = my_sales_figs[i]
    my_company_dict["employees"] = my_number_employees[i]

    # Add dictionary to list
    my_company_list_v2.append(my_company_dict)

print("My company list, v2")
print(my_company_list_v2)

# Now use that list to answer a question
print("Which companies have sales bigger than 1 and fewer than 25 employes?")
for company in my_company_list:
    if company["sales"] > 1 and company["employees"] < 25:
        print(f"{company['name']}")

####################################
# Example 2: Counting
#   Go through the list of random numbers and count how many of each number (rounded down) we have
#   Note that this is such a common thing to do that Python has a built-in way to do it - see
#     https://docs.python.org/3/library/collections.html

# Making an array of integer values - can't use floating points as keys
my_array_of_random_numbers = np.round(np.random.uniform(-5, 5, 20))
my_count_vals_dict = {}  # Empty dictionary

for n in my_array_of_random_numbers:
    if n in my_count_vals_dict:
        my_count_vals_dict[n] += 1   # Add one to the dictionary entry
    else:
        my_count_vals_dict[n] = 1    # Make the dictionary entry

# Print out the sums - notice k, v
for k, v in my_count_vals_dict.items():
    print(f"Key {k} showed up {v} times")

# [Optional: The python way]
my_count_vals_dict = {}  # Empty dictionary
for n in my_array_of_random_numbers:
    try:
        my_count_vals_dict[n] += 1   # Add one to the dictionary entry
    except KeyError:
        my_count_vals_dict[n] = 1    # Make the dictionary entry

for k, v in my_count_vals_dict.items():
    print(f"Key {k} showed up {v} times")

####################################
# Gotchas
#

# Gotcha 1: Key versus value in a for loop
#  Dictionaries have got keys AND values - you can loop over keys, values, or both together. The default
#   is to loop over keys, since you can always get the values out FROM the keys.
#  The usual gotcha is that you loop over keys and expect the values... Here are the three examples

# This is the default, but can't hurt to specify keys so you won't forget...
print("Default behavior")
for k in my_dict:
    print(f"From key {k} get the value {my_dict[k]}")

# ... letting the reader know that you are just getting keys
print("Loop through keys")
for k in my_dict.keys():
    print(f"From key {k} get the value {my_dict[k]}")

# If you just want the values and don't care about the keys
print("Loop through values")
for v in my_dict.values():
    print(f"Value only, can't get key: {v}")

# If you want both... - just remember which order these are returned in!
print("Loop through both")
for k, v in my_dict.items():
    print(f"Got key {k} and value {v}")

# Gotcha 2: Older versions of Python (pre 3.7)
#  In older versions of Python the dictionary was not guaranteed to be ordered, i.e., things might come out in a
#  different order than they went in... Look at the for loops above: If you are running a later version of
# Python the keys come out in the order we put them in: Data, Name, Mean, Sum, Accessed, Date, Date analzed.
# In older versions, this is not guaranteed unless you specifically ask for an ordered dictionary...

# Gotcha 3: Accessing a key value that isn't there
#   This throws the following error:
#     KeyError: 'sum'
# but it's usually confusing because you think it should be there, but it's not OR you're doing an access and
# not realizing it. EG, in this example "Sum" is the correct key, but I forgot to capitalize it. AND
#  doing a += 1 first accesses the key, then assigns it, even though it looks like an assignment
my_dict["sum"] += 1
