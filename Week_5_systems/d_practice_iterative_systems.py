#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# ----- iterative systems (using functions) ----------
# Do the parabolic flight again, but write the code yourself, this time
# 1) keep both the position and the velocity at all time steps
#
# You're free, obviously, to copy code from the practice script, but try to write it yourself, first

# Just to have
def acceleration_due_to_gravity():
    """Somewhat silly - but if we need to change it, then we can  change it just here"""
    gravity = -9.8     # m/s
    return gravity  # kg m/s


# TODO your compute_next_position_and_velocity and calculate_n_time_steps functions here - call from
#  if __name__ at the bottom of the file

# Your compute_next_position_and_velocity should do the same thing as the tutorial script
# TODO: Modify calculate_n_time_steps to store a 4xn np array instead of a 2xn
#   Change the size of the array
#   (Before the for loop) copy the velocity into the array along with the pose
#   In the for loop, copy the new velocity into the array along with the new pose

# Optional: Go until you hit the ground
#  Modify calculate_n_time_steps to loop until the new pose y value is less than zero
# TODO: Since you don't know the size of the arrays in advance, better to use two lists, one for the pose, and
#  one for the velocity.
#    Create the lists and set the first elements to be initial pose and velocity, respectively
#    Modify the for loop to be a while loop that stops when the new pose has a y value < 0. I like to do this
#    with
#        b_done = False
#        while not b_done:
#             ... set b_done to be true when y < 0
# After the while loop you will know how big the return array should be. Create the array then copy the list values
#  in. Note: np.array(list) creates a numpy array from the list.

# This time we'll draw the poses and the velocities at each time step (but no closed form)
def plot_results(ret_poses, ret_velocities):
    """ plot the results of running the system
    @param ret_poses - x y position values in a 2xn numpy array
    @param ret_velocities - vx, vy values in a 2xn numpy array
    @return Nothing
    """
    nrows = 1
    ncols = 1
    fig, axs = plt.subplots(nrows, ncols, figsize=(4, 4))

    # The values we calculated in calculate_n_time_steps
    axs.plot(ret_poses[0, :], ret_poses[1, :], '-k', label="Poses")

    # This one's a bit trickier because we need to plot the arrows at each time step. Turns out there's a function
    # (quiver) that will do that for us...
    axs.quiver(ret_poses[0, :], ret_poses[1, :], ret_velocities[0, :], ret_velocities[1, :], color='magenta', label="Velocities")

    axs.set_title(f"Parabolic motion")
    axs.legend()


# --------------------------------- answers ------------------------
# This function should be the same as tge tutorial
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


# I chose to return the results in a 4xn array, instead of two 2xn arrays. Either works; somewhat clearer to return
#  two arrays (since you can name them) but somewhat easier to use downstream if it's one array
def calculate_n_time_steps(pos_initial, vel_initial, delta_t=0.1, n_time_steps=100):
    """ Call compute one time step multiple times and store it in a numpy array
    @param pos_initial - the starting x,y position (numpy array)
    @param vel_initial - the starting vx, vy velocity (numpy array)
    @param delta_t - the time step to use. Define a default t value that you've determined works well
    @param n_time_steps - how many time steps to take. Again, default to a reasonable number
    @return x, y, vx, vy values as a 4xtimesteps numpy array
    """

    # The returned array. We know the size, so we can pre-allocate it
    ret_pose_all = np.zeros((4, n_time_steps))
    # We know the first pose is the initial one - note 0:2 and 2:4 to do the 1st/2nd rows and 3rd/4th ones
    ret_pose_all[0:2, 0] = pos_initial
    # Put the initial velocity in as well
    ret_pose_all[2:4, 0] = vel_initial

    # Note the start from 1 - you already know what the values for 0 should be
    for i in range(1, n_time_steps):
        # Make sure to use the last x,y values you just computed
        pos_next, vel_next = compute_next_position_and_velocity(ret_pose_all[0:2, i-1], ret_pose_all[2:4, i-1], delta_t=delta_t)

        # Put the new values into the numpy array
        ret_pose_all[0:2, i] = pos_next
        ret_pose_all[2:4, i] = vel_next

    # All done - return the numpy array
    return ret_pose_all


