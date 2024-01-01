#!/usr/bin/env python3

# The usual imports
import numpy as np
from scipy.optimize import fmin
import sys
import os

# This bit of crazy code ensures that we can access the routines in arm_optimization_routines 
if "Week_6_matrices" not in sys.path:
    save_path = os.getcwd()
    os.chdir("..")
    sys.path.append(f'{os.getcwd()}/Week_6_matrices')
    os.chdir(save_path)


# These are the routines used in the lab and/or you need to fill in for the homeowrk
from arm_routines import set_angles_of_arm_geometry, get_gripper_location


# ----------------- Helper functions for joint angles --------------------------
def copy_angles(angles):
    """ Make a copy of the angles - just sort of annoying because of the list with lists, so do it once here
    @param angles
    @return copy of angles in a new list structure"""

    # Copy the link angles
    angles_ret = []
    for a in angles[:-1]:
        angles_ret.append(0)

    # Copy the wrist and finger angles
    angles_ret.append([])
    for wa in angles[-1]:
        angles_ret[-1].append(wa)


def angles_list_to_numpy(angles):
    """ Extract the arm and wrist angles
    @param angles
    @return numpy array with angles"""

    # Copy the link angles
    angles_as_numpy = np.zeros(len(angles))
    for i, a in enumerate(angles[0:-1]):
        angles_as_numpy[i] = a
    # and the wrist angle
    angles_as_numpy[-1] = angles[-1][0]

    return angles_as_numpy


def angles_numpy_to_list(angles_as_numpy, top_finger=0, bot_finger=0):
    """ Convert back to a list
    @param angles_as_numpy,
    @param top_finger optional finger
    @param bot_finger optional finger
    @return angles as list"""
    angles_ret = []
    for i, a in enumerate(angles_as_numpy[:-1]):
        angles_ret.append(a)
    angles_ret.append([])
    angles_ret[-1].append(angles_as_numpy[-1])
    angles_ret[-1].append(top_finger)
    angles_ret[-1].append(bot_finger)

    return angles_ret

# -------------------- Distance calculation --------------------
# Whether you're doing gradient descent or IK, you need to know the vector and/or distance from the current
#  grasp position to the target one. I've split this into two functions, one that returns an actual vector, the
#  second of which calls the first then calculates the distance. This is to avoid duplicating code.
def vector_to_goal(arm_with_angles, target):
    """
    Calculate the grasp pt for the current arm configuration. Return a vector going from the grasp pt to the target
    @param arm_with_angles - The arm geometry, as constructed in arm_forward_kinematics
    @param target - a 2x1 numpy array (x,y) that is the desired target point
    @return - a 2x1 numpy array that is the vector (vx, vy)
    """
    # TODO:
    #   Get the gripper/grasp location using get_gripper_location
    #   Calculate and return the vector
    # BEGIN SOLUTION
    end_pt = get_gripper_location(arm_with_angles)

    return np.array(target) - np.array(end_pt)
    # END SOLUTION


def distance_to_goal(arm_with_angles, target):
    """
    Length of vector - this function is zero when the gripper is at the target location, and gets bigger
    as the gripper moves away
    Note that, for optimization purposes, the distance squared works just as well, and will save a square root - but
    for the checks I'm using distance.
    @param arm_with_angles - The arm geometry, as constructed in arm_forward_kinematics
    @param target - a 2x1 numpy array (x,y) that is the desired target point
    @return: The distance between the gripper loc and the target
    """

    # TODO: Call the function above, then return the vector's length
    # BEGIN SOLUTION
    vec = vector_to_goal(arm_with_angles, target)

    return np.sqrt(vec[0] * vec[0] + vec[1] * vec[1])
    # END SOLUTION


def func_for_fmin(angles_from_fmin, arm, target):
    """Move the arm to the given angles then calculate distance to target
    @param angles_from_fmin - angles from fmin (only arm angles, no fingers)
    @param arm - the arm geometry
    @param target - the target point
    @return distance to goal"""

    # TODO:
    #  1: Fill in angles_fill_in with the angles from fmin
    #    Note: optional version sets wrist angle as well as arm links
    #    Finger angles should be zero
    #  2: Use set_angles_of_arm_geometry to set the joint angles of the arm
    #  3: Return the distance to the target
    # See the angles_to_list helper function
    # BEGIN SOLUTION
    set_angles_of_arm_geometry(arm, angles_numpy_to_list(angles_from_fmin))
    return distance_to_goal(arm, target)
    # END SOLUTION
    return 0.0


def do_fmin(angles_start, arm, target):
    """Run fmin with the target, given the starting angles
    @param angles_start - angles to start with
    @param arm - the arm geometry
    @param target - the target point
    @return new angles"""

    # This creates a new list from angles_start that has the same values (and structure) as angles_start
    #  Remember that thw wrist + finger angles are stored as a triplet at the end
    angles_ret = copy_angles(angles_start)

    # TODO:
    #  1. Set up the initial angles for fmin. This is either the arm link angles or the (optional) link angles plus
    #  the wrist angle. Use the angles in angles_gripper_check
    #  2. Call fmin with those angles and func_for_fmin.
    #  3. There is an optional args parameter for fmin that works very similarly to the optional arguments we used
    #  in ode solve - this is how you will pass in the arm geometry and the target point
    #  4. Copy the angles returned from fmin into angles_ret
    #  See angles_to_list and list_to_angles helper functions
    # BEGIN SOLUTION
    angles_for_fmin = angles_list_to_numpy(angles_start)
    angs_at_min = fmin(func_for_fmin, x0=angles_for_fmin, args=(arm, target))
    angles_ret = angles_numpy_to_list(angs_at_min, angles_start[-1][1], angles_start[-1][2])
    # END SOLUTION
    return angles_ret

