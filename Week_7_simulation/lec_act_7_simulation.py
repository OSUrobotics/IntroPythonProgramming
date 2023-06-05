#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Routines we'll re-use
from pinball_routines import compute_next_step, acceleration_due_to_gravity

# ----- iterative systems part II ----------
# This is a continuation/extension of week 4's simulation with some slight modifications
#
# Full 2D - position and velocity of a point in space
# Integrate velocity as well as position
#
# Slides: https://docs.google.com/presentation/d/1ruu1Lq9MpYSHiVa5RNrvyxap4yXpTpiXf_VTzHKAFb8/edit?usp=sharing

# Code structure: I've broken the code up in to several pieces: Code that is shared across the lecture activity,
# lab, and homework is in pinball_routines.py. Code that is specific to just the one assignment (running the simulation,
# plotting) is in the JN/the assignment .py files.

# ------------------- Simulation ------------------------
# Note that you could use either the number of time steps OR total time for the last parameter
#  Timesteps is a bit safer because at least you know it will only go for so many time steps...
#  In this activity we'll just loop over n time steps; we'll do something "smarter" in the lab
#
def calculate_n_time_steps(starting_state, delta_t=0.1, n_time_steps=100):
    """ Call compute one time step multiple times and store it in a numpy array
    @param starting_state - the starting positino, velocity, acceleration
    @param delta_t - the time step to use. Define a default t value that you've determined works well
    @param n_time_steps - how many time steps to take. Again, default to a reasonable number
    @return position values as a 2xtimesteps numpy array
    """

    # The returned array. We know the size, so we can pre-allocate it
    ret_pose_all = np.zeros((2, n_time_steps))

    # TODO: for the given number of time steps, call compute_next_step and save the position
    # Note: compute_next_step is in pinball_routines.py
# YOUR CODE HERE
    # All done - return the numpy array
    return ret_pose_all


# ------------------- plots ------------------------

# This is pretty arbitrary - but I chose to ask the person calling the function to pass in the poses returned from
#  the interation and the initial velocity (so we can see it).
def plot_results(ret_poses, initial_vel, total_time):
    """ plot the results of running the system AND the "correct" closed form result
    @param ret_poses - x y position values in a 2xn numpy array
    @param initial_vel - Show the initial velocity
    @param total_time - the total time the system ran (for closed form solution, delta_t * n time steps)
    @return Nothing
    """
    nrows = 1
    ncols = 1
    fig, axs = plt.subplots(nrows, ncols, figsize=(4, 4))

    # The values we calculated in calculate_n_time_steps
    axs.plot((ret_poses[0, 0], ret_poses[0, 0] + initial_vel[0]),
             (ret_poses[1, 0], ret_poses[1, 0] + initial_vel[1]),
             '-m', label="Initial vel")
    axs.plot(ret_poses[0, 0], ret_poses[1, 0], 'xr', markersize=10, label="Start")
    axs.plot(ret_poses[0, :], ret_poses[1, :], '-Xk', label="Poses")

    axs.axis('equal')
    axs.set_title(f"Path of object, 0-{total_time} s")
    axs.legend()


# TODO: Play around with the starting velocities, delta t, and number of time steps. Make sure to reset
# to the given ones for the automated tests
if __name__ == '__main__':
    # Time step
    delta_t = 0.1

    starting_state = np.zeros([3, 2])  # meters
    starting_state[0, :] = [0, 0] # Start at zero, zero
    # Velocity - mostly up with a bit of x
    starting_state[1, :] = [-0.25, 5.0]
    # Acceleration is really boring
    starting_state[2, :] = [0.0, acceleration_due_to_gravity()]

    first_time_step = compute_next_step(starting_state, delta_t=delta_t)
    print(f"Checking first time step {first_time_step}")

    assert(np.all(np.isclose(first_time_step[0, :], starting_state[0, :] + delta_t * starting_state[1, :])))
    assert(np.all(np.isclose(first_time_step[1, :], starting_state[1, :] + delta_t * starting_state[2, :])))

    # Set number of time steps
    ret_poses = calculate_n_time_steps(starting_state, delta_t=delta_t, n_time_steps=15)
    print(f"Last pose: {ret_poses[:, -1]}")
    assert(np.isclose(ret_poses[0, -1], -0.35))
    assert(np.isclose(ret_poses[1, -1], -1.918))

    n_time_steps = ret_poses.shape[1]

    total_time = delta_t * n_time_steps
    plot_results(ret_poses, starting_state[1, :], total_time)
    print("Done")

