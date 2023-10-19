#!/usr/bin/env python3

# --------------------------- Create a function -------------------------
#
# Create a function that takes in a list, an element to search for, and an (optional) element to replace
#  that element. If that optional replacement is "none", then simply remove that element. This function
#  should create a new list and return that (do NOT edit the original list)
#
#  There are many, many ways to do this - I'll walk you through one. See here https://datagy.io/python-replace-item-in-list/
#   for more ways if you're curious.

# Specific instructions:
#  1) Name your function your_list_replace
#  2) First parameter should be the input list
#  3) Second parameter is the element to find
#  4) Third parameter is what to replace that element with. It should default to None
#  5) Do NOT edit the input list - you should create a new list and return that

# The craziness of Python - you can pass functions into functions and then run them! I wanted a way to test my own
#  version of the function as well as yours, so I wrote a function that will do that
def check_list_replace(func_to_check):
    """Check that the function correctly replaces values
    @param func_to_check - function to check (either my_list_replace or your_list_replace)
    @returns True if no errors found"""

    list_to_check1 = ["a", "b", "c", "d", "a"]
    save_list_to_check1 = ["a", "b", "c", "d", "a"]
    expected_return1 = [1, "b", "c", "d", 1]
    expected_return2 = ["b", "c", "d"]

    # First check that it works with replacing "a" with 1
    ret1 = func_to_check(list_to_check1, "a", 1)
    if not (list_to_check1 == save_list_to_check1):
        print(f"You modified the original list {list_to_check1}, {save_list_to_check1}")
        return False

    if not (ret1 == expected_return1):
        print(f"Return incorrect, expected {expected_return1}, got {ret1}")
        return False

    ret2 = func_to_check(list_to_check1, "a")
    if not (list_to_check1 == save_list_to_check1):
        print(f"You modified the original list {list_to_check1}, {save_list_to_check1}")
        return False

    if not (ret2 == expected_return2):
        print(f"Return incorrect, expected {expected_return2}, got {ret2}")
        return False

    return True


# ----------------------------- answers ----------------------------------
# I've used in_list and ret_list to be as clear as possible which one is the input and which is the returned one
#
def my_list_replace(in_list, elem_find, elem_replace=None):
    """Replace elem_find with elem_replace, removing it if elem_replace is none
    @param in_list - the input list
    @param elem_find - the element to find. Assumes in_list[i] == elem_find returns True
    @param elem_replace - what to set the element to; if None, delete the element
    @return returns a new list with the replaced element"""

    # This is an example of create a new list, and append the element to that list
    ret_list = []

    # What type of for loop to use - Do we need an index? No, because we're using .append to add the new
    #  element. So just a standard for e in list  will work just fine
    for e in in_list:
        # Use ==, not is, because it will work across more data types
        if e == elem_find:
            # Check if the replacement element is NOT none - if so, append the replacement element
            if elem_replace is not None:
                ret_list.append(elem_replace)
        else:
            # Just copy the element over
            ret_list.append(e)

    # Return the list
    return ret_list


if __name__ == '__main__':
    # Check that it works
    list_to_check1 = ["a", "b", "c", "d", "a"]

    # First check that it works with replacing "a" with 1
    #ret1 = your_list_replace(list_to_check1, "a", 1)
    ret1 = my_list_replace(list_to_check1, "a", 1)

    # Use this line to check your own function
    # if check_list_replace(your_list_replace):
    if check_list_replace(my_list_replace):
        print("Passed checks")
