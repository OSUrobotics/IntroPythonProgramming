#!/usr/bin/env python3

# ------------------------------------------------------------------------------
# String formatting practice
#
x = 3.7925
y = 1.3e10
x_name = "x"
y_name = "y"

# Create a formatted string and print it out
#   Use "".format with {} OR the f"" syntax
# DON'T copy the stuff from the variables above into the string - if you change any of the variable values above
#  it should still work

# LO: Use of {} in a string with format
# First version - modify one (or both) of the print statements below to produce:
#   First variable is x, value 3.7925, second variable is y, value 13000000000.0
print("First variable is , value , second variable is , value ".format())
print(f"First variable is , value , second variable is , value ")

# LO: Use of modifiers in {} to format numbers
# Second version - modify one (or both) of the print statements below to produce:
#   First variable is x, value 3.79, second variable is y, value 1.30e+10

# LO: Can do equations in format, newline (\n) and tab (\t)
# Third version - modify one (or both) of the print statements below to produce:
#   - do this with ONE print statement, using \n, and without creating new variables
#   - hint mu is (x + y) / 2
# Variables (x, y), values (3.79, 1.30e+10),
# 	mu 6500000001.90

# ------------------------------------------------------------------------------
# Splitting up long strings into text and numbers
#
# LO: String indexing, building one string from multiple ones (use + or "".format or f"")
# Change my_new_fname to be "foo.csv" instead of "foo.txt'
#   You must use my_fname - don't just type in the values. This should work even if you change foo to something else
# Should output:
# Old file name: foo.txt, New file name: foo.csv

my_fname = "foo.txt"

my_new_fname = my_fname
print(f"Old file name: {my_fname}, New file name: {my_new_fname}")

# LO: Find (and replace) dashes or other special characters in a string
# Replace the dash with a space
# Should output:
# Dashed: a-dash, not dashed: a dash
str_with_dash = "a-dash"
str_without_dash = str_with_dash
print(f"Dashed: {str_with_dash}, not dashed: {str_without_dash}")

# Do these in order
# LO: strip for removing unwanted characters
#  First change: Take out the () so a string and 10 don't have parenthesis in them
#  Second change: Remove extra white space so everything prints left-justified
#   - hint: strip with no parameters will take out ALL white space (including tabs and new lines)
#   - you can do the strip on the ENTIRE string OR on each individual one - doesn't really matter
# LO: Using the .isxxx() methods to determine if the string is an integer or not
#  Third change: Print out either "Is an integer [the number]" or "Is not an integer [the string]" for each string
#   - you will have to do this on individual strings AND add an if statement into the for loop...
#   - [optional] if you want to detect 3.7 or 1e30 you need to try converting to a number and then throw an
#        exception if it didn't work - see answers below
# LO: Use the cast int() or float() to convert a string to a number
#  Fourth change: Add 2 to the number before printing it out
#  Fifth change: take out any dashes or ' in the strings
# LO: Putting strings together in a for loop (how to do an append), str() to convert a number to a string
#  You will need to do the following, because you can't edit strings in place - this creates a new string from the
#    old one plus the new stuff
#  my_new_str
#  for [blah]
#     my_new_str = my_new_str + [new stuff]
#           OR
#     my_new_str = f"{my_new_str} new stuff"
#
#  Glue the string back together. The for loop and the final print should produce:
# Is not an integer: a string
# Is not an integer: 3.7
# Is not an integer: a dash
# Is not an integer: 1e30
# Is an integer: 7, adding two: 9
# Is not an integer: a tick
# Is an integer: 10, adding two: 12
# My fixed string: (a string, 3.7, a dash, 1e30, 9, a tick, 12)
#
my_long_str = "(a string, 3.7, a-dash, 1e30, 7, a'tick, \n \t 10)"
my_fixed_str = my_long_str
for my_str in my_long_str.split(","):
    print(f"{my_str}")
print(f"My fixed string: {my_fixed_str}")

# ------------------------------------------------------------------------
# ANSWERS
print("-"*10 + "ANSWERS" + "-"*10)
print("First version")
print("First variable is {}, value {}, second variable is {}, value {}".format(x_name, x, y_name, y))
print(f"First variable is {x_name}, value {x}, second variable is {y_name}, value {y}")

print("Second version")
print("First variable is {}, value {:0.2f}, second variable is {}, value {:0.2e}".format(x_name, x, y_name, y))
print(f"First variable is {x_name}, value {x:0.2f}, second variable is {y_name}, value {y:0.2e}")

print("Third version")
print("Variables ({}, {}), values ({:0.2f}, {:0.2e}), \n\tmu {:0.2f}".format(x_name, y_name, x, y, (x + y) / 2))
print(f"Variables ({x_name}, {y_name}), values ({x:0.2f}, {y:0.2e}), \n\tmu {((x + y) / 2):0.2f}")

