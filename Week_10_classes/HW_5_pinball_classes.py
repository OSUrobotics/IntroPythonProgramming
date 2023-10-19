#!/usr/bin/env python3

import numpy as np
# This bit of crazy code ensures that we can access the files in Week_5_matrices
import os 
import sys
if "Week_5_matrices" not in sys.path:
    save_path = os.getcwd()
    os.chdir("..")
    sys.path.append(f'{os.getcwd()}/Week_5_matrices')
    os.chdir(save_path)


# ----------------------- Pinball Classs ---------------------------
#
# In this homework you'll take the classes you created in the lecture activity and lab (PinballWall and PinballBumper)
#  and use them in a class that wraps up the entire simulation (Pinball)
#
# We'll import the classes just like we've imported functions. There are 3 classes to import, the two you did
#  already (PinballWall and PinballBumper) as well as the one you'll be editing (Pinball).
#
# Slides: https://docs.google.com/presentation/d/1DCSykIMBSlzCNNnmUcxPqfGxJmeGYd-7LF_W_-_7fUU/edit?usp=sharing
from pinball_wall import PinballWall
from pinball_bumper import PinballBumper
from pinball import Pinball


if __name__ == '__main__':
    # Create an instance of the pinball class
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
    starting_state[1, :] = [3.5, 15.5]
    starting_state[2, :] = [0.0, pinball.acceleration_due_to_gravity()]

    # Run the simulation
# YOUR CODE HERE

    # ... and plot the results
    pinball.plot_pinball_hw()

    print("Done")
