#!/usr/bin/env python3

# What are strings?
#
# Strings are just arrays of characters. They are immutable - the can't be edited "in place".
# A character is a single letter or symbol. They are actually numbers - see ASCII table - that we interpret as
#  letters/numbers/symbols/whitespace etc.
# Strings are primarily used for displaying data in a "human readable" form, but they can also be used as parameters
#  to functions.
# The primary "gotcha" of strings is that the string "3.5" is NOT the number 3.5 - it is three characters, 3.5, that
#  can be converted to a number (or is the string version of a number).
#
# There are many utilities/functions for converting from other data types (like numbers, dates, times) to strings and
#   back again, and for splitting up/processing strings (eg, taking out white space, dashes, etc)

# ------------------------------------------------------------------------------
# Printing out variables or displaying them in the debugger: This is probably the most common use for strings

# A random collection of variables of different types - look at their type in the debugger
a_floating_point_number = 3.6720
an_integer = 6
a_string = "I am a string"
a_string_with_symbols = "% {} \n '"

# Make a list out of all of those items
a_list_of_all = [a_floating_point_number, an_integer, a_string, a_string_with_symbols]

# Print out the variable, no formatting
#   You can print out more than one thing
print(a_floating_point_number)
print(a_floating_point_number, a_string_with_symbols)

# What this is doing underneath - run this in the debugger and look at they types for each
# Convert the variable to a string
a_temp_str = str(a_floating_point_number)
# print JUST takes strings - but it automatically converts the things in parentheses to strings before printing
print(a_temp_str)

# What does this look like? Why does it not look exactly like the a_string_with_symbols?
print(a_string_with_symbols)
# answer: The \n is a "special" character that puts in a new-line - print finds any of these and replaces them
#   with a new line when it writes to the console

# Why does this work? What is it doing?
print(a_list_of_all)
# answer: a list is always printed as [ , , ] with print called for each element. Note that, in this case, because
#  a_string_with_symbols is already a string, it just prints it out - and does NOT interpret the \n

# An aside: If you want to print out each of the elements in turn in the string, you can do it this way:
for item in a_list_of_all:
    print(item)

# Formatting a string - this is how you create a "nice" string for printing. You should always make "nicely" formatted
#  strings for printing. Yes, this syntax is weird. Think of it as calling the string function
#     format("string to format var 1 (put first variable here) var 2 (put second variable here)", first variable, second)
#  The curly brackets tell the format function to "fill in" the variables that are passed in
# Note that I've split up the creating of the string from the printing here....
a_formatted_str = "string to format var 1 {} var 2 {}".format(a_floating_point_number, an_integer)
print(a_formatted_str)
# but you can do both in one line
print("string to format var 1 {} var 2 {}".format(a_floating_point_number, an_integer))

# The {} syntax can do A LOT - left indent, print with a certain precision, etc. In this example, the first parameter
#   is printed twice, once with no formatting, once with fancy formatting, with a special character (the /n) to separate
#   the lines.
# See here: https://docs.python.org/3/library/string.html#formatspec for a full list of functionality.
# Note that you can use "" for specifying a string OR ''.
#  If no numbers are given in the {} it takes them in order; there need to be as many variables as {}
print('No formatting: {}\nFormatted: {:.2}'.format(a_floating_point_number, a_floating_point_number))
#  If numbers are given then it takes them in that order (indexing from 0)
print("No formatting: {0}\nFormatted: {0:.2}".format(a_floating_point_number))
#  Or you can use names - in this case, x, to refer to the parameter
print('No formatting: {x}\nFormatted: {x:.2}'.format(x=a_floating_point_number))

# Note that you can use the '+' with strings to "glue" a bunch of strings together if you don't need the full functionality
#  of the format function - this can be handy, for example, for creating a file name:
data_dir = "home/directory/directory/"
file_name = "my_file_name"
file_type = "csv"
str_file_name = data_dir + file_name + "." + file_type
print(str_file_name)

# OPTIONAL: if you don't like typing, Python provides a "shortcut" for "".format() called f-strings
#  See, eg, https://realpython.com/python-f-strings/
#  Basically, this takes out the explicity .format part and lets you put variables directly in the {}
f"No formatting: {a_floating_point_number}\nFormatted: {a_floating_point_number:.2}"
# END OPTIONAL

# OPTIONAL: You can use the .join function on a list to format a string from a list in one command:
# This doesn't do quite what you want
a_list_of_strings = ["Hi", "how", "are", "you?"]
print(str(a_list_of_strings))
# Instead use join
print("".join(a_list_of_strings))
# ... and once again, with spaces...
print(" ".join(a_list_of_strings))
# ... and one more time with numbers...
list_of_numbers = [0.3 + 0.1 * n for n in range(0, 10)]
print(", ".join(["{:.2}"] * len(list_of_numbers)).format(*list_of_numbers))

# ... taking the above apart...
list_of_n_curlies = ["{:.2}"] * len(list_of_numbers)  # Uses the * with a string to make multiple copies
curlies_with_commas = ", ".join(list_of_n_curlies)   # Use join to convert the list to one string
# The *list_of_numbers is puts each item in in turn, and is the same as l[0], l[1], l[2]... l[n]
fill_in_curlies = curlies_with_commas.format(*list_of_numbers)
print(fill_in_curlies)

# In more traditional code, this would be written as
my_str_list = ""
for n in list_of_numbers:
    str_n = "{:.2}".format(n)  # Convert n to a string, with formatting
    my_str_list = my_str_list + str_n + ", "  # append the string for n with a ,
my_str_list = my_str_list[0:-2]  # Take out the last ,
print(my_str_list)

# END OPTIONAL

# ------------------------------------------------------------------------------
# Converting strings to numbers - this mostly just "works".
a_number = float("3.57")
an_exp_number = float("3.3e-3")
an_integer = int("3")

# ERRORS - converting a string to a number
# It will throw an error if, for example, you try to convert a string that isn't a number - uncomment these lines and
#   you'll get ValueError: could not convert string to float: 'a3.2' printed out to the command line
# UNCOMMENT
#bad_number = float("a3.2")
#  ... and this one gives ValueError: invalid literal for int() with base 10: '6.7'
# UNCOMMENT
#bad_int_number = int("6.7")
# END ERRORS

# ERRORS - weird behavior with a number and string
# Why you need to know that strings are arrays of numbers, NOT the number:
my_str_not_a_number = "3.6"
# Weird string behavior - the '*' is interpreted as make 3 copies of the string
my_str_times_3 = my_str_not_a_number * 3
# Causes a TypeError: unsupported operand type(s) for +: 'int' and 'str'
# END ERRORS

# ERRORS - you can't change an element of a string because it is immutable
# TypeError: 'str' object does not support item assignment
my_str = "A long string"
# Attempting to convert the first character to a lower case
# UNCOMMENT
# my_str[0] = 'a'
# The right way to do this is to create a new string with the change and assign it to the same variable
my_str = my_str.lower()
# OR
my_str = 'a' + my_str[1:]
# END ERRORS
