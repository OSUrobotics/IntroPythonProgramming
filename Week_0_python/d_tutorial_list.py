#!/usr/bin/env python3

import math

# What are lists?
#
# Lists are just ordered collections of anything. They mutable - the can be edited "in place".
#  Although lists can be treated as arrays (see numpy array) in fact they are a lot more flexible. Arrays
#   require that all the element types be the same, and if the array is n-dimensional (think matrix) then all the
#   rows have to have the same number of elements. This is NOT true for lists.
# Lists are primarily used to keep data that may be changing over time or of different types. Some common examples:
#  Keep the header/row names of the columns/rows of a spreadsheet
#  Keep the n parameter values you want to try in a function (think spring constant, joint angles, etc)
# In general, if you want to do something n times with n different values, put those values in a list and then
#  iterate over the list with a for loop
#
# The primary "gotcha" of lists is that variable names are pointers - assigning a = b does NOT copy the values of b into
#  a, a points to the exact same data as b did. So editing b will edit a and vice versa.
#
# There are many utilities/functions for iterating over, sorting and building lists.
# Related data structures:
#   strings - a list of characters, immutable
#   tuples - a list of anything (like a list), but immutable (you can't change it once it's built)
#   numpy arrays - n-dimensional arrays of numbers or booleans. Provides very, very fast interation/operations over
#     those arrays
#
# Use strings or tuples if you just build the list and don't edit it/change it
# Use numpy arrays if all your data is of the same type (number, boolean)
#
# Syntax: https://docs.python.org/3/tutorial/datastructures.html#
# Alternative tutorial: https://www.programiz.com/python-programming/list

# ------------------------------------------------------------------------------
# Creating lists
#   In general, [] is used to create a list AND access elements of it

# Use case: You know in advance what you want in the list (eg, parameters you want to try)
my_list_advance = ["A string", ["Another", "list", 3], 10.3, True]
print(my_list_advance)

# Use case: You are iterating over something and want to add the items in one at a time
#   Note that the for loop could be a lot more complicated, and include if statements
my_list_add = []  # Empty list
for i in range(10, 15):
    # Add in the string "item n"
    my_list_add.append("item " + str(i))
# Add in a "done", just for fun
my_list_add.append("done")
print(my_list_add)

# Fancy version, if you want to build the list in one line - requires being able to iterate over something
#   See list comprehension (that's the fancy name for this)
#  Iterates over the for loop, and puts the stuff on the left in the list
#    Identical to the above for loop, just in one line
my_list_fancy_add = ["item " + str(i) for i in range(10, 15)]
print(my_list_fancy_add)

# OPTIONAL - you can even do if statements
#  - in this case, if i is even, add the item
my_list_fancy_add_with_if = ["item " + str(i) for i in range(10, 15) if i % 2 == 0]
print(my_list_fancy_add_with_if)

# END OPTIONAL

# --------------------------------------------------
# Accessing elements of a list
#  - range is a generator function. To make it a list, we explicitly cast to a list
#    Could also use the [i for i in range(0,10)] syntax above
my_list_numbers = list(range(0, 10))
print(my_list_numbers)
print(f"First index: {my_list_numbers[0]}")   # Get one element out - note, index from 0
print(f"Last index: {my_list_numbers[-1]}")    # Get last element out - note -1
print(f"Slice index: {my_list_numbers[1:3]}")  # Get second, third - note does NOT include list[3]

# Looping over elements in the list
print("Starting loop")
for item in my_list_numbers:   # item will be each element in my_list_numbers in turn
    print(f"Item {item}")
print("Ending loop")

# Looping over some of the elements in the list (using slicing)
print("Starting loop")
for item in my_list_numbers[1:-1]:   # All but the first and last elements
    print(f"Item {item}")
print("Ending loop")

# Creating a new list from the old one
my_list_from_old = []
for item in my_list_numbers:
    # Create the element ["item n", n] (which is a list) and add it to the new list
    my_list_from_old.append([f"Item {item}", item])
print(my_list_from_old)

# OPTIONAL
# The following is a fairly complicated example that combines a for loop with an if statement and enumerate to
#   combine indexing with element access. There are two versions here; one that does this all in one line, the second
#   takes that single line apart and shows what it would look like in more traditional coding.

# You can return tuples from for loop iteration on lists to do indexing and values at the same time
#  - in this case, if i is even, add the item
my_list_fancy_add_with_if_and_enumerate = ["item " + str(i) + " is " + str(n) for i, n in enumerate(range(0, 5)) if i % 2 == 0]
print(my_list_fancy_add_with_if_and_enumerate)

