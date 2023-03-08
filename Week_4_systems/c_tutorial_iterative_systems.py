#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# ----- iterative systems (using functions) ----------
# A large number of engineering/economics/ecosystem problems can be defined by how things change over time (basically
#  partial differential equations). One of the very first examples of this is the "predator-prey" equations, also
#  known as the Lotka-Volterra equations (see https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations). There
#  is no shortage of problems that can be written like this, from how leopard spots form (reaction-diffusion equations)
#  to modeling heat diffusion to chemical reactions.
#
# In this tutorial we are going to focus on implementing a very simple iterative example - calculating how
# an object moves as it is thrown up in the air - and focus on one of the more challenging aspects
# of this type of problem - the role of time. There are two common issues with iterative examples, one theoretical,
# another a common programming mistake
#
# Time: Equations are continuous. We approximate them computationally by taking time steps. The smaller the time step,
#  the more accurate - but slow - the solution.
#
# 1) Theoretical: If the time step is too big, and/or the derivatives are changing a lot, then the approximation is off.
#    Unfortunately, setting the time step to be really small means the entire thing runs really slow.
# 2) When calculating the values for the next time step, ALL of the input values should be from the previous time step.
#    It is rather easy to accidentally use a next-time-step value in the calculation
#
# Code: This will also be an example of functions calling functions - structuring code so it doesn't all happen
# in one big chunk. This helps prevent problem 2
#

# The equation we're going to do has what's called a closed-form solution - you can just write down where the object is
#  after a given amount of time. We're going to use that equation to "check" our answer. Of course, the reason this
#  example is used all the time when teaching is because it *has* a closed form solution - most real-world examples
#  don't.

# I like this version of describing the formula: https://www.fisicalab.com/en/section/parabolic-motion but there is
#  no shortage of descriptions out there

# Code structure: I've broken the code up in to several pieces: what is the acceleration (so we can change it if we
#  want in just one place), computing the next position and velocity from the previous one, and doing a sequence
#  of computations. And the plot function.

def acceleration_due_to_gravity():
    """Somewhat silly - but if we need to change it, then we can  change it just here"""
    gravity = -9.8     # m/s
    return gravity


# It seems a bit overkill to make a functions for the update, but it *does* make it easier to
#  debug, because you can check if this function is correct with some known values
def compute_next_position_and_velocity(pos, vel, delta_t=0.1):
    """ How to compute the next pose from current values of position and velocity (the partial differential equation)
    @param pos - the pose (x, y) as a numpy array
    @param vel - the current velocity (vx, vy) as a numpy array
    @param delta_t - the time step to use. Define a default t value that you've determined works well
    @return the new position, velocity as a tuple"""

    # The new position (for both x and y) is just p + dt * v - current position + delta t * velocity
    pos_new = pos + delta_t * vel   # Numpy arrays will handle doing both x and y

    # The new velocity for x is just the old velocity
    # Make a new array - note, if you don't, and do this instead
    #   vel_new = vel
    # Then you will CHANGE vel_inital in the calling function
    # TODO - replace this line with vel_new = vel and see what happens to vel_initial
    vel_new = np.zeros(vel.shape)

    # Set the vx value to be the same as the old one
    vel_new[0] = vel[0]

    # The new velocity for y is the old velocity plus acceleration * dt - which in this case is gravity
    # You could make these parameters, but to keep things simple, we'll just declare them here
    vel_new[1] = vel[1] + delta_t * acceleration_due_to_gravity()

    return pos_new, vel_new


