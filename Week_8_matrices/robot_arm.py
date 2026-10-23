#!/usr/bin/env python3
# Fall26

# The usual imports
import numpy as np
import matplotlib.pyplot as plt

# The matrix routines. You must use these to build the matrices
import matrix_routines as mt

# The arm components code you wrote
from arm_component import ArmComponent

# If doing extra credit, uncomment this
#from gripper import Gripper
# YOUR CODE HERE

# Class that handles putting multiple arm components together to create an arm
#   1) Store the arm components in a dictionary or list
#   2) Call the creation methods to make the shapes
#   3) Set the pose matrices based on joint angles


class RobotArm2D():
    def __init__(self, base_arm_size: tuple, link_sizes: list[tuple]):
        """ Create the base and the arm links 
        You should make one ArmComponent for each.
         The first tuple is the base, the rest the links
          You should not assume 3 links """

        # GUIDE: Create and store one ArmComponent for the base and each link.

        # YOUR CODE HERE
        # This is the base of the robot
        # Keep the geometry in a list - start the list with the base object
        # Since arm links are kinda the same, just different sizes, create a list with the link sizes and make one
        #  component from each pair of sizes
        # Note that this makes it easy to add (or remove) links by just changing the list link_sizes
            # Add this version to our list of arm components

    def add_gripper(self, palm_size: float, finger_length: float):
        """Extra credit - add a gripper with the given sizes"""
        # YOUR CODE HERE
        pass

    # YOUR CODE HERE

    def set_link_angles(self, link_angles: list[float], palm_angle: float=0.0, finger_angle: float=0.0):
        """
        GUIDE:
          The first link matrix needs to rotate the iink, then translate it to the top of the base, pointing up out of the base
          To make this generalizable (so they depend on the base shape's size) you need to calculate
          the point on the top of the base shape from the base shape's shape matrix.
           Remember that the shape matrix for an ArmComponent can be gotten by get_shape_matrix
           Determine the base point by figuring out where (0.0, 1.0) on the base wedge went in the world coordinate (see Example code in JN)
            
          Step 1: Get the shape matrix from the base link
          Step 2: Find the point in the world coordinate, which is (0.0,1.0) in the base wedge coordinate.
                  (point_in_world = matrix @ point_in_local, Remember that the matrix is 3x3.)
          Step 3: Rotate first to point up, then translate to the location you found in step 2

          For the remaining matrices, this is the pseudo code:
            Build the matrix mat_current that moves the first link
            Set the first link's matrix to mat_current
            For each remaining link
                mat_add_rot_trans = add the rotation for the current link then translate by the previous link's length
                mat_current is mat_current plus mat_add_rot_trans
                Set the link's matrix to the above
            Setting the gripper's position (extra credit): Add in the palm rotation & translation to mat_current

            Remember to set the pose matrix for each link as you go.
        """
        # YOUR CODE HERE
        # Double checking that the geometry has the same number of links as the angles
        # Save the end of the last link location
            # Now do the gripper (palm)

    def get_n_links(self):
        """ Return the number of links"""
        # YOUR CODE HERE
        # GUIDE - return the number of links
        return -1
    
    def get_base(self)->ArmComponent:
        """ Return the base arm component 
        @return the base component (should be of the type ArmComponent)"""
        # YOUR CODE HERE
        # GUIDE: Return the base which should be an instance ArmComponent
        return ...
    
    def get_link(self, which_link)->ArmComponent:
        """ Return one of the links component
        @param which_link - which link 
        @return the ArmComponent for the link"""
        # YOUR CODE HERE
        # GUIDE: Return the nth link which should be an instance ArmComponent
        return ...

    def get_gripper(self):
        """ Extra credit - return the gripper"""
        # YOUR CODE HERE
        # GUIDE: Return the gripper, which should be an instance of Gripper
        #. Reminder to uncomment the import at the top of the file
        return None
    
    def get_end_location(self) -> tuple:
        """ Return the end location of the last link as a numpy array """
        # YOUR CODE HERE
        return (0.0, 0.0)

    def plot(self, axs, b_do_pose_matrix=True):
        """ Plot all arm components in the same window
        @param axs are the axes of the plot window
        @param arm is your data structure"""

        # Put the box around the figure
        box_pts = mt.make_scale_matrix(0.75, 0.75) @ ArmComponent.points_in_a_square()
        axs.plot(box_pts[0, :], box_pts[1, :], color="lightgrey", linestyle='solid')

        # The base and links
        self.get_base().plot(axs, b_do_pose_matrix=True)
        for ilink in range(0, self.get_n_links()):
            self.get_link(ilink).plot(axs, b_do_pose_matrix=b_do_pose_matrix)

        # The gripper
        if self.get_gripper() is not None:
            self.get_gripper().plot(axs, b_do_pose_matrix=b_do_pose_matrix)

        # The end location of the last link
        end_loc = self.get_end_location()
        axs.plot(end_loc[0], end_loc[1], "-gX", label="End loc")

        axs.set_title("Arm")
        axs.axis("equal")
        axs.legend(loc="lower left")


