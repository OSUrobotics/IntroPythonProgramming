#!/usr/bin/env python3

# The usual imports
import numpy as np
import matplotlib.pyplot as plt

# These are the routines used in the lecture activity - we'll re-use them here
import matrix_routines as mt
from object_routines import read_object, plot_object_in_world_coord_system

# --------------------------- Forward kinematics ------------------
# The goal of this part of the assignment is to use matrices to position a robot arm in space. In the lab we'll just
#  position each component independently and rotate them by angles
#
# Slides: https://docs.google.com/presentation/d/1Ut5RnIKU8DF8k_joGXp4tJ1FzBKNIX8JYRE9wkIP_qE/edit?usp=sharing
#



# ------------------ Step 1: Link transform matrices -------------------------------------
# Use matrices to take two basic shapes (a square and a wedge) and re-shape them into the geometry for the arm, gripper.
#
# Yes, you could just create these basic shapes with the "correct" XYs, but we'll use a matrix to transform the
# basic shape (square, wedge) to the correct size and shape.
#
# This is actually what most packages (eg, solidworks) do when you make a model. Each part of the model is defined
# in a "canonical" location, then transformed to the desired position/scale/rotation using a matarix. This is
# *before* calculating the matrix that positions the part based on the, eg, joint angles
#
# For all of these, you should be creating a matrix that consists of a scale followed by a rotate (maybe) followed by a translate
# See slides for what the resulting re-positioned shapes look like
# Wedge and Square are both -1,-1 to 1, 1 (you can open up the .json files to see what the vertex locations are)
def get_transform_base(base_width=1.0, base_height=0.5):
    """ Position and orient the base of the object
    Base middle should be at 0,0, wedge pointed up, base_width wide, base_height tall
    @param base_width - width of the base
    @param base_height - height of the base
    @return 3x3 matrix that positions the base as listed"""

    # TODO: create a matrix to get the wedge into the right position/size/orientation
    #  Scale first, then rotate, then translate
    # Open up Data/Wedge.json if you want to see the XYs (this shape is made in object_routines.py)
    # Reminder that all of the matrix creation functions are some form of
    #    mt.make_scale_matrix(sx, sy)  rotation and translation

    mat_return = np.identity(3)
# YOUR CODE HERE

    return mat_return


def get_transform_link(arm_length, arm_height):
    """ This is one of the arm components - since they're all kinda the same (just different sizes) just have
    one function to create them
    The arm should have the left hand side, middle at 0,0 and extend along the x_axis by length
    @param arm_length - the desired length of the arm
    @param arm_height - the desired height of the arm
    @return the 3x3 matrix"""

    # TODO: return the matrix that puts the link in the right position/size/orientation
    #  Reminder that squares are defined by -1,-1 to 1,1, and so currently have side lengths of 2...
    mat_return = np.identity(3)
# YOUR CODE HERE

    # Force recalculation of matrix
    return mat_return


def get_transform_palm(palm_width):
    """ This is palm of the gripper - a rectangle palm_width tall, centered at the origin, 1/10 as wide as it is tall
    @param palm_width - the desired separation of the two fingers
    @return the 3x3 matrix"""

    # TODO: Calculate the scale matrixthat makes the palm the correct size
    mat_return = np.identity(3)
# YOUR CODE HERE

    return mat_return


def get_transform_finger(palm_width, finger_size, b_is_top):
    """ This is one of the fingers - two wedges, separated by the palm width
    @param palm_width - the desired separation of the two fingers
    @param finger_size - tuple, how long and wide to make the finger
    @param b_is_top - is this the top or the bottom finger?
    @return the modified object"""

    # TODO [optional]: Calculate the transform to get it in the right position/size/orientation
    #  b_is_top means it's the top finger...
    mat_return = np.identity(3)
# YOUR CODE HERE

    return mat_return


