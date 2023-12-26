#!/usr/bin/env python3

# The usual imports
import numpy as np
import matplotlib.pyplot as plt


# These are the routines used in the lab and/or you need to fill in for the homework (lab 5, week 5)
from arm_routines import get_matrices_all_links, create_arm_geometry, set_angles_of_arm_geometry, get_gripper_location, plot_complete_arm

# These are the routines used in the lab and/or you need to fill in for the homework (lab 6, week 6)
from arm_optimization_routines import distance_to_goal, do_fmin


# ----------------- Checks --------------------------
# Check/debug/plot routines for week 5 (forward kinematics)
def forward_kinematics_check():
    # Create the arm geometry
    base_size_param = (1.0, 0.5)
    link_sizes_param = [(0.5, 0.25), (0.3, 0.1), (0.2, 0.05)]
    palm_width_param = 0.1
    finger_size_param = (0.075, 0.025)

    # This function calls each of the set_transform_xxx functions, and puts the results
    # in a list (the gripper - the last element - is a list) (Lab 5)
    arm_geometry = create_arm_geometry(base_size_param, link_sizes_param, palm_width_param, finger_size_param)

    ## Check the combined link/gripper/finger rotations
    # Several different angles to check your routines with
    angles_none = [0.0, 0.0, 0.0, [0.0, 0.0, 0.0]]
    angles_check_link_0 = [np.pi/4, 0.0, 0.0, [0.0, 0.0, 0.0]]
    angles_check_link_0_1 = [np.pi/4, -np.pi/4, 0.0, [0.0, 0.0, 0.0]]
    angles_check_wrist = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [np.pi/3.0, 0.0, 0.0]]
    angles_check_fingers = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [0.0, np.pi/4.0, -np.pi/4.0]]

    # The check below is for angles_check
    angles_check = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [np.pi/3.0, np.pi/4.0, -np.pi/4.0]]
    set_angles_of_arm_geometry(arm_geometry, angles_check)
    matrices = get_matrices_all_links(arm_geometry)

    mat_check_base = np.identity(3)
    assert(np.all(np.isclose(matrices[0], mat_check_base, atol=0.01)))

    mat_check_link_1 = np.array([[ 0.0, -1.0,  0.0], [ 1.0,  0.0,  0.5], [ 0.0,  0.0,  1.0]])
    assert(np.all(np.isclose(matrices[1], mat_check_link_1, atol=0.01)))

    mat_check_link_2 = np.array([[ -1.0, 0.0,  -0.5], [ 0.0,  -1.0,  0.5], [ 0.0,  0.0,  1.0]])
    assert(np.all(np.isclose(matrices[2], mat_check_link_2, atol=0.01)))

    mat_check_wrist = np.array([[ 1.0, 0.0,  -0.5121], [ 0.0, 1.0,   0.7121], [ 0.0,  0.0,  1.0]])
    assert(np.all(np.isclose(matrices[-1], mat_check_wrist, atol=0.01)))

    # Check the gripper function
    angles_gripper_check = [np.pi/3, -np.pi/6, 3.0 * np.pi/6, [-np.pi/4, np.pi/4.0, -np.pi/4.0]]

    # Set the angles
    set_angles_of_arm_geometry(arm_geometry, angles_gripper_check)
    grasp_loc = get_gripper_location(arm_geometry)

    print(f"Grasp loc is {grasp_loc}, expected (-0.8106, 0.92437)")
    assert(np.isclose(grasp_loc[0], -0.8106, atol=0.01) and np.isclose(grasp_loc[1], 0.92437, atol=0.01))

    # Now actually plot - the grasper grip location should show up as a green cross
    fig, axs = plt.subplots(1, 1, figsize=(8, 8))
    plot_complete_arm(axs, arm_geometry, matrices)


# Check routines for week 6 (optimization)
def optimization_check():
    # Create the arm geometry
    base_size_param = (1.0, 0.5)
    link_sizes_param = [(0.5, 0.25), (0.3, 0.1), (0.2, 0.05)]
    palm_width_param = 0.1
    finger_size_param = (0.075, 0.025)

    arm_geometry = create_arm_geometry(base_size_param, link_sizes_param, palm_width_param, finger_size_param)

    # Set the angles of the arm
    angles_start = [np.pi/6.0, -np.pi/4, 1.5 * np.pi/4, [np.pi/3.0, -np.pi/8.0, np.pi/6.0]]
    set_angles_of_arm_geometry(arm_geometry, angles_start)

    # Do the optimization
    target = np.array([0.55, 1.15])
    angles_optimized = do_fmin(angles_start, arm_geometry, target)

    # Make sure the angles of the arm are set to the optimized one
    set_angles_of_arm_geometry(arm_geometry, angles_optimized)

    # Check that this is close to zero
    d_to_target = distance_to_goal(arm_geometry, target)
    print(f"Distance to goal {d_to_target}, should be 0.00441")

    # Plot arm with target
    fig, axs = plt.subplots(1, 1, figsize=(8, 8))
    plot_complete_arm(axs, arm_geometry, get_matrices_all_links(arm_geometry))
    axs.plot(target[0], target[1], '+g', markersize=20)


def generalization_check():
    # Create the arm geometry
    base_size_param = (0.5, 0.25) # squished
    link_sizes_param = [(0.3, 0.15), (0.2, 0.09), (0.1, 0.05), (0.075, 0.03)]
    palm_width_param = 0.15
    finger_size_param = (0.085, 0.015)


    # This function calls each of the set_transform_xxx functions, and puts the results
    # in a list (the gripper - the last element - is a list)
    arm_geometry = create_arm_geometry(base_size_param, link_sizes_param, palm_width_param, finger_size_param)

    # Set the angles of the arm
    angles_start = [-np.pi/4.0, -np.pi/4, 1.2 * np.pi/4, -1 * np.pi/8, [-np.pi/3.0, np.pi/6.0, -np.pi/6.0]]
    set_angles_of_arm_geometry(arm_geometry, angles_start)

    target = np.array([0.3, -0.25])

    # Plot arm with target
    fig, axs = plt.subplots(1, 1, figsize=(8, 8))
    plot_complete_arm(axs, arm_geometry, get_matrices_all_links(arm_geometry))
    axs.plot(target[0], target[1], '+g', markersize=20)

    # Do the optimization
    angles_optimized = do_fmin(angles_start, arm_geometry, target)
    set_angles_of_arm_geometry(arm_geometry, angles_optimized)
    plot_complete_arm(axs, arm_geometry, get_matrices_all_links(arm_geometry))


if __name__ == '__main__':
    # For week 5
    forward_kinematics_check()

    # For week 6
    optimization_check()

    # Generalization check
    generalization_check()

    print("Done")
