#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Routines we'll re-use
# YOUR CODE HERE

# ----- iterative systems part III ----------
# We'll add two things here:
# 1) Circular "bumpers"
# 2) Some bumpers will impart an acceleration to the pinball
#
# See Slides for how to handle a circular bumper


# Start with lab...
# TODO 1: Set it up to reflect off of circular bumpers
#   Think how you'll store the walls/bumpers
#   Think how you'll alter simulate pinball to bump off of walls and bumpers
# TODO 2: Add in accelerating off of some bumpers
#   Think how you'll change acceleration so that you can have a one-time acceleration on an impact
#
# YOUR CODE HERE


# TODO: Plot the track, walls, and bumpers
#  Start with the lab
# YOUR CODE HERE


# TODO: Play around with delta t and see what happens when it hits the wall
if __name__ == '__main__':
    # Time step
    delta_t = 0.01

    # Test 1 - do you stop when you hit the floor?
    starting_state = np.zeros([3, 2])  # location, velocity, acceleration
    starting_state[0, :] = [0, 0] # Start at zero, zero
    # Velocity - mostly up with a bit of x noise
    # Check top wall only
    # starting_state[1, :] = [-0.2, 10.0]
    # Check all walls
    # starting_state[1, :] = [5.2, 5.0]
    # Check top left bumper
    starting_state[1, :] = [2.4, 8.5]
    starting_state[2, :] = [0.0, acceleration_due_to_gravity()]

    # Define a dictinary that holds the walls and bumpers
    # Default is top wall at y=5, left/right walls at +- 3.0
    # Bumpers of radius around 1 at each corner
# YOUR CODE HERE
    print("Done")

