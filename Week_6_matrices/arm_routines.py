#!/usr/bin/env python3
# I25

# The usual imports
import numpy as np

# The matrix routines
import matrix_routines as mt

# The arm components
from arm_component import ArmComponent


# --------------------------- Forward kinematics ------------------
# These are all of the routines needed for the lab and the homework in order to position the robot arm. The routines are
# broken up into the four groups, one for each step in the slides
#
# Slides: https://docs.google.com/presentation/d/1Ut5RnIKU8DF8k_joGXp4tJ1FzBKNIX8JYRE9wkIP_qE/edit?usp=sharing
#

# --------------------------- How to store the arm ------------------
# These are the routines you need to create the "geometry" of the arm. Each part of the arm (link, base, palm, fingers)
#   is stored as a dictionary with all the information you need in it (angles, the matrix that shapes the geometry, the
#    points of the shape, the matrix that takes the object to it's pose in space, the color)
#
#

# ------------------  Creating the list of dictionaries that are the arm components -------------------------------------
# There are no TODOs within create_gripper and create_arm_geometry - the TODOs are all in the above functions
#  This is the function that shapes each component
def create_gripper(palm_width, finger_size):
    """ Make a gripper from a palm and two fingers
    Palm is centered on the x and y axis, base of finger will be at 0, 1/2 palm width
    @param palm_width - the desired separation of the two fingers
    @param finger_size - how long and wide to make the finger
    @return the modified object"""

    # Make an object as a dictionary
    palm_obj = create_arm_component(name="Palm", pts=points_in_a_square(), color="tomato")
    # Sets the matrix_shape key
    matrix_shape_palm(palm_obj, palm_width)
    # Keep this for later as a key
    palm_obj["Palm width"] = palm_width
    # This is an additional key we'll want to specify the center of the grasp
    palm_obj["Grasp"] = finger_size[0] * 0.75

    # The gripper is a list of three elements - the fingers are optional
    gripper = [palm_obj]  # First element of the list is the palm

    # THe power of zip - set the top and bottom finger
    for b, tag, col in zip([True, False], ["Top", "Bottom"], ["darkgoldenrod", "darkgreen"]):   # top and bottom fingers
        # Create the finger from a wedge
        finger_obj = create_arm_component(name="Finger_" + tag, pts=points_in_a_wedge(), color=col)
        # Sets the matrix_shape key
        matrix_shape_finger(finger_obj, palm_width, finger_size, b)

        # Keep this for later as a key
        finger_obj["Palm width"] = palm_width

        # Add it to the list
        gripper.append(finger_obj)

    # return the list
    return gripper


def create_arm_geometry(base_size, link_sizes, palm_width, finger_size):
    """ Create the base and each of the arm links - the number of links is given in the list link_sizes
    See slides for what these should look like when done
    @param base_size - the width/height of the base
    @param link_sizes - A list of tuples, one for each link, with the link length and width
    @param palm_width - The width of the palm (how far the fingers are spaced apart)
    @param finger_size - A tuple with the finger length and width
    @returns A list of the objects (arm_geometry)
    """

    # This is the base of the robot
    base_obj = create_arm_component(name="Base", pts=points_in_a_wedge(), color="darkturquoise")

    # Here is where the matrix that moves the base (which is a wedge) to the right size/place is set
    matrix_shape_base(base_obj=base_obj, base_height=base_size[0], base_width=base_size[1])

    # Keep the geometry in a list - start the list with the base object
    arm_geometry = [base_obj]

    # Since arm links are kinda the same, just different sizes, create a list with the link sizes and make one
    #  component from each pair of sizes
    # Note that this makes it easy to add (or remove) links by just changing the list link_sizes
    for i, size in enumerate(link_sizes):
        link_obj = create_arm_component(name=f"Link {i}", pts=points_in_a_square(), color="black")
        # Set the matrix that scales/translates the square to the right place
        matrix_shape_link(link_obj=link_obj, link_length=size[0], link_width=size[1])

        # Add this version to our list of arm components
        arm_geometry.append(link_obj)

    # The gripper is made of Three pieces - we're going to put them all together (as a list) at the end of the list...
    #   This will make it possible to build the matrix for the gripper and apply that matrix to all gripper elements
    #   Note: Putting the fingers on is optional
    gripper = create_gripper(palm_width, finger_size)

    # Add the gripper as a single element to the end of the list
    arm_geometry.append(gripper)
    return arm_geometry