def create_gripper(palm_width, finger_size):
    """ Make a gripper from a palm and two fingers
    Palm is centered on the x and y axis, base of finger will be at 0, 1/2 palm width
    @param palm_width - the desired separation of the two fingers
    @param finger_size - how long and wide to make the finger
    @return the modified object"""

    palm = read_object("Square")
    palm["Matrix"] = get_transform_palm(palm_width)
    palm["Grasp"] = finger_size[0] * 0.75
    # Keep this for later
    palm["Palm width"] = palm_width
    palm["Angle"] = 0  # Wrist angle
    palm["Color"] = "tomato"
    palm["Name"] = "Palm"

    # The gripper is a list of three elements - the fingers are optional
    gripper = [palm]
    for b in [True, False]:
        finger = read_object("Wedge")
        finger["Matrix"] = get_transform_finger(palm_width, finger_size, b)

        finger["Angle"] = 0.0
        if b:
            finger["Location"] = "Top"
            finger["Color"] = "darkgoldenrod"
        else:
            finger["Location"] = "Bottom"
            finger["Color"] = "darkgreen"

        finger["Name"] = f"Finger {finger['Location']}"

        # Keep this for later
        finger["Palm width"] = palm_width
        finger["Angle"] = 0
        gripper.append(finger)

    return gripper


def create_arm_geometry(base_size, link_sizes, palm_width, finger_size):
    """ Read in the square/wedge matrices, then call the set_transform_* functions to move them around
    See slides for what these should look like when done
    @param link_sizes: A list of tuples, one for each link, with the link length and width
    @param palm_width: The width of the palm (how far the fingers are spaced apart)
    @param finger_size: A tuple with the finger length and width
    @returns A list of the objects (arm_geometry)
    """

    # This is the base of the robot
    base = read_object("Wedge")
    base["Color"] = "darkturquoise"
    base["Name"] = "Base"
    base["Angle"] = 0.0

    # Here is where the matrix that moves the base (which is a wedge) to the right size/place is set
    base["Matrix "] = get_transform_base(base_size[0], base_size[1])

    # Keep the geometry in a list - start the list with the base object
    arm_geometry = [base]

    # Since arm links are kinda the same, just different sizes, create a list with the link sizes and make one
    #  component from each pair of sizes
    # Note that this makes it easy to add (or remove) links by just changing this list
    for i, size in enumerate(link_sizes):
        arm_link = read_object("Square")
        # Note that, because dictionaries are pointers and we edited square inside of set_transform, square and arm
        #   link point to the same thing after this call - which is why we'll read in a new copy of square on the
        #   next loop
        arm_link["Matrix"] = get_transform_link(size[0], size[1])
        arm_link["Name"] = f"Link {i}"

        # Add this version to our list of arm components
        arm_geometry.append(arm_link)

    # The gripper is made of Three pieces - we're going to put them all together (as a list) at the end of the list...
    #   This will make it possible to build the matrix for the gripper and apply that matrix to all gripper elements
    #   Note: Putting the fingers on is optional
    gripper = create_gripper(palm_width, finger_size)

    # Add the gripper as a single element to the end of the list
    arm_geometry.append(gripper)
    return arm_geometry


# ------------------ Step 2: Rotate each component by the given angle -------------------------------------
def get_rotation_link(arm_link):
    """ Compute JUST the rotation matrix for this link
    @param arm_link - the link as an object dictionary, angle stored in arm_link['Angle']
    @return 3x3 rotation matrix"""

    # TODO Create a rotation matrix based on the link's angle (stored with the key "Angle")
# YOUR CODE HERE
    return np.identity(3)


def get_matrix_finger(finger):
    """ Compute JUST the matrix that moves the finger to the correct angle
    Pulling this out as a method so we can use it elsewhere
    @param finger - the finger as an object dictionary
    @return a 3x3 matrix"""

    # TODO (optional):
    #   Translate the base of the finger back to the origin, rotate it, then translate it back out
    #   Reminder: The base of the finger can be found using mt.get_dx_dy_from_matrix
