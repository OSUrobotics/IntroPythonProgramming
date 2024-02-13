#!/usr/bin/env python3

# The usual imports
import numpy as np

# The matrix routines
import matrix_routines as mt
from object_routines import read_object, plot_object_in_world_coord_system

# --------------------------- Forward kinematics ------------------
# These are all of the routines needed for the lab and the homework in order to position the robot arm. The routines are
# broken up into the four groups, one for each step in the slides
#
# Slides: https://docs.google.com/presentation/d/1Ut5RnIKU8DF8k_joGXp4tJ1FzBKNIX8JYRE9wkIP_qE/edit?usp=sharing
#


# ------------------ Step 1: base/link/palm/finger transform matrices -------------------------------------
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

    # Force recalculation of matrix
    return mat_return


def get_transform_palm(palm_width):
    """ This is palm of the gripper - a rectangle palm_width tall, centered at the origin, 1/10 as wide as it is tall
    @param palm_width - the desired separation of the two fingers
    @return the 3x3 matrix"""

    # TODO: Calculate the scale matrixthat makes the palm the correct size
    mat_return = np.identity(3)

    return mat_return


def get_transform_finger(palm_width, finger_size, b_is_top):
    """ This is one of the fingers - two wedges, separated by the palm width
    @param palm_width - the desired separation of the two fingers
    @param finger_size - tuple, how long and wide to make the finger
    @param b_is_top - is this the top or the bottom finger?
    @return the modified object"""

    # TODO [optional]: Calculate the transform to get it in the right position/size/orientation
    #  b_is_top means it's the top finger...
    #  If you don't do this part, the finger will just show up as a very, very small box in the middle of the palm
    # Note 1: The base of the finger should be at 0, +- 0.5 * palm width, i.e,the base is in the middle of the palm rectangle in the x direction
    # Note 2: This should be just a scale (make the finger the right size) followed by a translate - the fingers point up in the
    #  default configuration
    # TODO: If you are doing the optional finger placement, change this matrix
    mat_return = mt.make_scale_matrix(0.1 * finger_size[0], 0.1 * finger_size[1] / 2)

    return mat_return


# ------------------ Step 1: Creating the dictionaries that hold the arm components -------------------------------------
# There are no TODOs within create_gripper and create_arm_geometry - the TODOs are all in the above functions
#  This is the function that calls get_transform_palm and get_tansform_finger
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
    base["Matrix"] = get_transform_base(base_size[0], base_size[1])

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
    arm_link is the dictionary element that corresponds to one of the links
    @param arm_link - an Object dictionary, with the angle stored in arm_link['Angle']
    @return 3x3 rotation matrix"""

    # TODO Create a rotation matrix based on the link's angle (stored with the key "Angle")
    # Return that matrix instead of the identity matrix
    return np.identity(3)


def get_matrix_finger(finger):
    """ Compute JUST the matrix that moves the finger to the correct angle
    Pulling this out as a method so we can use it elsewhere
    Finger is the dictionary element that corresponds to one of the fingers
    @param finger - the finger as an object dictionary, angle stored in finger['Angle']
    @return a 3x3 matrix"""

    # TODO (optional):
    #   Translate the base of the finger back to the origin, rotate it, then translate it back out
    #   Reminder: The middle of the finger can be found using mt.get_dx_dy_from_matrix with the 'Matrix' key
    #    Note: You want to move the base of the finger, NOT the middle, to the origin before you do the rotate
    matrix = np.identity(3)
    return matrix


def set_angles_of_arm_geometry(arm_geometry, angles):
    """ Just sets the angle of each link, gripper
    No TODOs here
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


# ----------------- Step 3: Doing forward kinematics --------------------------
def get_matrix_base(base_link):
    """ Get a matrix that will move the first link to the top of the base, pointed up
    This should work even if we change the orientation, location, and scale of the base
    @param base_link is the object that is the base (see make_blank_object() in object_routines.py for the key values in an object dictionary)
    @return 3x3 matrix that takes the origin, translates it to the top of the base, and makes x point up"""

    # TODO:
    #  Figure out where (1.0, 0.0) on the base wedge went in the world coordinate. (see Example code in JN)
    #    Remember that base_link is a dictionary; to get the matrix out use the key "Matrix"
    #  Step 1: Get the matrix from the base link
    #  Step 2: Find the point in the world coordinate, which is (1.0,0.0) in the base wedge coordinate.
    #          (point_in_world = matrix @ point_in_local, Remember that the matrix is 3x3.)
    #  Step 3: Extract only the rotation element of base_link by rotating the vector 1,0 
    #    You might find get_theta_from_matrix in matrix_routines.py useful
    #  Step 4: Rotate first (Rotation matrix in step 3), then translate (Point in step 2)
    # Return the matrix that makes the base (instead of an identity matrix)
    return np.identity(3)