# --------
print("-"*20)
# I like plus in this case (rather than format) because you're just putting two strings together
my_new_fname_v1 = my_fname[:-4] + ".csv"
# But this works too
my_new_fname_v2 = f"{my_fname[:-4]}.csv"
# And this...
my_new_fname_v3 = "{}.csv".format(my_fname[:-4])
# Print out the new file names
print(f"Old file name: {my_fname}, New file name: {my_new_fname_v1}")
print(f"Old file name: {my_fname}, New file name: {my_new_fname_v2}")
print(f"Old file name: {my_fname}, New file name: {my_new_fname_v3}")

# --------
# Simplest dash replace:
str_without_dash = str_with_dash.replace("-", " ")
print(f"Dashed: {str_with_dash}, not dashed: {str_without_dash}")

# You can also use find and string indexing to do it manually
index_dash = str_with_dash.find("-")
str_without_dash = str_with_dash[0:index_dash] + " " + str_with_dash[index_dash+1:]
print(f"Dashed: {str_with_dash}, not dashed: {str_without_dash}")

# ----
#  This strips out both the ( and the ) from the string
#  You COULD do the following if you want to strip out all the white space at the same time:
my_do_it_all = my_long_str.strip("()").strip()   # optional
print(my_do_it_all)
m_long_str_modified = my_long_str.strip("()") # Or just take out the () and do the white space later
# Building the new string
my_fixed_string = "("  # Start with the (

# Split returns a list of strings, removing the ,
#   The for loop will assign my_str to each of those strings in the list in turn
for my_str in m_long_str_modified.split(","):
    # Remove the white space - don't pass in parameters if you want strip to remove ALL types of white space
    my_str_modified = my_str.strip()
    # See if we have a digit
    if my_str_modified.isdigit():
        # Note the conversion to int - you can't add 2 to a string
        my_num = int(my_str_modified) + 2
        # Note the my_fixed_string = my_fixed_string - you can't edit my_fixed_string, but you can make a new
        #   string from my_fixed_string and then assign that to the same variable
        my_fixed_string = my_fixed_string + str(my_num) + ", "   # Note the cast back to a str
        # Print statement
        print(f"Is an integer: {my_str_modified}, adding two: {my_num}")
    else:
        # You can do this one at a time - note that my_str_modified is on the left and right (rather than creating
        #   a new variable)
        my_str_modified = my_str_modified.replace("-", " ")
        my_str_modified = my_str_modified.replace("'", " ")
        # OR
        my_str_modified = my_str_modified.replace("-", " ").replace("'", " ")
        # See above about building my_fixed_string
        my_fixed_string = my_fixed_string + my_str_modified + ", "

        # Print statement
        print(f"Is not an integer: {my_str_modified}")

# Take out the last comma and add the )
my_fixed_string = my_fixed_string[0:-2] + ")"
print(f"My fixed string: {my_fixed_string}")

# ----------------------
# OPTIONAL - doing it the fancy way with join and a list
# This version is a bit "easier" to debug, because we split up the string, then store each piece in the list,
#  and wait until the end to put the list back together. This separates out two conceptual steps - splitting up and
#  editing the original list, and sticking the list back together into a string.
my_fixed_strs_fancy = []  # where to put the fixed strings

# Outer for loop is the same
for my_str in m_long_str_modified.split(","):
    # Remove the white space - don't pass in parameters if you want strip to remove ALL types of white space
    my_str_modified = my_str.strip()
    # See if we have a digit
    if my_str_modified.isdigit():
        # Note the conversion to int - you can't add 2 to a string
        my_num = int(my_str_modified) + 2
        # Convert back to a string
        my_num_str = str(my_num)
        # Put the new string in the list - note the str() to cast the number to a string
        my_fixed_strs_fancy.append(my_num_str)
        # Print statement
        print(f"Is an integer: {my_str_modified}, adding two: {my_num}")
    else:
        # Do all the modifications at once
        my_str_modified = my_str_modified.replace("-", " ").replace("'", " ")

        # Put the new string in the list
        my_fixed_strs_fancy.append(my_str_modified)

        # Print statement
        print(f"Is not an integer: {my_str_modified}")

# This is the more elegant way to do this, building a list of strings then using join to put them together with ,s
my_fixed_string_fancy = "(" + ", ".join(my_fixed_strs_fancy) + ")"
print(f"My fixed string fancy: {my_fixed_string_fancy}")

# OPTIONAL - if you want to do the decimals/other number formats, the right thing to do is TRY to cast the
#  string to a number and then, if it fails, assume it is not a number
my_fixed_strs_fancy = []
for my_str in m_long_str_modified.split(","):
    # Don't need to remove the white space because the cast will do it
    try:
        # Try to cast to a float and add two
        my_num = float(my_str) + 2
        my_str_modified = str(my_num)  # You could do these in one line, but...
        print(f"Is a number: {my_str_modified}")
    except ValueError:
        # If the above code failed, do this instead
        my_str_modified =  my_str.strip().replace("-", " ").replace("'", " ")
        print(f"Is not a number: {my_str_modified}")

    my_fixed_strs_fancy.append(my_str_modified)

my_fixed_string_fancy = "(" + ", ".join(my_fixed_strs_fancy) + ")"
print(f"My fixed string fancy: {my_fixed_string_fancy}")
