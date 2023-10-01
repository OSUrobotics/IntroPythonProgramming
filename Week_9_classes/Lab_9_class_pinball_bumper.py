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

# YOUR CODE HERE

# ------------------------ Lab 9 classes ------------------------------
#
# TODO: Create a class for your bumper.
# Code in pinball_bumper.py
# Slides: https://docs.google.com/presentation/d/172YYy0RNsGW4Gpruj3lejtBYuW0uTwZwjD-gMOrLYIc/edit?usp=sharing
#
from pinball_bumper import PinballBumper

# TODO: Create instance(s) of Bumper and check that they work
if __name__ == '__main__':