def get_matrix_link(arm_link):
    """ Get a matrix that will move the next link to the end of this one, pointed along the x axis, then rotate
    both this link AND the next one by the angle of this link
    This should work even if we change the scale of the link
    @param arm_link is the object that is the arm link
    @return 3x3 matrix that takes the origin, translates it to the end of the link, and then rotates by angle"""

    # TODO:
    #  Figure out where (1.0, 0.0) on the link went in the world coordinate.
    #   Remember that the Matrix used to transform a square into the link is stored in ["Matrix"]
    #  Step 1: Get the matrices from the link
    #  Step 2: Find the point in the world coordinate, which is (1.0,0.0) in the link coordinate.
    #          (point_in_world = matrix @ point_in_local, Remember that the matrix is 3x3.)
    #  Step 3: Get the rotation matrix by using make_rotation_matrix and the angle stored in ["Angle"].
    #  Step 4: Translate first (Point in step 2), then rotate (Rotation matrix in step 3) 
    # Return the matrix that rotates the link (instead of an identity matrix)
    return np.identity(3)


def get_matrices_all_links(arm_with_angles):
    """ Get a list of matrices (one for each link, plus one for the base and one for the gripper) that we can
    use to move each component to its final location
    First matrix: The matrix to multiply the base by (should be the identity)
    Second matrix: The matrix to multiply the first link by in order to attach it to the base, pointing up
    Third matrix: The matrix to multiply the second link by in order to attach it to the first link, pointing
       in the same direction as the first link
       ...
    Last matrix: The matrix to multiply the gripper by in order to attach it to the last link, pointing in the
    same direction as the last link"""

    # First matrix is the one for the base link - should be the identity
    matrices = [np.identity(3)]

    # Matrix for the first link - the rotation plus translation to put the arm on top of the base link
    matrices.append(get_matrix_base(arm_with_angles[0]))

    # Now do all of the links - the last matrix is the one that is applied to the gripper
    # This does NOT include the finger matrices
    for link in arm_with_angles[1:-1]:
        # TODO: append a matrix to the list that is the matrix that we will multiply this link from
        #   In other words, multiply the last matrix by the matrix for this link then add it to the list

    return matrices


# ----------------- Step 4: Gripper location --------------------------
def get_gripper_location(arm_with_angles):
    """ Get the gripper grasp location (between the fingers) given the arm
    Assumes the angles are stored in the arm links.
    Use the "Grasp" key in the gripper to figure out how far to offset the  point from the base of the gripper
    @param arm_with_angles
    @return x,y as a tuple - the location of the "grasp" point in the gripper
    """
    gripper = arm_with_angles[-1]
    grasp_dist = gripper[0]["Grasp"]  # The distance out along the x axis that we'll call the "grasp" point

    # TODO:
    # Step 1: Get the matrices
    # Step 2: Use the last matrix plus the rotation of the wrist to build a matrix for the gripper
    # Step 3: Multiply the last matrix by [d, 0] to get the location in world coordinates
    # Format for returning a tuple
    return (0, 0)


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

# ----------------- Plotting --------------------------
def plot_complete_arm(axs, arm, matrices):
    """ From left to right, work backwards, plotting first the gripper, then each link in turn, and finally, the
    whole thing on the base
    @param axs are the axes of each plot window
    @param arm as a list of dictionaries, each of which is an object
    @param matrices - the matrices for each component (the TRTRTR) """

    box = read_object("Square")
    box["Matrix"] = mt.make_scale_matrix(0.75, 0.75)
    box["Color"] = "lightgrey"

    # From left to right,
    plot_object_in_world_coord_system(axs, box)
    origin = np.transpose(np.array([0, 0, 1]))
    for i, component in enumerate(arm[:-1]):
        new_origin = matrices[i] @ origin
        axs.plot(new_origin[0], new_origin[1], 'g+')
        plot_object_in_world_coord_system(axs, component, matrices[i] @ get_rotation_link(component))

    gripper = arm[-1]
    # The palm
    wrist_rotation = get_rotation_link(gripper[0])
    plot_object_in_world_coord_system(axs, gripper[0], matrices[-1] @ wrist_rotation)

    for finger in gripper[1:3]:
        plot_object_in_world_coord_system(axs, finger, matrices[-1] @ wrist_rotation @ get_matrix_finger(finger))

    # These will work when you do step 4
    x, y = get_gripper_location(arm)
    axs.plot(x, y, '+g', label="Grasp location")

    axs.set_title("Arm")
    axs.axis("equal")
    axs.legend(loc="lower left")


