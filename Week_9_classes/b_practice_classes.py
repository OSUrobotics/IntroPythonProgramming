#!/usr/bin/env python3

import numpy as np

#------------------------ Circle class ----------------------
# Create a class named Circle that takes as input a radius when it is created, and has two methods, one that
#  returns the area of the circle, the other that returns the perimeter. Write code to create two circles, one with
#  radius 1 and one with radius 2 and print out their area and circumference
#
# [optional-fancy] If you stick the two class instances in a list, you can print them both out with a for loop...

# ----------------- Answers --------------------------------
class Circle:
    """
    A 2d circle.
    """

    def __init__(self, radius):
        """
        Constructor.
        :param radius: The circle radius.
        """
        # We're not going to allow a negative radius.
        if radius < 0:
            raise ValueError('Circle: Radius must be non-negative')

        self.radius = radius

    def __str__(self):
        return 'Circle({0})'.format(self.radius)

    def area(self):
        """
        Circle radius.
        :return: The radius of the circle.
        """
        return np.pi * self.radius ** 2

    def circumference(self):
        """
        The circumference of the circle.
        :return: The circle circumference.
        """
        return 2 * np.pi * self.radius


if __name__ == '__main__':
    c1 = Circle(1.0)
    c2 = Circle(2.0)

    # Since the circles are just... objects, we can stick them in a list
    shapes = [c1, c2]
    for s in shapes:
        print(f"{s}: area is {s.area():0.2f}, circumference is {s.circumference():0.2f}")
