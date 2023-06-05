#!/usr/bin/env python3

import numpy as np
# YOUR CODE HERE

# ------------------------ Lab 9 classes ------------------------------
#
# TODO: Create a class for your bumper. Exactly how you create and store the bumper is up to you, but you should
#  define method(s) to determine if your pinball was inside/outside of the bumper, and a method to reflect the pinball
#  if it is inside
#
# You're welcome to add more methods to the class; just make sure not to rename the ones that are there
#   or change their parameters
# [Optional] add in your test code here as test methods on the class

# YOUR CODE HERE
class Bumper:
   # TODO: Define parameters to initialization function
    def __init__(self):
        # TODO: set self variables

    def __str__(self):
        # TODO Return a string that has the bumper info in it
        return ''

    def inside(self, x_y):
        # TODO Write a method that determines if the point is inside the bumper

    def reflect(self, x_y, vx_vy):
        # TODO: Write a method that reflects the pinball position and velocity

    def plot(self, axs, left, right, height):
        # TODO (HWK) Plot the bumper inside the box defined by left, right, height

    # Add your test methods here

# TODO: Create instance(s) of Bumper and check that they work
if __name__ == '__main__':