# YOUR CODE HERE
    return matrix


def set_angles_of_arm_geometry(arm_geometry, angles):
    """ Just sets the angle of each link, gripper
    Assumes that the arm has as many links as the angles and that the gripper is two objects at the end.
    There are three numbers for that last angle - a wrist angle, and one angle for each finger, stored as a list
    Not setting the base transformation
    @param arm_geometry - the arm geometry
    @param angles - the actual angles"""

    if len(arm_geometry) != len(angles) + 1:
        raise ValueError("Arm geometry and angles do not match")

    # Set angles of joints
    for comp, ang in zip(arm_geometry[1:-1], angles[0:-1]):
        comp["Angle"] = ang

    # Set angle of wrist and fingers
    #   Note that these are all dictionaries, so this is just a pointer to the last list element
    gripper = arm_geometry[-1]
    gripper[0]["Angle"] = angles[-1][0]
    for i, comp in enumerate(gripper):
        comp["Angle"] = angles[-1][i]


# ----------------- Plotting routines --------------------------

def plot_arm_components(axs, arm, b_with_angles=False):
    """ Plot each component in its own coordinate system with the matrix that was used to move the geometry
    @param axs are the axes of each plot window
    @param arm as a list of dictionaries, each of which is an object
    @param b_with_angles - if True, rotate the geometry by the given angle stored in the object """

    box = read_object("Square")
    box["Matrix"] = mt.make_scale_matrix(0.75, 0.75)
    box["Color"] = "lightgrey"

    # if b_with_angles is false, this stays the identity matrix for all plots
    rot_matrix = np.identity(3)

    # Plot the base and the arm links in their own windows
    for i, component in enumerate(arm[:-1]):
        plot_object_in_world_coord_system(axs[i], box)

        # TODO: if b_with_angles is True, sets the rotation matrix by the angle stored in the component
        #   You should call get_rotation_link to get the matrix
# YOUR CODE HERE

        plot_object_in_world_coord_system(axs[i], component, rot_matrix)
        axs[i].set_title(component["Name"])
        axs[i].plot(0, 0, 'xr')
        axs[i].axis("equal")

    # plot the gripper - I know it's more than one piece of geometry, so plot each in turn
    plot_object_in_world_coord_system(axs[-1], box)

    gripper = arm[-1]

    # Palm first
    palm = gripper[0]
    if b_with_angles:
        rot_matrix = get_rotation_link(palm)

    plot_object_in_world_coord_system(axs[-1], palm, rot_matrix)

    # Now the fingers
    for finger in gripper[1:]:
        # TODO (optional): Rotate each finger by the given amount, then rotate the entire gripper by the wrist angle
        # Step 1: Edit get_matrix_finger to get the matrix to move just the finger
        # Step 2: Multiply that matrix by the rotation matrix for the palm
# YOUR CODE HERE
        plot_object_in_world_coord_system(axs[-1], finger, rot_matrix)

    # Draw a red line for the palm and an x at the base of the wrist and another at the finger contact points

    # Get the y axis of the rotation matrix
    axs_x, axs_y = mt.get_axes_from_matrix(mt.make_rotation_matrix(palm["Angle"]))
    # Scale by palm width
    axs_y = axs_y * palm["Palm width"] / 2.0
    # Go from -vec to + vec
    axs[-1].plot([-axs_y[0], axs_y[0]], [-axs_y[1], axs_y[1]], '-r')

    # Draw a red + at the base of the palm
    axs[-1].plot(0, 0, '+r')

    # Draw a green x at the contact point of the fingers
    axs[-1].plot(axs_x[0] * palm["Grasp"], axs_x[1] * palm["Grasp"], 'xg')

    axs[-1].set_title("Gripper")
    axs[-1].legend(loc="upper left")
    axs[-1].axis("equal")


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
