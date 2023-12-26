#!/usr/bin/env python3

import numpy as np


# ---------------------------- Class Example ---------------------------------
#
# Essentially re-do the pinball homework using classes
#  In this example we do one class for the walls (completed in lecture activity)
#
# Classes encapsulate data plus functions; instead of having data passed into the functions, the class stores
#  the data. The functions are "inside" the class, and have access to that data. As with using functions instead
#  of just writing all the code in one big long piece, classes help with making code clearer, easier to read, and
#  testable in pieces.
#
# Covering the full functionality of Python classes would take a long time; we focus here on the most common usage
#  of classes, which is this encapsulation. Learning about the syntax of how classes are structured will also help
#  you use classes other people have defined.

# Syntax: To declare a class, you just do
# class Classname:
#   and everything that is indented after that belongs to the class
#
# You'll see **self.** - this is how you access the data and the methods in the class from within the methods.
#
# You create variables for the class by doing **self.variablename = 3.0**, just like a regular variable.
#
# You create functions that belong to the class the same as a regular function, except the first parameter is "self"

class PinballWall:
    # This is the creator for the class - it gets called when you make a class (see below)
    def __init__(self, wall_type="Vertical", intercept_value=None, a_b_c=None):
        """Create a horizontal, vertical, or general half-plane wall
         if vertical/horizontal, use intercept value
         if general, use a_b_c
        @param wall_type - Vertical, Horizontal or General (ax + by + c = 0)
        @param intercept_value - number, where to place the wall on the x or y axis (Vertical or Horizontal)
        @param a_b_c - for General wall, list of 3 values"""

        # Save what kind of wall it is, then save as a general ax + by + c equation
        # What this does:
        #  - checks that the input is at least somewhat correct - eg, if they asked for a vertical wall they
        #    need to specify the intercept value
        # Lets the user "special case" a vertical or horizontal wall, rather than having to convert to the
        #   ax + by + c format
        if wall_type == "Vertical":
            self.wall_type = "Vertical"
            if intercept_value is None:
                raise ValueError("If vertical wall, need to specify intercept value")
            if intercept_value > 0:
                self.abc = [1.0, 0.0, -intercept_value]
            else:
                self.abc = [-1.0, 0.0, intercept_value]
        elif wall_type == "Horizontal":
            self.wall_type = "Horizontal"
            if intercept_value is None:
                raise ValueError("If horizontal wall, need to specify intercept value")
            if intercept_value > 0:
                self.abc = [0.0, 1.0, -intercept_value]
            else:
                self.abc = [0.0, -1.0, intercept_value]
        elif wall_type == "General":
            self.wall_type = "General"
            if a_b_c is None:
                raise ValueError("If general wall, need to specify a, b, and c a_b_c")
            if a_b_c[0] * 0 + a_b_c[1] * 0 + a_b_c[2] < 0:
                self.abc = [a_b_c[0], a_b_c[1], a_b_c[2]]
            else:
                self.abc = [-a_b_c[0], -a_b_c[1], -a_b_c[2]]
        else:
            raise ValueError("Wall type is not one of Vertical, Horizontal, or General")

    def evaluate_halfplane(self, x_y):
        """ Evaluate ax + by + c
        @param x_y numpy array/tuple for the current location
        @return ax + by + c"""
        # self is the same self we set in the __init__ function
        return self.abc[0] * x_y[0] + self.abc[1] * x_y[1] + self.abc[2]

    def outside(self, x_y):
        """ Is the point outside of this half/plane representing the wall?
        @param x_y numpy array/tuple for the current location
        @return True or False"""
        # We can call any of the methods defined in the class
        return self.evaluate_halfplane(x_y) >= 0.0

    def inside(self, x_y):
        """ We can call class methods from within class methods
        @param x_y numpy array/tuple for the current location
        @return True or False"""
        return not self.outside(x_y)

    def __str__(self):
        """
        The string representation of this class.
        :return: a string
        """
        # f"" creates a string; in this case, instead of printing it, just return it
        return f"{self.abc[0]:0.3f}x + {self.abc[1]:0.3f}y + {self.abc[2]:0.3f}"

    def test_on_wall(self, x_y):
        """ Pass in a point that should be on the wall; should return 0
         @param x_y - xy point
         @preturn True or False"""
        return np.isclose(self.evaluate_halfplane(x_y), 0.0)

    def test_origin_inside(self):
        """ Test that we correctly oriented the wall so that (0,0) is inside"""
        # Notice call to self
        assert(self.inside([0, 0]))
        return True

if __name__ == '__main__':
    # Now create two instances of the class
    # Notice that we do NOT pass in a self variable
    # Format is: variable_name = class_name(parameters to __init__)
    #. - this calls init - you don't call it directly
    my_vert_wall = PinballWall(wall_type="Vertical", intercept_value=.2)
    my_horiz_wall = PinballWall(wall_type="Horizontal", intercept_value=.2)

    # Print them both - this will call the string __str__ function - this is another example of a method that is
    #  not directly called, but is called for you when you Python wants to convert the class to a string
    # You can actually call my_vert_wall.__str__() - it will do the same thing
    print(f"Vertical wall: {my_vert_wall}")
    print(f"Horizontal wall: {my_horiz_wall}")

    # Now we'll try calling one of the methods in the class directly
    #
    # Check that we got the math right - should be 0 at 0.2, y for vertical wall
    # Notice the use of my_vert_wall. to say which wall to use
    #  this, essentially, is the same as calling
    #        PinballWall.evaluate_halfplane(self=my_vert_wall, x_y=[0.2, 10.0])
    x_y = [0.2, 10.0]
    eval_vert_at_line = my_vert_wall.evaluate_halfplane(x_y=x_y)
    print(f"Vertical wall evaluated at 0.2: {eval_vert_at_line}")
    assert(my_vert_wall.test_on_wall(x_y=x_y))

    x_y = [10.0, 0.2]
    eval_horiz_at_line = my_horiz_wall.evaluate_halfplane(x_y=x_y)
    print(f"Horizontal wall evaluated at 0.2: {eval_horiz_at_line}")
    assert(my_horiz_wall.test_on_wall(x_y=x_y))

    # Check the other test functions
    # A diagonal wall in the lower right corner
    my_general_wall = PinballWall("General", a_b_c=[1.0, 1.0, 0.7])
    # One cool thing with encapsulating code in classes is you can do things like this - this calls origin_inside for
    #   each instance of the class
    for w in [my_horiz_wall, my_vert_wall, my_general_wall]:
        w.test_origin_inside()

    # Some things that *don't* work
    #  - this doesn't work because you need an instance of PinballWall - i.e., the self pointer
    #  - notice that the error is a method not found error - that's because all of the methods in a class
    #   have a tag (the name of the class - PinballWall) pre-pended to the method name
    #    NameError: name 'evaluate_halfplane' is not defined
    # ret_val = evaluate_halfplane(x_y=[10.0, 0.2])

    # This solves the name error - we tell Python that we want the method in the PinballWall class
    # However, it generates a different error - because it's missing the "self" parameter
    #   TypeError: evaluate_halfplane() missing 1 required positional argument: 'self'
    # ret_val = PinballWall.evaluate_halfplane(x_y=[10.0, 0.2])

    # here we explicitly set the self pointer - you should never do this, it's just here to show you what is happening
    #  under the hood when you do my_vert_wall.evaluate_halfplane(x_y=[10.0, 0.2])
    ret_val = PinballWall.evaluate_halfplane(self=my_vert_wall, x_y=[10.0, 0.2])