# Note that you could use either the number of time steps OR total time for the last parameter
#  Timesteps is a bit safer because at least you know it will only go for so many time steps...
#
# Decisions made:
#   Instead of returning JUST the final pose, we're returning all of the intermediate poses. This makes debugging a
#   bit easier - can plot all of the intermediate poses and see if they make sense. You can always get the final
#   pose out by doing ret_pose[:, -1].
#
#   NOT keeping/returning the final/intermediate velocities. You certainly could - in fact, you will do just that
#   in the practice version of this script.
#
#   Using numpy arrays and pre-allocating space, rather than a list and using append and some other stopping criteria
#   (like hit the ground). Almost always better to do it this way, at least at first; trying to write end conditions
#   for this sort of iterative calculation can be difficult to get correct, and it also means you're debugging two
#   things at the same time - the interative update AND the stopping conditions.
#
#   Note that in the practice script we will change this up to stop when the object hits the ground and return the
#   final velocity. Neither of these are "right" or "wrong" - it's just what you want the behavior to be.
#
#   I'm doing this one first - keep all the poses, return them - because it's easier to debug
def calculate_n_time_steps(pos_initial, vel_initial, delta_t=0.1, n_time_steps=100):
    """ Call compute one time step multiple times and store it in a numpy array
    @param pos_initial - the starting x,y position (numpy array)
    @param vel_initial - the starting vx, vy velocity (numpy array)
    @param delta_t - the time step to use. Define a default t value that you've determined works well
    @param n_time_steps - how many time steps to take. Again, default to a reasonable number
    @return x, y values as a 2xtimesteps numpy array
    """

    # The returned array. We know the size, so we can pre-allocate it
    ret_pose_all = np.zeros((2, n_time_steps))
    # We know the first pose is the initial one
    ret_pose_all[:, 0] = pos_initial
    vel_last = vel_initial

    # Note the start from 1 - you already know what the values for 0 should be
    for i in range(1, n_time_steps):
        # Make sure to use the last x,y values you just computed
        pos_next, vel_next = compute_next_position_and_velocity(ret_pose_all[:, i-1], vel_last, delta_t=delta_t)

        # Put the new values into the numpy array
        ret_pose_all[:, i] = pos_next

        # Now it is safe to set the velocity we'll use at the next time step from the one we just calculated
        vel_last = vel_next

    # All done - return the numpy array
    return ret_pose_all


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
    axs.plot(ret_poses[0, :], ret_poses[1, :], '-k', label="Poses")
    axs.plot((ret_poses[0, 0], ret_poses[0, 0] + initial_vel[0]),
             (ret_poses[1, 0], ret_poses[1, 0] + initial_vel[1]),
             '-m', label="Initial vel")

    # The closed-form solution
    #  x = x_initial + total_time * x velocity
    #  y = y_initial * total_time + (1/2) a (t^2), a being gravity -9.8
    ts = np.linspace(0, total_time, ret_poses.shape[1])
    xs = ret_poses[0, 0] + ts * initial_vel[0]
    # Split this up
    ys = ret_poses[1, 0] + initial_vel[1] * ts + (1/2) * acceleration_due_to_gravity() * np.power(ts, 2)
    axs.plot(xs, ys, ':g', label="Closed form")
    axs.set_title(f"Parabolic motion, 0-{total_time} s")
    axs.legend()


# TODO: Play around with delta t and see what happens
#   Make delta really big - what happens?
#   Make delta really small and add lots of time steps - what happens?
if __name__ == '__main__':
    # Time step
    # TODO: Try a very big delta t, and also a tiny one (but pick the number of time steps so that the total time
    #   is still 1 second)
    # delta_t = 0.1, n time steps 10 and delta_t = 0.001, n time steps 1000
    delta_t = 0.01

    pose_initial = np.array([0.0, 10.0])  # meters
    vel_initial = np.array([0.5, 4.0])  # meters/second

    pose_new, vel_new = compute_next_position_and_velocity(pos=pose_initial, vel=vel_initial, delta_t=delta_t)
    print(f"Checking pose new {pose_new}, vel new {vel_new}")

    # Using default value of number of time steps
    ret_poses = calculate_n_time_steps(pos_initial=pose_initial, vel_initial=vel_initial, delta_t=delta_t)
    n_time_steps = ret_poses.shape[1]

    #delta_t = 0.1
    #n_time_steps = 10
    #ret_poses = calculate_n_time_steps(pos_initial=pose_initial, vel_initial=vel_initial, delta_t=delta_t, n_time_steps=n_time_steps)

    total_time = delta_t * n_time_steps
    plot_results(ret_poses, vel_initial, total_time)
    print("Done")

