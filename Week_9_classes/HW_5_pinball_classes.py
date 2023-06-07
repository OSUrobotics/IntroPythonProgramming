#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


# ----------------------- Pinball Classs ---------------------------
#
# One more class - the pinball class that does the simulation
#
# In this homework you'll take the classes you created in the lecture activity and lab (PinballWall and PinballBumper)
#  and use them in a class that wraps up the entire simulation (PinballClass)

# You can import classes just like you import functions
#  To make this work, copy your class definition from your .ipynb file to the corresponding .py file
#   (or make a new file with both the classes in it)
from lec_act_9_class_pinball_wall import PinballWall
from Lab_9_class_pinball_bumper import PinballBumper


class Pinball:
    """ Walls and bumpers for a rather boring pinball game"""
    def __init__(self, left, right, height, delta_t=0.01):
        """ Just set size of pinball box - assumes floor is y = 0
        Note: We'll add the walls and bumpers later - but we're going to create the variables we need here
        (It's very bad form to add new variables later) """
        self.left = left
        self.right = right
        self.height = height

        # What delta t to use
        self.delta_t = delta_t

        # If you're doing drag...
        self.do_drag = False

        # We're going to add any walls/bumpers here
        self.obstacles = []

        # For storing the path
        self.poses = None
        self.velocities = None

    @staticmethod
    def acceleration_due_to_gravity():
        """Somewhat silly - but if we need to change it, then we can  change it just here
        Note the static method tag - this says we don't need a self pointer"""
        gravity = -9.8     # m/s
        return gravity

    def add_obstacle(self, obstacle):
        """ Add in a bumper or wall
        @param obstacle - an instance of a bumper or a wall"""
        # Putting this as a separate method because it works better to make and add then try to pass everything
        #  into the init function. More sophisticated versions would also allow removing/changing obstacles
        self.obstacles.append(obstacle)

    def _compute_next_step(self, current_state):
        """ How to compute the next position and velocity from this one
        Note that I'm passing in current state and returning next here, rather than storing and updating an internal
        variable. This makes it clearer what the method does
        The _ in front of the method signals to someone using this class that this method is "private" and probably
        shouldn't be called
        @param current_state - the pose (x, y) and velocity (vx, vy) and acceleration (ax, ay) as a numpy array
        @return the new position, velocity as a tuple"""

        # TODO: Copy in your compute next step from pinball_routines. The only thing you should have to change is that
        #  you're now going to get delta t from self instead of passing it in
        result = np.zeros(current_state.shape)
# YOUR CODE HERE

        return result

    def simulate_pinball(self, starting_state):
        """ Call compute one time step multiple times and store it in a numpy array
        This should be your simulate code, again with delta_t and do_drag replaced with self.delta_t, as well
        as compute_next_step
        @param starting_state - the starting position, velocity, acceleration
        @return position & velocity values as two 2xtimesteps numpy array
        """

        # TODO - put your simulate function here. Only pass in the starting state - the remainder of the
        #  data you use to pass in should be in the self. pointer

        # The returned array.We do not know the size, so do not pre-allocate
        self.poses = []
        self.velocities = []

        # Use a while loop instead of the for loop
        # Set the stopping criteria based on current state y value
        # We know the first pose is the initial one
        # Notice that the poses are being stored in the self variable
        # TODO STEP 2 Use this code to do the inside/outside & reflect for each wall
            # This should work, and will replace your if/then code for walls and bumpers, if your classes are
            #   implemented correctly
            # for o in self.obstacles:
            #     if o.outside(current_state[0, :]):
            #         pt_back, vel_back = o.reflect(current_state[0, :], current_state[1, :])
            #         current_state[0, :] = np.array(pt_back).transpose()
            #         current_state[1, :] = np.array(vel_back).transpose()

# YOUR CODE HERE
        # It's ok to return the self results
        return self.poses, self.velocities

    def plot_pinball_hw(self):
        """ plot the results of running the system AND the "correct" closed form result
        Note that everything we need is already in the class
        """
        nrows = 1
        ncols = 1
        fig, axs = plt.subplots(nrows, ncols, figsize=(4, 4))

        # The values we calculated in calculate_n_time_steps
        axs.plot([self.left, self.right], [self.height, self.height], color='gray', linestyle='dotted')
        axs.plot([self.left, self.right], [0, 0], color='gray', linestyle='dotted')
        axs.plot([self.left, self.left], [0, self.height], color='gray', linestyle='dotted')
        axs.plot([self.right, self.right], [0, self.height], color='gray', linestyle='dotted')

        # Again, this should work if your wall and bumper plots are correct
        for o in self.obstacles:
            o.plot(axs, self.left, self.right, self.height)

        axs.plot(self.poses[0, 0], self.poses[1, 0], 'xr', label="Start")
        axs.plot(self.poses[0, :], self.poses[1, :], '.-k', label="Poses")

        axs.axis('equal')
        axs.set_title(f"Not so boring pinball, 0-{self.delta_t * self.poses.shape[0]} s")


if __name__ == '__main__':
    # Create the pinball class
    #   Use: left -5.0, right 5.0, height 10.0, delta_t 0.01
# YOUR CODE HERE

    # Now create and add any obstacles
    # Required: Side walls at -4.5, 4.5 and top at 9.5
    # Required: At least one bumper
# YOUR CODE HERE

    # Now run a simulation
    #  setup
    starting_state = np.zeros([3, 2])  # location, velocity, acceleration
    starting_state[0, :] = [0, 0] # Start at zero, zero
    # Velocity - mostly up with a bit of x noise
    starting_state[1, :] = [2.4, 15.5]
    starting_state[2, :] = [0.0, pinball.acceleration_due_to_gravity()]

    # Run the simulation
# YOUR CODE HERE

    # ... and plot the results
    pinball.plot_pinball_hw()

    print("Done")
