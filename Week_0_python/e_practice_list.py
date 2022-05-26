#!/usr/bin/env python3

# ------------------------------------------------------------------------------
# List creation/accessing/editing practice
#

# Practice: slicing, accessing, creating new list from old, enumerate (zip, optional)

# Goal: Create a new list that is the running average of three numbers
#  I.e., the first element will be 0.1 + 0.2 + 0.8
#        the last element will be 0.9 + 1.0 + 1.2
#  total: 4 elements, [0.3666666666666667, 0.6333333333333333, 0.9, 1.0333333333333332]
#  NOTE: You should do this with numpy/scipy in "real life" - this is just list practice

# Version 1: Use a for loop with an if statement to skip the first/last elements
#   Hint: you'll need enumerate to get the index
#   Modify the for loop to
#     a) use enumerate to produce an index 0, 1, etc
#     b) Add an if statement to see if this is the first or last element
#         - do NOT use i == 4  or i < 4
#           Compare to the length of the list so it will still work even if we add an element to the list
#          HINT lhs < i < rhs  works in python (yay!)
#     c) sum the previous, current, and next elements
my_list_numbers = [0.1, 0.2, 0.8, 0.9, 1.0, 1.2]  # Should be able to add more numbers to this list without breaking anything

my_list_averaged = []
for v in my_list_numbers:
    my_list_averaged.append(v)
print(f"Averaged list: {my_list_averaged}")

# Version 2: Change the above so that, instead of having an if statement to check for first and last elements,
#   you use slicing to iterate only over the 2nd-n-1 elements
#   NOTE: Fixing the indexing of enumerate - you can use an optional parameter to enumerate to start at 1 instead
#    of zero   eg. enumerate(my_list_numbers, start=1)
#    OR just make sure you adjust your i's and i+1 i-1 appropriately

# Version 3 (OPTIONAL): Do this with a zip and slicing instead of enumerate. Should look like
#    prev, cur, next = zip(l[stuff], l[stuff], l[stuff]) where stuff pulls out the
#        0..n-3 elements, then 1..n-2  then 2..n-1
#

# ------------------------------------------------------------------------------
# List of lists, sorting practice
# Sorting is really easy - but what about sorting two lists by one? (Think selecting two rows of a spread sheet and sorting by the first row.)

# Think of this as the header row of your csv file
my_header_list = ["a", "e", "b", "d", "c", "c"]
# Think of this as the second row of your csv file
my_values_list = [0.3, 1.2, 5.2, 6.2, 3.2, 3.5]

# Sort the values row by the header row - think of doing a spreadsheet sort where all the columns are sorted by the
#   first column:
# What the sorted my_values_list should look like
#  [0.3, 5.2, 3.2, 3.5, 6.2, 1.2]

# First try - sort my_header_list to be in alphabetical order
#   Copy over the list, since sorting edits in place
my_header_list_sorted = my_header_list.copy()
# Now sort it
# TODO: Sort my_header_list_sorted (Google sort on python lists)
print(f"Sorted: {my_header_list_sorted}")

# Problem - how do you sort the *second* list by the first list?
#  Python-esq answer: Make a new list that has both lists in it using zip, sort the result, then extract the
#    second list back out
#  For this, google the answer and see if you can make sense of the results using what you know of lists
#
# Step 1: Just get to the sorted list of lists
# Step 2: Extract out the second element of the sorted list from the list of lists

# A CAUTIONARY NOTE
# NOTE: Do NOT do something like this - it SEEMS like it will work - and it will - but only if there are no
#   duplicate elements... Also, it's really inefficient.
#      Count how many elements there are in the my_sort_second_list_wrong - why are there so many?
my_sort_second_list_wrong = []
for h in sorted(my_header_list):
    for i, orig_h in enumerate(my_header_list):
        if h is orig_h:
            my_sort_second_list_wrong.append(my_values_list[i])
print(f"Wrong answer: {my_sort_second_list_wrong}")
# END A CAUTIONARY NOTE

# ------------------ Answers -------------------

print("#" * 20 + " ANSWERS " + "#" * 20)
print("Version 1")
my_list_averaged = []
for i, v in enumerate(my_list_numbers):
    if 0 < i < len(my_list_numbers) - 1:  # Remember, indexing is 0..len - 1
        # Remember, v is my_list_numbers[i]
        val = (my_list_numbers[i-1] + v + my_list_numbers[i+1]) / 3
        my_list_averaged.append(val)
print(my_list_averaged)

print("Version 2")
my_list_averaged = []
for i, v in enumerate(my_list_numbers[1:-1], start=1):
    # You could also do enumerate(list) and then do [i] and [i+2]
    val = (my_list_numbers[i-1] + v + my_list_numbers[i+1]) / 3
    my_list_averaged.append(val)
print(my_list_averaged)

print("Version 3")
my_list_averaged = []
# Notice 2: to get up to the last element; -1 gets all but the last
for p, v, n in zip(my_list_numbers[0:-2], my_list_numbers[1:-1], my_list_numbers[2:]):
    # You could also do enumerate(list) and then do [i] and [i+2]
    val = (p + v + n) / 3
    my_list_averaged.append(val)
print(my_list_averaged)

# -------------------------------- Sorting answers -------------------
# Sorting returns a NEW list that is sorted
my_header_list_sorted.sort()   # Sorts the list in-place
print(f"Sorted: {my_header_list_sorted}")

# Step 1: Zip the two UNSORTED lists together, then sort
my_combined_lists = zip(my_header_list, my_values_list)
# Step 2: Sort - this will by default, sort by the first element then by the second
my_combined_lists_sorted = sorted(zip(my_header_list, my_values_list))
print(f"Sorted iterable {my_combined_lists_sorted}")
# Step 3: Extract out the second element of the sorted list from the list of lists
my_value_sorted = [hv[1] for hv in my_combined_lists_sorted]
print(f"Second list, sorted by first: {my_value_sorted}")

