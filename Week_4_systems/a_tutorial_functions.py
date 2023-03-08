#!/usr/bin/env python3

import numpy as np

# --------------------------- Functions -------------------------
# First concept: All of the data/variables/inputs are passed INTO the function. You can create as many variables
#   in the function as you want, but only the values/data in the return statement are returned to the calling
#   function
# Implications:
#   When you are designing your function you should mentally (or on paper) write down
#      Input: What data do you need?
#      Output: What data are you going to return:
#      Body of function: How is the output related to the input?
#          Mathematical function
#          Data manipulation (eg, reorganize the data into a dictionary, sort it, etc)
#          Classification/Decision making (eg, does the data contain a zero? How many 1's in the data, etc)
#   Practical: Scoping. The variables IN the function are not the same as the variables OUTSIDE the function -
#      even if they have the same name. One way to think about it is that every variable in the function is
#      actually called func_name.a, not a - and every variable outside the function is called global.a, not a.
#      This isn't quite true, but it's pretty close

# First try it and see: input --- output, scope of variables in a function versus not
def func_calc_min_max(data):
    """ Return the min and max of the data array
    @param data - a numpy array with some numbers in it
    @returns min_value, max_value of the numpy array"""
    min_value = np.min(data)
    max_value = np.max(data)

    # TODO: Uncomment the following line. What error does this generate, and why? Where is it generated?
    #   Hint: where is my_data defined?
    # m_v = np.min(my_data)
    return min_value, max_value

# Calling function - note that it's really a terrible idea to have code like this at the "top"/global level, but
#   I'm trying to keep things simple
my_data = np.random.uniform(-0.2, 0.6, (100, 2))  # Generate some random numbers between -0.2 and 0.6

out_min, out_max = func_calc_min_max(my_data)
# TODO: Uncomment the following line. What error does this generate, and why?
#   Hint: What happens to variables in func_calc_min_max when the function exits?
# print(f"Min value {min_value}, max_value {max_value}")

# This doesn't generate an error. What happened to the min/max return value? See hint above
func_calc_min_max(my_data)

# Parameter passing
#   Python's input paramter specification and parameter passing is very sophisticated. One of the best things about
# Python is that you can directly assign variables to parameters by name. Side-stepping all of the fancy things
#  you can do, I'd recommend the following two rules:
# If the function only has one parameter, just pass it in (see example above)
# If the function has more than one parameter, use pass by name.
# Why: One of the most common (and sometimes difficult) to debug problems is that you *thought* you were passing zero
#   to the x parameter, but you actually sent it to the y one..

# Next try it and see, parameter ordering
def func_lots_of_params(a, b, c):
    """ Function with three parameters
    @param a - should be a string
    @param b - should be a list
    @param c - should be a dictionary
    @return None - no return value"""

    print("a should be a string: convert to upper case " + a.upper())

    print(f"b has {len(b)} elements")
    for i, b_elem in enumerate(b):
        print(f"{i}th element of b is {b_elem}, should be {b[i]}")

    for k, v in c.items():
        print(f"key {k} has value {v}")
    return None

a_string = "Hello, I'm a string"
b_list = [3.0, "hi", 10.0]
c_dict = {"key 1":"value 1", "Key 2":0.3}

# This one works and does what you expect (prints out the values of the variables)
func_lots_of_params(a_string, b_list, c_dict)

# TODO: Uncomment this one and see what error is generated. Can you predict what error will be generated?
#   Hint: does a list have an "upper" method like a string does?
#func_lots_of_params(b_list, a_string, c_dict)

# To prevent this problem you can use pass by parameter name - note that the parameters do NOT need to be in the
# correct order! (Although you probably do want to keep the order the same, anyways...)
# TODO: Try rearranging the paramter order. What happens if you take out one of the a=?
func_lots_of_params(a=a_string, c=c_dict, b=b_list)

# You don't have to set the parameters to variables, either, you can just set them to values:
func_lots_of_params(a="mystring", b=[0.2, 0.3], c={"as":0.2, "bs":0.3})

# Pass by value versus pass by reference
# This is a technical term related to the discussion in week 1 about immutable (strings, numbers) variable types
#  versus mutable (lists, dictionaries, numpy arrays). Strings and numbers just have their values copied over,
#  lists etc just have a reference to the data passed in - so if you change the value in the function, it changes it
#  in the calling function. This is Bad. Just Bad, and very difficult to debug. In general, just Don't change
#  the input variable values inside of the function.

def func_bad_bad_programmer(a_list, a_value=3.0):
    """ Edit the numpy array in place by multiplying by the given value
    @param a_array - a numpy array
    @param a_value - a value to multiply by
    @return The multiplied array"""
    for i, a in enumerate(a_list):
        a_list[i] *= a_value  # multiply and assign back to same variable
    return a_list

a_array_in = [-0.1, 0.2, 0.3]
print(f"a_array_in before function call {a_array_in}")
b_array_out = func_bad_bad_programmer(a_array_in, 3.0)
print(f"a_array_in after function call {a_array_in}")
# b_array_out is actually the same as a_array_in
b_array_out.append(2.0)
print(f"a_array_in after editing b {a_array_in}")

# TODO: Fix func_bad_bad_programmer by making a new list and putting the a_list[i] * a_value values in that new list

# Global variables and breaking function encapsulation
#  Also known as: Why I dislike Jupyter Notebooks and writing code like this

# It can be really tempting to use global variables rather than passing values in as parameters.
#  Saves typing, but will almost always lead to debugging headaches
a_global_variable = 3.0

def func_bad_use_global_variable(a_np_array):
    """ Multiply the numpy array by the global variable
    @param a_np_array - a numpy array
    @return a numpy array"""
    print(f"Global variable {a_global_variable}")
    return a_np_array * a_global_variable

a_np_array = np.linspace(0, 1, 6)
b_output_array = func_bad_use_global_variable(a_np_array)
print(f"Does what is expected {b_output_array}")
a_global_variable = 10

# TODO: Understand why this call returns different values than the first one
b_output_array_bad = func_bad_use_global_variable(a_np_array)
print(f"Oops: new output array {b_output_array_bad}")

def func_really_bad_use_global_variable():
    a_global_variable = 5.0

# TODO [optional]: Why does this multiply by 10 and not by 5? Didn't I set a_global_variable to 5?
#  Hint: Is a_global_variable in func_really_bad_use_global_variable the same one as in func_bad_use_global_variable?
func_really_bad_use_global_variable()  # suppose to set a_global_variable to 5
b_output_array_bad_optional = func_bad_use_global_variable(a_np_array)
print(f"Oops: new output array {b_output_array_bad_optional}")

# Optional: If you want to put some test code in your .py file, but you want to do it "right" this is the way
#  to do it - this code only gets executed if you execute this script.
# Define all of your functions first, then write the code that calls those functions here
if __name__ == '__main__':
    # Make some variables
    a_string = "Hello, I'm a string"
    b_list = [3.0, "hi", 10.0]
    c_dict = {"key 1":"value 1", "Key 2":0.3}

    # Test your function
    func_lots_of_params(a_string, b_list, c_dict)