# Taking this apart - this is the same code, just written in pieces
my_list_add_with_if_and_enumerate = []
# Build up to enumerate/range - you can print/look at each of these in the debugger
r = range(0, 5)  # Note: range is a generator function - not a list. It functions like a list, but doesn't actually make all the values
index_plus_r = enumerate(r)  # Enumerate is a generator as well
index_plus_r_as_list = list(index_plus_r)  # You can, however, cast to a list to see what it looks like
# index_plus_r[0] - this does NOT work, because index_plus_r is a generator, not a list
tuple_return = index_plus_r_as_list[0]  # See what one element looks like - see tuples tutorials
my_list_add_with_if_and_enumerate = []
for i, n in enumerate(range(0, 5)):
    i_str = str(i)
    n_str = str(n)
    make_str = "item " + i_str + " is " + n_str
    if i % 2 == 0:
        my_list_add_with_if_and_enumerate.append(make_str)

print(my_list_add_with_if_and_enumerate)

# END OPTIONAL

# ---------------------------------------------------
# Getting indices of elements
# Task: Suppose you have three lists, one with strings for what you want to do, and two with numbers. You want to do
#   something different depending on what is in the first list - eg, add instead of multiply. The output is a list
#   with the results (but only if the first list says to).

#  Here are multiple ways to do this, getting steadily more sophisticated.
my_list_todos = ["add", "add", "multiply", "skip", "multiply"]
my_list_lhs_numbers = [1, 2, 3, -10, 4]
my_list_rhs_numbers = [0.1, 0.2, -0.3, 0.4, 0.5]

# Old-school, matlab or C++ version
#  Declare an index variable and use the length of the list to iterate over
#   range produces the numbers 0, 1, etc through n-1
#   for the c programmer, there is no for (i = 0, i < n, i++) equivalent
my_list_result = []
for i in range(0, len(my_list_todos)):
    if my_list_todos[i] is "add":
        my_list_result.append(my_list_lhs_numbers[i] + my_list_rhs_numbers[i])
    elif my_list_todos[i] is "multiply":
        my_list_result.append(my_list_lhs_numbers[i] * my_list_rhs_numbers[i])
    elif my_list_todos[i] is "skip":
        pass  # This is the RIGHT way to do this, so you catch if someone mis-typed something
    else:
        raise ValueError(f"Expected add, multiply, or skip, got {my_list_names[i]}")
print(my_list_result)

# Do NOT do the following. It is prone to errors (forgetting to increment i) and is just UGLY
i = 0
for n in my_list_todos:
    lhs = my_list_lhs_numbers[i]
    rhs = my_list_rhs_numbers[i]
    print(f"stuff in for loop {i} {n} {lhs} {rhs}")
    i = i + 1

# Better: Use python's enumerate function to get i (enumerate is AWESOME)
#   i will have 0, 1, etc, while n will take on each element of the list in turn
#   Note that, technically, enumerate is returning a tuple with two elements i and n
my_list_result = []  # Set list back to empty
for i, n in enumerate(my_list_todos):
    if n is "add":
        my_list_result.append(my_list_lhs_numbers[i] + my_list_rhs_numbers[i])
    elif n is "multiply":
        my_list_result.append(my_list_lhs_numbers[i] * my_list_rhs_numbers[i])
    elif n is "skip":
        pass  # This is the RIGHT way to do this, so you catch if someone mis-typed something
    else:
        raise ValueError(f"Expected add, multiply, or skip, got {n}")
print(my_list_result)

# Best: Use python's zip function to do all the work for you (look ma, no i!)
#  Note that zip is returning a tuple with the ith element from each list each iteration
#  Note also that this does NOT require an index variable i - it's all handled for you
my_list_result = []  # Set list back to empty
for n, lhs, rhs in zip(my_list_todos, my_list_lhs_numbers, my_list_rhs_numbers):
    if n is "add":
        my_list_result.append(lhs + rhs)
    elif n is "multiply":
        my_list_result.append(lhs * rhs)
    elif n is "skip":
        pass  # This is the RIGHT way to do this, so you catch if someone mis-typed something
    else:
        raise ValueError(f"Expected add, multiply, or skip, got {n}")
print(my_list_result)

# ---------------------------------------------------
# extend - gluing together two lists
# Again, we'll give you two ways to do this, the not so pretty one then the nice one
# Followed by  two examples that are not technically mistakes, but probably aren't what you want
my_list_part_1 = ["a", "list", "part", "1"]
my_list_part_2 = ["part", "2"]

# old school way of adding list 2 to list 1; this works, but it's clunky and slow
for elem in my_list_part_2:
    my_list_part_1.append(elem)
