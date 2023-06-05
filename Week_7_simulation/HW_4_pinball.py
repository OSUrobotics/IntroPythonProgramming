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


def length_of_pinball_path(poses):
    """ Calculate the length of the pinball path using euclidian distances
    @param poses - the x,y poses
    @return length"""
    # TODO: Sum up the distance between all of the pose points
    # Reminder: Distance is sqrt(x^2 + y^2)
# YOUR CODE HERE
    return 0.0


def integral_of_path_velocity(velocities, delta_t):
    """ Calculate the x and y distance traveled of the pinball path by integrating the velocities
    @param velocities - the vx,vy velocities at each time step
    @param delta_t - the sampling used to generate the velocities
    @return integral of vx, integral of vy"""
    # TODO: Calculate the integral of vx and vy
    # Note: You'll want trapz because these are samples of the velocity function
# YOUR CODE HERE
    return integral_x, integral_y


# TODO: Set up the starting state to do an interesting bounce
if __name__ == '__main__':
    # Time step
    delta_t = 0.01

    xs = np.linspace(0, 1)
    v = np.trapz(xs, dx=0.1)
    # Test 1 - do you stop when you hit the floor?
    starting_state = np.zeros([3, 2])  # location, velocity, acceleration
    starting_state[0, :] = [0, 0] # Start at zero, zero
    # Velocity - mostly up with a bit of x noise
    # Check top wall only
    # starting_state[1, :] = [-0.2, 10.0]
    # Check all walls
    # starting_state[1, :] = [5.2, 5.0]
    # Check bottom left bumper
    starting_state[1, :] = [2.4, 8.5]
    # Check distance traveled
    starting_state[1, :] = [0.5, 3.5]
    starting_state[2, :] = [0.0, acceleration_due_to_gravity()]

    # TODO Add your test code, definitions of the walls, etc here
    # TODO Plot the pinball setup plus your path
# YOUR CODE HERE

    # TODO For these tests  and use this starting state
    #  - do NOT place a bumper/wall in the path - it should just go up and down
    #  - Use the given starting position and velocity
    #  - Use a delta t of 0.01
    #  - Do NOT do damping
    starting_state = np.zeros([3, 2])  # location, velocity, acceleration
    starting_state[0, :] = [0, 0] # Start at zero, zero
    # Velocity - mostly up with a bit of x noise
    starting_state[1, :] = [0.5, 3.5]
    starting_state[2, :] = [0.0, acceleration_due_to_gravity()]

    # TODO: call your simulate routine with  delta_t = 0.01 and the above starting state

# YOUR CODE HERE
    ret_poses, ret_velocities = simulate_pinball(starting_state, ..., delta_t=delta_t)

    len_path = (length_of_pinball_path(ret_poses))
    print(f"Distance traveled {len_path}, expected 1.386298")
    integral_x, integral_y = integral_of_path_velocity(ret_velocities, delta_t)
    print(f"Integral of x velocity {integral_x}, expected 0.365")
    print(f"Integral of y velocity {integral_y}, expected -0.056209")
    assert(np.isclose(len_path, 1.386298, atol=0.001))
    assert(np.isclose(integral_x, 0.365, atol=0.001))
    assert(np.isclose(integral_y, -0.056209, atol=0.001))
    print("Done")

