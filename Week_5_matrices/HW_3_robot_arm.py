#!/usr/bin/env python3

# The usual imports
import numpy as np
import matplotlib.pyplot as plt

# These are the routines used in the lecture activity - we'll re-use them here
import matrix_routines as mt
from object_routines import read_object, plot_object_in_world_coord_system

# And the ones from lab 5
from Lab_5_matrices import create_arm_geometry, set_angles_of_arm_geometry, get_rotation_link, get_matrix_finger

# ----------------- Doing forward kinematics --------------------------
def get_matrix_base(base_link):
    """ Get a matrix that will move the first link to the top of the base, pointed up
    This should work even if we change the orientation, location, and scale of the base
    @param base_link is the object that is the base
    @return 3x3 matrix that takes the origin, translates it to the top of the base, and makes x point up"""

    # TODO:
    #  Figure out where (1.0, 0.0) went on the base wedge (that's the translation you need to apply)
    #  Figure out how (1, 0) should be rotated to make it point up
    #    Reminder: mt.get_xx_from_matrix is helpful here...
    #    Rotate first, then translate
# YOUR CODE HERE
    return np.identity(3)


def get_matrix_link(arm_link):
    """ Get a matrix that will move the next link to the end of this one, pointed along the x axis, then rotate
    both this link AND the next one by the angle of this link
    This should work even if we change the scale of the link
    @param arm_link is the object that is the arm link
    @return 3x3 matrix that takes the origin, translates it to the end of the link, and then rotates by angle"""

    # TODO:
    #  Figure out where (1.0, 0.0) went on the link (that's the translation you need to apply)
    #  Figure out how (1,0) should be rotated to make it point up
    #    Reminder: mt.get_xx_from_matrix is helpful here...
    #    Rotate first, then translate
# YOUR CODE HERE
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
    for link in arm_with_angles[1:-1]:
        # TODO: append a matrix to the list that is the matrix that we will multiply this link from
        #   In other words, multiply the last matrix by the matrix for this link then add it to the list
# YOUR CODE HERE

    return matrices


# ----------------- Gripper location --------------------------
def get_gripper_location(arm_with_angles):
    """ Get the gripper grasp location (between the fingers) given the arm
    Assumes the angles are stored in the arm links.
    Use the "Grasp" key in the gripper to figure out how far to offset the point point from the base of the gripper
    @param arm_with_angles
    @return x,y as a tuple - the location of the "grasp" point in the gripper
    """
    gripper = arm_with_angles[-1]
    grasp_dist = gripper[0]["Grasp"]  # The distance out along the x axis that we'll call the "grasp" point

    # TODO:
    # Step 1: Get the matrices
    # Step 2: Use the last matrix plus the rotation of the wrist to build a matrix for the gripper
    # Step 3: Multiply the last matrix by [d, 0] to get the location in world coordinates
# YOUR CODE HERE
    # Format for returning a tuple
    return (0, 0)


def get_gripper_orientation(arm_with_angles):
    """ Get a vector pointing out of the palm from the arm with angles
    Assumes the angles are stored in the arm links.
    @param arm_with_angles
    @return vx, vy as a tuple - the vector out of the grasp (unit length)
    """
    gripper = arm_with_angles[-1]

    # TODO:
    # Step 1: Get the matrices
    # Step 2: Use the last matrix plus the rotation of the wrist to build a matrix for the gripper
    # Step 3: Get the matrix that takes (1,0) to the world
# YOUR CODE HERE
    # Format for returning a tuple
    return (1, 0)


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

    vx, vy = get_gripper_orientation(arm)
    axs.plot([x, x + vx * gripper[0]["Grasp"]], [y, y + vy * gripper[0]["Grasp"]], '-g', label="Grasp orientation")

    axs.set_title("Arm")
    axs.axis("equal")
    axs.legend(loc="lower left")


if __name__ == '__main__':
    # Step 1 - create the arm geometry
    base_size_param = (1.0, 0.5)
    link_sizes_param = [(0.5, 0.25), (0.3, 0.1), (0.2, 0.05)]
    palm_width_param = 0.1
    finger_size_param = (0.075, 0.025)

    # This function calls each of the set_transform_xxx functions, and puts the results
    # in a list (the gripper - the last element - is a list)
    arm_geometry = create_arm_geometry(base_size_param, link_sizes_param, palm_width_param, finger_size_param)

    # Step 2 - rotate each link element in its own cooridinate system
    # Several different angles to check your results with
    angles_none = [0.0, 0.0, 0.0, [0.0, 0.0, 0.0]]
    angles_check_fingers = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [0.0, np.pi/4.0, -np.pi/4.0]]
    angles_check_wrist = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [np.pi/3.0, 0.0, 0.0]]
    angles_check = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [np.pi/3.0, np.pi/4.0, -np.pi/4.0]]
    set_angles_of_arm_geometry(arm_geometry, angles_check)

    # Step 3 & 4 - step 4 adds in drawing the green + for the gripper
    # Plot the entire arm
    # More angles to check
    angles_check_link_0 = [np.pi/4, 0.0, 0.0, [0.0, 0.0, 0.0]]
    angles_check_link_0_1 = [np.pi/4, -np.pi/4, 0.0, [0.0, 0.0, 0.0]]
    angles_gripper_check = [np.pi/6.0, -np.pi/4, 1.5 * np.pi/4, [np.pi/3.0, -np.pi/8.0, np.pi/6.0]]

    # Actually set the matrices
    set_angles_of_arm_geometry(arm_geometry, angles_gripper_check)
    matrices = get_matrices_all_links(arm_geometry)

    # Print out the matrices (if you want)
    np.set_printoptions(precision=2, suppress=True)
    for i, m in enumerate(matrices):
        print(f"Matrix {i} is\n{m}")

    # Now actually plot - when you do the gripper grasp location (step 4) it will show up here
    fig2, axs2 = plt.subplots(1, 1, figsize=(8, 8))
    plot_complete_arm(axs2, arm_geometry, matrices)

    # Depending on if your mac, windows, linux, and if interactive is true, you may need to call this to get the plt
    # windows to show
    plt.show()

    print("Done")