print(my_list_part_1)

# Far simpler is to use extend
my_list_part_1 = ["a", "list", "part", "1"]
my_list_part_1.extend(my_list_part_2)
print(my_list_part_1)

# ERROR: This does NOT work the way you intend - syntactically correct, but it just adds the entire list as the
#  next element.
# Why is my list not a list?
my_list_part_1 = ["a", "list", "part", "1"]
my_list_part_2 = ["part", "2"]
my_list_part_1.append(my_list_part_2)
print(my_list_part_1)
print(f"Length of list {len(my_list_part_1)}, should be 6")

# I've also seen people do this, which is a list of lists with single elements
#   This creates a list with one element in it then appends the element
my_list_part_1 = ["a", "list", "part", "1"]
my_list_part_2 = ["part", "2"]
for elem in my_list_part_2:
    my_list_part_1.append([elem])
print(my_list_part_1)

# Typical indexing errors
#  error message: IndexError: list index out of range
# UNCOMMENT
# my_list_part_1[50]  # Not 50 elements
n = 10.0
#  error message: TypeError: list indices must be integers or slices, not float
# UNCOMMENT
# my_list_part_1[n]  # n is not an integer

# Not really an error, but if you meant to include the last number THIS WON'T work
#   Use [1:] to include the last element
#   Use [0:1] to get just the first element
for n in my_list_todos[1:-1]:
    print(n)
# END ERROR

# ERROR: List variables point to THE SAME THING
my_list_todos_2 = my_list_todos

# fine if you're just accessing
print(f"List names {my_list_todos}")
print(f"List names 2 {my_list_todos_2}")

# If we edit either one, we edit the other
my_list_todos.append("Oops")
print(f"List names {my_list_todos}")
print(f"List names 2 {my_list_todos_2}")

# This is particularly problematic - because it will never stop. (Hit control c)
#   It keeps adding n oops to my_list names
# UNCOMMENT
# for n in my_list_todos:
#     my_list_todos_2.append(n + "oops")

# How to detect these problems
#   Lists change number of elements when you don't expect them to (leading to indexing errors)
#   The values in your list change when you don't think you changed them
#   Look for l1 = l2 OR when you've passed a list into a function
#     Note that in python it's really, really bad form to change a list inside a function - but that doesn't stop people
# How to avoid generating this error
#    Always create a new list and do an append to "change" the original list
#    Avoid re-using variable names
my_list_no_problem = []
for n in my_list_todos:
    my_list_no_problem.append(n)
# END ERROR

# ERROR: Don't edit lists in place
#  Ok, this isn't technically an error, just dangerous/bad coding practice
l_orig = [3.0, 5.0, -1.0, 6.0, -2.0, 5.0]
# Code to fix negative numbers
for i, v in enumerate(l_orig):
    if v < 0:
        l_orig[i] = 0.0
    # Hidden else - l_orig stays the same

# CORRECT way to do this
l_orig = [3.0, 5.0, -1.0, 6.0, -2.0, 5.0]
l_orig_fixed = []
for v in l_orig:
    if v < 0:
        l_orig_fixed.append(0.0)
    elif v is math.nan:
        l_orig_fixed.append(0.0)
    else:
        l_orig_fixed.append(v)

# OPTIONAL: Same holds true for using a function to do the same thing
def bad_programmer(l_orig):
    for i, v in enumerate(l_orig):
        if v < 0:
            l_orig[i] = 0.0
        elif v is math.nan:
            l_orig[i] = 0.0
    return l_orig

# Just... don't do this. Not only does this edit l_orig in place, but it's hidden behavior - how do you, as someone
#  using bad_programmer(), suppose to know that l_orig will be edited? And that l_orig is the same as l_orig_fixed?
l_orig = [3.0, 5.0, -1.0, 6.0, -2.0, 5.0]
l_orig_fixed = bad_programmer(l_orig)
print("These are the SAME list")
print(l_orig)
print(l_orig_fixed)

def good_programmer(l_orig):
    l_orig_fixed = []
    for v in l_orig:
        if v < 0:
            l_orig_fixed.append(0.0)
        elif v is math.nan:
            l_orig_fixed.append(0.0)
        else:
            l_orig_fixed.append(v)
    return l_orig_fixed
l_orig = [3.0, 5.0, -1.0, 6.0, 0.0 / 0.0, 5.0]
l_orig_fixed = good_programmer(l_orig)
print("These are the NOT the same list")
print(l_orig)
print(l_orig_fixed)

# END OPTIONAL
# END ERROR
