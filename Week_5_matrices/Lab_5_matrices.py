#!/usr/bin/env python3

# The usual imports
import numpy as np
import matplotlib.pyplot as plt

# The matrix routines
import matrix_routines as mt

# These are the routines used in the lecture activity - we'll re-use them here
from object_routines import read_object, plot_object_in_world_coord_system

# These are the routines you'll be editing/using - they're in arm_routines.py
from arm_routines import get_rotation_link, get_matrix_finger, get_transform_base, get_transform_link, get_transform_palm, \
    get_transform_finger, create_arm_geometry, set_angles_of_arm_geometry, plot_arm_components

# --------------------------- Forward kinematics ------------------
# The goal of the lab is to use matrices to position a robot arm in space. In the lab we'll just
#  position each component independently and rotate them by angles (steps 1 and 2 in the slides)
#
# Slides: https://docs.google.com/presentation/d/1Ut5RnIKU8DF8k_joGXp4tJ1FzBKNIX8JYRE9wkIP_qE/edit?usp=sharing
#
# The majority of the code for this assignment is in arm_routines.py. The code here does the testing
#


# ----------------- Multiple examples to practice with --------------------------
def check_return_values():
    base_size_param = (1.0, 0.5)
    link_sizes_param = [(0.5, 0.25), (0.3, 0.1), (0.2, 0.05)]
    palm_width_param = 0.1
    finger_size_param = (0.075, 0.025)

    np.set_printoptions(precision=4, floatmode='fixed')

    mat_base = get_transform_base(base_size_param[0], base_size_param[1])
    mat_base_check = np.array([[0, -0.5, 0], [0.25, 0.0, 0.25], [0.0, 0.0, 1.0]])
    print(mat_base_check)
    assert(np.all(np.isclose(mat_base, mat_base_check)))

    mat_link1 = get_transform_link(link_sizes_param[0][0], link_sizes_param[0][1])
    print(mat_link1)
    mat_link1_check = np.array([[0.25, 0.0, 0.25], [0.0, 0.125, 0.0], [0.0, 0.0, 1.0]])
    assert(np.all(np.isclose(mat_link1, mat_link1_check)))

    mat_palm = get_transform_palm(palm_width_param)
    print(mat_palm)
    mat_palm_check = np.array([[0.005, 0.0, 0.0], [0.0, 0.05, 0.0], [0.0, 0.0, 1.0]])
    assert(np.all(np.isclose(mat_palm, mat_palm_check)))

    mat_finger_top = get_transform_finger(palm_width_param, finger_size_param, True)
    print(mat_finger_top)
    mat_finger_top_check = np.array([[0.0375, 0.0, 0.0375], [0.0, 0.0125, 0.05], [0.0, 0.0, 1.0]])
    assert(np.all(np.isclose(mat_finger_top, mat_finger_top_check)))

    mat_finger_bot = get_transform_finger(palm_width_param, finger_size_param, False)
    mat_finger_bot_check = np.array([[0.0375, 0.0, 0.0375], [0.0, 0.0125, -0.05], [0.0, 0.0, 1.0]])
    assert(np.all(np.isclose(mat_finger_bot, mat_finger_bot_check)))
    print(mat_finger_bot)


def check_matrix_from_angle_values():
    base_size_param = (1.0, 0.5)
    link_sizes_param = [(0.5, 0.25), (0.3, 0.1), (0.2, 0.05)]
    palm_width_param = 0.1
    finger_size_param = (0.075, 0.025)

    angles_check = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [np.pi/3.0, np.pi/4.0, -np.pi/4.0]]

    np.set_printoptions(precision=4, floatmode='fixed')

    arm_geometry = create_arm_geometry(base_size_param, link_sizes_param, palm_width_param, finger_size_param)
    set_angles_of_arm_geometry(arm_geometry, angles_check)

    # Check the rotation matrix for the first link
    mat_rot_link1 = get_rotation_link(arm_geometry[1])
    print(mat_rot_link1)
    mat_rot_link1_check = np.array([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
    assert(np.all(np.isclose(mat_rot_link1, mat_rot_link1_check)))

    # Check the rotation matrix for the top finger (optional)
    mat_rot_top_finger = get_matrix_finger(arm_geometry[-1][1])
    print(mat_rot_top_finger)
    mat_rot_top_finger_check = np.array([[0.7071, -0.7071, 0.0354], [0.7071, 0.7071, 0.0146], [0.0, 0.0, 1.0]])
    assert(np.all(np.isclose(mat_rot_top_finger, mat_rot_top_finger_check, atol=0.3)))

    mat_rot_bot_finger = get_matrix_finger(arm_geometry[-1][2])
    print(mat_rot_bot_finger)
    mat_rot_bot_finger_check = np.array([[0.7071, 0.7071, 0.0354], [-0.7071, 0.7071, -0.0146], [0.0, 0.0, 1.0]])
    assert(np.all(np.isclose(mat_rot_bot_finger, mat_rot_bot_finger_check, atol=0.3)))


if __name__ == '__main__':
    # Checks step 1
    check_return_values()

    # Checks step 2
    check_matrix_from_angle_values()

    # Step 1 - create the arm geometry
    base_size_param = (1.0, 0.5)
    link_sizes_param = [(0.5, 0.25), (0.3, 0.1), (0.2, 0.05)]
    palm_width_param = 0.1
    finger_size_param = (0.075, 0.025)

    # This function calls each of the set_transform_xxx functions, and puts the results
    # in a list (the gripper - the last element - is a list)
    arm_geometry = create_arm_geometry(base_size_param, link_sizes_param, palm_width_param, finger_size_param)
    if len(arm_geometry) != 5:
        print("Wrong number of components, should be 5, got {len(arm_geometry)}")
    if len(arm_geometry[-1]) != 3:
        print("Wrong number of gripper components, should be 3, got {len(arm_geometry[-1])}")

    # Should show all 5 components, the base, 3 links, and the gripper
    # Step 1 - note, comment out this one if you don't want both drawn on top of each other when you do step 2
    fig, axs = plt.subplots(1, len(arm_geometry), figsize=(4 * len(arm_geometry), 4))
    plot_arm_components(axs, arm_geometry)

    # Step 2 - rotate each link element in its own cooridinate system
    # Several different angles to check your results with
    angles_none = [0.0, 0.0, 0.0, [0.0, 0.0, 0.0]]
    angles_check_fingers = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [0.0, np.pi/4.0, -np.pi/4.0]]
    angles_check_wrist = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [np.pi/3.0, 0.0, 0.0]]
    angles_check = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [np.pi/3.0, np.pi/4.0, -np.pi/4.0]]
    set_angles_of_arm_geometry(arm_geometry, angles_check)
    fig2, axs2 = plt.subplots(1, len(arm_geometry), figsize=(4 * len(arm_geometry), 4))
    plot_arm_components(axs2, arm_geometry, b_with_angles=True)


    print("Done")
