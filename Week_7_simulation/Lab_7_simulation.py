#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Routines we'll re-use
from pinball_routines import compute_next_step, acceleration_due_to_gravity, outside_top_wall, outside_left_wall, outside_right_wall

# ----- iterative systems part II ----------
# We'll add two things here:
# 1) Stop when the "ball" drops below the y = 0 line
# 2) "Bouncing" off of the top and side walls
#
# See Slides for how to handle crossing a wall (naive versus smart fix)


# Switch from going a set number of time steps to going until the ball passes through y = 0
# TODO 1: Set it up to return when passing through floor
# TODO 2: Add in reflecting off of walls
#  - negate the velocity
#  - reposition on the wall
#  - fancy - actually calculate the intersection and reflect the remaining vector back
# Keep the pose just after the ball passes through the floor - so the second to last pose should be above the floor, the last below it
#
def simulate_pinball(starting_state, top_wall=5.0, left_wall=-3.0, right_wall=3.0, delta_t=0.1):
    """ Call compute one time step multiple times and store it in a numpy array
    @param starting_state - the starting positino, velocity, acceleration as a 3x2 numpy array
    @param top_wall y value of top of pinball box
    @param left_wall x value of left wall of pinball box
    @param right_wall x value of right wall of pinball box
    @param delta_t - the time step to use. Define a default t value that you've determined works well
    @return position values as a 2xtimesteps numpy array
    """

    # The returned array. We do not know the size, so do not pre-allocate
    ret_pose_all = []

    # TODO Use a while loop instead of the for loop
    # Set the stopping criteria based on current state y value
    # Add in each wall/top at a time (there are test routines for reach below)
    # Use if statements, not if-else statements, because it is possible to be outside of the top and side wall...
# YOUR CODE HERE
    # All done - return the numpy array
    return np.array(ret_pose_all).transpose()


# Plot the walls and the pinball path
def plot_pinball_lab(ret_poses, walls, total_time):
    """ plot the results of running the system AND the "correct" closed form result
    @param ret_poses - x y position values in a 2xn numpy array
    @param walls - The walls and ceiling locations (top, left, right)
    @param total_time - the total time the system ran (for closed form solution, delta_t * n time steps)
    @return Nothing
    """
    nrows = 1
    ncols = 1
    fig, axs = plt.subplots(nrows, ncols, figsize=(4, 4))

    # The values we calculated in calculate_n_time_steps
    axs.plot([walls[1], walls[2]], [walls[0], walls[0]], '-m', label="Top wall")
    axs.plot([walls[1], walls[2]], [0, 0], '-k', label="Floor wall")
    axs.plot([walls[1], walls[1]], [0, walls[0]], '-g', label="Left wall")
    axs.plot([walls[2], walls[2]], [0, walls[0]], '-g', label="Right wall")

    axs.plot(ret_poses[0, 0], ret_poses[1, 0], 'xr', label="Start")
    axs.plot(ret_poses[0, :], ret_poses[1, :], '.-k', label="Poses")

    axs.axis('equal')
    axs.set_title(f"Boring pinball, 0-{total_time} s")
    axs.legend()


# TODO: Check with different starting states. Set to final one when done (bouncing off all walls)
if __name__ == '__main__':
    # Time step
    delta_t = 0.01

    # Test 1 - do you stop when you hit the floor?
    starting_state = np.zeros([3, 2])  # location, velocity, acceleration
    starting_state[0, :] = [0, 0] # Start at zero, zero
    # Velocity - mostly up with a bit of x noise
    # Check stopping condition only
    # starting_state[1, :] = [-0.3, 5.0]
    # Check top wall only
    # starting_state[1, :] = [-0.2, 10.0]
    # Check all walls
    starting_state[1, :] = [-10.2, 10.0]
    starting_state[2, :] = [0.0, acceleration_due_to_gravity()]

    # walls: top, left, right
    top_wall = 5.0
    left_wall = -3.0
    right_wall = 3.0
    # Do the simulation
    ret_poses = simulate_pinball(starting_state, top_wall=top_wall, left_wall=left_wall, right_wall=right_wall, delta_t=delta_t)

    # TODO Put your checks here
# YOUR CODE HERE
    walls = [top_wall, left_wall, right_wall]
    total_time = delta_t * ret_poses.shape[1]
    plot_pinball_lab(ret_poses, [top_wall, left_wall, right_wall], total_time)
    print("Done")