if __name__ == '__main__':

    np.set_printoptions(precision=4, floatmode='fixed')  # Print out with 4 digits of precision

    # These are example inputs for the create_arm_geometry function. 
    base_size_param = (0.5, 1.0)   # Height, width
    link_sizes_param = [(0.5, 0.25), (0.3, 0.1), (0.2, 0.05)]

    # This function should make an instance of ArmComponent (and call the correct set_to_X_shape function) for
    #   the base, one component for each of the links, and another three for the gripper (palm and fingers)
    # This function returns one thing - the data structure you make to hold all of the components
    robot_arm2d = RobotArm2D(base_arm_size=base_size_param, link_sizes=link_sizes_param)
    # If you are not doing the extra credit, this won't do anything
    palm_size = 0.1
    finger_length = 0.075
    robot_arm2d.add_gripper(palm_size=palm_size, finger_length=finger_length)

    assert robot_arm2d.get_n_links() == 3

    # Correct shape matrices - these should be correct after the Lab, but double checking here
    mat_base_check = np.array([[0.5, 0.0, 0], [0.0, 0.25, 0.25], [0.0, 0.0, 1.0]])
    mat_link1_check = np.array([[0.25, 0.0, 0.25], [0.0, 0.125, 0.0], [0.0, 0.0, 1.0]])
    mat_link2_check = np.array([[0.15, 0.0, 0.15], [0.0, 0.05, 0.0], [0.0, 0.0, 1.0]])
    mat_link3_check = np.array([[0.1, 0.0, 0.1], [0.0, 0.025, 0.0], [0.0, 0.0, 1.0]])

    assert np.all(np.isclose(robot_arm2d.get_base().get_shape_matrix(), mat_base_check))
    for indx, m in enumerate([mat_link1_check, mat_link2_check, mat_link3_check]):
        assert np.all(np.isclose(robot_arm2d.get_link(indx).get_shape_matrix(), m))

    # Don't change this one
    angles_check = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [np.pi/3.0, np.pi/4.0]]

    # Set the pose matrices
    robot_arm2d.set_link_angles(link_angles=angles_check[0:-1], palm_angle=angles_check[-1][0], finger_angle=angles_check[-1][1])

    # Now check the matrices numerically
    mat_check_base = np.identity(3)
    print("Base matrix")
    print(robot_arm2d.get_base().get_pose_matrix())
    assert np.all(np.isclose(robot_arm2d.get_base().get_pose_matrix(), mat_check_base, atol=0.01))  

    mat_check_link_1 = np.array([[ -1.0,  0.0,  0.0], \
                                [  0.0, -1.0,  0.5], \
                                [  0.0,  0.0,  1.0]])
                                
    mat_check_link_2 = np.array([[ -0.7071, -0.7071, -0.5], \
                                [  0.7071, -0.7071,  0.5], \
                                [  0.0,     0.0,  1.0]])

    mat_check_link_3 = np.array([[ 1.0, 0.0, -0.71213], \
                                [ 0.0, 1.0,  0.71213], \
                                [ 0.0, 0.0,  1.0]])

    for ilink, m in enumerate((mat_check_link_1, mat_check_link_2, mat_check_link_3)):
        print(f"link {ilink}")
        print(robot_arm2d.get_link(ilink).get_pose_matrix())
        assert(np.all(np.isclose(robot_arm2d.get_link(ilink).get_pose_matrix(), m, atol=0.01)))   

    # Check the end location method
    # As in the previous problem, you can use the "simpler" angles to check your function
    angles_check_end_location = [np.pi/3, -np.pi/6, 3.0 * np.pi/6]

    robot_arm_2 = RobotArm2D(base_arm_size=base_size_param, link_sizes=link_sizes_param)
    robot_arm_2.set_link_angles(angles_check_end_location)

    # Check the end location is correct (there is plotting code in the next cell)
    end_loc = robot_arm_2.get_end_location()
    assert np.isclose(end_loc[0], -0.7562, atol=0.01) and np.isclose(end_loc[1], 0.9098, atol=0.01)

    # -------------- Generalization check ------------------#
    # Create another arm geometry
    base_size_longer_param = (0.5, 0.25) # squished (height, width)
    link_sizes_longer_param = [(0.3, 0.15), (0.2, 0.09), (0.1, 0.05), (0.075, 0.03)]
    palm_width_longer_param = 0.15
    finger_length_longer_param = (0.085, 0.015)


    # This function calls each of the set_transform_xxx functions, and puts the results
    # in a list (the gripper - the last element - is a list)
    robot_arm_longer = RobotArm2D(base_size_longer_param, link_sizes_longer_param)

    # Set the angles of the arm
    angles_start_longer = [-np.pi/4.0, -np.pi/4, 1.2 * np.pi/4, -1 * np.pi/8]
    robot_arm_longer.set_link_angles(angles_start_longer)

    end_loc_longer_check = robot_arm_2.get_end_location()

    assert np.isclose(end_loc_longer_check[0], -0.756218, atol=0.01) and np.isclose(end_loc_longer_check[1], 0.909808, atol=0.01)

    # ------------- plot code --------------#
    # Check the combined link/gripper/finger rotations
    # Several different angles to check your routines with 
    #  Feel free to change these
    angles_none = [0.0, 0.0, 0.0, [0.0, 0.0]]
    angles_check_link_0 = [np.pi/4, 0.0, 0.0, [0.0, 0.0]]
    angles_check_link_0_1 = [np.pi/4, -np.pi/4, 0.0, [0.0, 0.0]]
    angles_check_wrist = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [np.pi/3.0, 0.0]]
    angles_check_fingers = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [0.0, np.pi/4.0]]

    angs = {"None": angles_none,
            "Link 0": angles_check_link_0,
            "Link 0-1": angles_check_link_0_1,
            "All": angles_check,
            "Palm": angles_check_wrist,
            "Fingers": angles_check_fingers,
            }


    nrows = 2
    ncols = 3
    fig, axs = plt.subplots(nrows, ncols, figsize=(9, 6))
    for indx, (key, item) in enumerate(angs.items()):
        robot_arm2d.set_link_angles(link_angles=item[0:-1], palm_angle=item[-1][0], finger_angle=item[-1][1])
        robot_arm2d.plot(axs=axs[indx // ncols, indx % ncols])
        axs[indx // ncols, indx % ncols].set_title(key)

    fig.tight_layout()
    plt.show()

    print("Done!")