# ------------------ Any additional functions you want to write for both lab 6 and the homework------

# YOUR CODE HERE


# ----------------- Plotting routines --------------------------
def plot_object(axs, obj, b_do_pose_matrix=False):
    """Plot the object in the world by applying Matrix_shape then Matrix_pose (if in_b_do_pose_matrix is True)
    @param axs - the axes of the figure to plot in
    @param obj - the object (as a dictionary)
    @param b_do_pose_matrix - if True, do Matrix_pose @ Matrix_shape, otherwise, just do Matrix_shape"""

    matrix = obj["Matrix_shape"]
    if b_do_pose_matrix == True:
        matrix = obj["Matrix_pose"] @ obj["Matrix_shape"]

    try:
        # This multiplies the matrix by the points
        # matrix had better be 3x3 and obj["Pts"] 3 x n, otherwise this will fail
        pts_in_world = matrix @ obj["Pts"]
    except:
        # Something is wrong - draw a triangle
        pts = np.ones((3, 3))
        pts[0, 0] = -1
        pts[1, 0:1] = -1
        pts[2, 1] = 1
        print(f"Either your matrix is not 3x3 {matrix.shape} or your points are not 3xn {obj['Pts'].shape}")
        pts_in_world = matrix @ np.identity(3) @ pts

    axs.plot(pts_in_world[0, :], pts_in_world[1, :], color=obj["Color"], linestyle='solid', label=obj["Name"])
    axs.axis('equal')


def plot_arm_components(axs, arm, b_do_pose_matrix=False):
    """ Plot each component in its own coordinate system with the matrix that was used to move the geometry
    @param axs are the axes of each plot window
    @param arm as a list of dictionaries, each of which is an object
    @param b_do_pose_matrix - if True, use Matrix_pose"""

    # Put a box around the shape
    box_pts = mt.make_scale_matrix(0.75, 0.75) @ points_in_a_square()

    # Plot the base and the arm links in their own windows
    for i, component in enumerate(arm[:-1]):
        # Make a box
        axs[i].plot(box_pts[0, :], box_pts[1, :], color="lightgrey", linestyle='solid')

        plot_object(axs[i], component, b_do_pose_matrix)
        axs[i].plot(0, 0, 'xr')
        axs[i].set_title(component["Name"])
        axs[i].axis("equal")

    # plot the gripper - I know it's more than one piece of geometry, so plot each in turn
    axs[-1].plot(box_pts[0, :], box_pts[1, :], color="lightgrey", linestyle='solid')
    for palm_finger in arm[-1]:
        plot_object(axs[-1], palm_finger, b_do_pose_matrix)

    # Draw a red line for the palm and an x at the base of the wrist and another at the finger contact points
    palm = arm[-1][0]
    # Get the y axis of the rotation matrix
    axs_x, axs_y = mt.get_axes_from_matrix(mt.make_rotation_matrix(palm["Angle"]))
    # Scale by palm width
    axs_y = axs_y * palm["Palm width"] / 2.0
    # Go from -vec to + vec
    axs[-1].plot([-axs_y[0], axs_y[0]], [-axs_y[1], axs_y[1]], '-r')

    # Draw a red + at the base of the palm
    axs[-1].plot(0, 0, '+r')

    # Draw a green x at the grasp point
    axs[-1].plot(axs_x[0] * palm["Grasp"], axs_x[1] * palm["Grasp"], 'xg')

    axs[-1].set_title("Gripper")
    axs[-1].legend(loc="upper left")
    axs[-1].axis("equal")


def plot_complete_arm(axs, arm):
    """ Plot all arm components in the same window
    @param axs are the axes of each plot window
    @param arm as a list of dictionaries, each of which is an object"""

    # Put the box around the figure
    box_pts = mt.make_scale_matrix(0.75, 0.75) @ points_in_a_square()
    axs.plot(box_pts[0, :], box_pts[1, :], color="lightgrey", linestyle='solid')

    # The base and links
    for component in arm[:-1]:
        plot_object(axs, component, b_do_pose_matrix=True)

    # The gripper
    gripper = arm[-1]
    for component in gripper:
        plot_object(axs, component, b_do_pose_matrix=True)

    axs.set_title("Arm")
    axs.axis("equal")
    axs.legend(loc="lower left")


