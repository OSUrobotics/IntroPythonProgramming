#!/usr/bin/env python3

# The usual imports
import numpy as np

# ----------------- function for fmin --------------------------
#
# Write the function that will be passed to fmin
#
# Slides https://docs.google.com/presentation/d/1m-8UphLgGLVaDKKcZ-NA_ejgOFlkD1Rlz3_sW0fHBM8/edit?usp=sharing

# Routines from HW 3, Lab 5
# These are the routines used in the lab and/or you need to fill in for the homework (lab 5, week 5)
from arm_routines import create_arm_geometry, set_angles_of_arm_geometry, get_gripper_location

# These are the routines used in the lab and/or you need to fill in for the homework (lab 6, week 6)
from arm_optimization_routines import vector_to_goal, distance_to_goal, func_for_fmin, angles_list_to_numpy


# ----------------- Checks --------------------------

# Check routines for week 6 (optimization)
def optimization_check():
    # Create the arm geometry
    base_size_param = (1.0, 0.5)
    link_sizes_param = [(0.5, 0.25), (0.3, 0.1), (0.2, 0.05)]
    palm_width_param = 0.1
    finger_size_param = (0.075, 0.025)

    arm_geometry = create_arm_geometry(base_size_param, link_sizes_param, palm_width_param, finger_size_param)

    # Set the angles of the arm
    angles_gripper_check = [np.pi/6.0, -np.pi/4, 1.5 * np.pi/4, [np.pi/3.0, -np.pi/8.0, np.pi/6.0]]
    set_angles_of_arm_geometry(arm_geometry, angles_gripper_check)

    # Get the gripper location
    x, y = get_gripper_location(arm_geometry)
    print(f"Gripper location ({x}, {y}), should be (-0.383, 1.323)")

    target = np.array([0.75, 1.25])
    vx, vy = vector_to_goal(arm_geometry, target)
    print(f"Vector to goal ({vx}, {vy}), should be (1.133, -0.073)")

    d_to_target = distance_to_goal(arm_geometry, target)
    print(f"Distance to goal {d_to_target}, should be 1.1353")

    # This is a helper function to convert the list of angles in angles_gripper into a numpy array, which is
    #  what fmin works with
    angles_numpy = angles_list_to_numpy(angles_gripper_check)
    check_dist = func_for_fmin(angles_numpy, arm_geometry, target)
    print(f"Check func for min {check_dist}, should be 1.1353")


if __name__ == '__main__':
    # For week 6
    optimization_check()
    print("Done")