# Optional - go until you hit the ground
# In this version, instead of using a for loop, it's a while loop, and you will NOT know ahead of time how
#  big the array is. Simplest option is to use a list and then convert to a numpy array at the end
def calculate_until_hit_ground(pos_initial, vel_initial, delta_t=0.1):
    """ Call compute one time step multiple times and store it in a numpy array
    @param pos_initial - the starting x,y position (numpy array)
    @param vel_initial - the starting vx, vy velocity (numpy array)
    @param delta_t - the time step to use. Define a default t value that you've determined works well
    @return x, y, vx, vy values as a 4xtimesteps numpy array
    """

    # The returned array(s). We do NOT know the array size, so use a list and set the first element to be the
    #   pose and velocity. Easier to use two lists.
    ret_pose_list = [pos_initial]
    ret_velocity_list = [vel_initial]

    # I just like this format - then in the code you just set b_done to be True when you reach the stopping condition
    b_done = False
    i_count_explode = 0 # Safety check
    while not b_done and i_count_explode < 10000:
        # Make sure to use the last x,y values you just computed
        pos_next, vel_next = compute_next_position_and_velocity(ret_pose_list[-1], ret_velocity_list[-1], delta_t=delta_t)

        # Put the new values into the lists
        ret_pose_list.append(pos_next)  # this will be the ret_pose_list[-1] in the next interation
        ret_velocity_list.append(vel_next)

        if pos_next[1] < 0:
            b_done = True

        i_count_explode += 1 # belt and suspenders...

    # Ooops - let the caller know something went wrong, probably
    if not b_done:
        raise(ValueError, f"Did not hit the ground in 10,000 steps: p={pos_initial}, v={vel_initial}, dt {delta_t}")

    # All done - create a numpy array and set the first two rows and second two rows
    #   Transpose to go from nx2 to 2xn
    ret_pos_all = np.zeros((4, len(ret_pose_list)))
    ret_pos_all[0:2, :] = np.array(ret_pose_list).transpose()
    ret_pos_all[2:4, :] = np.array(ret_velocity_list).transpose()
    return ret_pos_all


# Calling code for answers
def check_version_one():
    # Time step
    delta_t = 0.1
    n_time_steps = 10

    pose_initial = np.array([0.0, 10.0])  # meters
    vel_initial = np.array([0.5, 4.0])  # meters/second

    # Using default value of number of time steps
    ret_poses = calculate_n_time_steps(pos_initial=pose_initial, vel_initial=vel_initial, delta_t=delta_t, n_time_steps=n_time_steps)

    plot_results(ret_poses[0:2, :], ret_poses[2:4, :])
    print("Done")


# Calling code for answers
def check_version_two():
    # Time step
    delta_t = 0.1

    pose_initial = np.array([0.0, 10.0])  # meters
    vel_initial = np.array([0.5, 4.0])  # meters/second

    # Using default value of number of time steps
    ret_poses = calculate_until_hit_ground(pos_initial=pose_initial, vel_initial=vel_initial, delta_t=delta_t)

    plot_results(ret_poses[0:2, :], ret_poses[2:4, :])
    print("Done")


# TODO: Call your function here
if __name__ == '__main__':
    # Time step
    delta_t = 0.1
    n_time_steps = 10

    pose_initial = np.array([0.0, 10.0])  # meters
    vel_initial = np.array([0.5, 4.0])  # meters/second

    # TODO: Pass values to your function
    # ret = my_calc_n_time_steps - takes in initial pose, velocity, delta t, and number of time steps

    # TODO: Pass the results to the plotting function
    # plot_results(ret_poses[0:2, :], ret_poses[2:4, :])

    # Test the answer code
    # check_version_one()
    # check_version_two()
    print("Done")
