#!/usr/bin/env python3
# TAF4

import numpy as np
import matplotlib.pyplot as plt

# If this fails, make sure arm_component.py is in this folder
from arm_component import ArmComponent

# The matrix routines
import matrix_routines as mt

# ------------------------- Robot classes -------------------------
# 
# Taking all the code from the robot arm assignment and organizing it in classes
# 
class RobotArm:
    def __init__(self, 
                 base_size = (0.5, 1.0),
                 link_sizes = ((0.5, 0.25), (0.3, 0.1), (0.2, 0.05)),
                 palm_width = 0.1,
                 finger_size = (0.075, 0.025)):
        """
        @param base_size - the width/height of the base
        @param link_sizes - A list of tuples, one for each link, with the link length and width
        @param palm_width - The width of the palm (how far the fingers are spaced apart)
        @param finger_size - A tuple with the finger length and width """
        # TODO (part I)
        #   Put your create_arm_geometry code here
        #   See the changes to create_gripper (from the version in arm_routines.py)
        #   Still keep all the components in a list
        #      However, each component is now an instance of ArmComponent
        #      keys become variables in the class
        #   Store the list in self.arm_geometry

        # YOUR CODE HERE
        pass
    
    def create_gripper(self, palm_width, finger_size):
        """ Make a gripper from a palm and two fingers
        Palm is centered on the x and y axis, base of finger will be at 0, 1/2 palm width

        The primary change here is to make all the objects into ArmComponent instances

        @param palm_width - the desired separation of the two fingers
        @param finger_size - how long and wide to make the finger
        @return the modified object"""

        # Make an object as a dictionary
        palm_obj = ArmComponent(name="Palm", pts=ArmComponent.points_in_a_square(), color="tomato")

        # Set the shape matrix
        palm_obj.matrix_shape_palm(palm_width=palm_width)

        # Keep this for later as a variable in the instance
        palm_obj.palm_width = palm_width
        # This is an additional variable we'll want to specify the center of the grasp
        palm_obj.grasp = finger_size[0] * 0.75

        # The gripper is a list of three elements - the fingers are optional
        gripper = [palm_obj]  # First element of the list is the palm

        # THe power of zip - set the top and bottom finger
        for b, tag, col in zip([True, False], ["Top", "Bottom"], ["darkgoldenrod", "darkgreen"]):   # top and bottom fingers
            # Create the finger from a wedge
            finger_obj = ArmComponent(name="Finger_" + tag, pts=ArmComponent.points_in_a_wedge(), color=col)
            # Sets the matrix_shape key
            finger_obj.matrix_shape_finger(palm_width=palm_width, finger_size=finger_size, b_is_top=b)

            # Keep this for later as a variable
            finger_obj.palm_width = palm_width

            # Add it to the list
            gripper.append(finger_obj)

        # return the list
        return gripper
        
# YOUR CODE HERE

    def set_angles(self, angles):
        """Set the matrix_pose matrices from the angles
        @param angles - the list of angles"""
        # TODO: Copy code from set_matrices_all_components in Homework 3 here. 
        #   Feel free to add any additional methods you need
        # YOUR CODE HERE
        pass

    def plot_complete_arm(self, axs):
        """ Plot all arm components in the same window
        @param axs are the axes of each plot window
        @param arm as a list of dictionaries, each of which is an object"""

        # Put the box around the figure
        box_pts = mt.make_scale_matrix(0.75, 0.75) @ ArmComponent.points_in_a_square()
        axs.plot(box_pts[0, :], box_pts[1, :], color="lightgrey", linestyle='solid')
        axs.plot([box_pts[0, 0], box_pts[0, -1]], [box_pts[1, 0], box_pts[1, -1]], color="lightgrey", linestyle='solid')

        # The base and links
        #   TODO: Loop over all of the base and link component and draw them
        # YOUR CODE HERE

        # The gripper
        #   TODO: Loop over all of the base and link component and draw them
        gripper = self.arm_geometry[-1]
        # YOUR CODE HERE

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
    robot_arm = RobotArm(base_size_param, link_sizes_param, palm_width_param, finger_size_param)
    if len(robot_arm.arm_geometry) != 5:
        print("Wrong number of components, should be 5, got {len(robot_arm.arm_geometry)}")
    if len(robot_arm.arm_geometry[-1]) != 3:
        print("Wrong number of gripper components, should be 3, got {len(robot_arm.arm_geometry[-1])}")


    # Step 2 - rotate each link element in its own cooridinate system
    # Several different angles to check your results with
    angles_none = [0.0, 0.0, 0.0, [0.0, 0.0, 0.0]]
    angles_check_fingers = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [0.0, np.pi/4.0, -np.pi/4.0]]
    angles_check_wrist = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [np.pi/3.0, 0.0, 0.0]]
    angles_check = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [np.pi/3.0, np.pi/4.0, -np.pi/4.0]]
    robot_arm.set_angles(angles_check)

    fig, axs = plt.subplots(1, 1, figsize=(6, 6))
    robot_arm.plot_complete_arm(axs)

    plt.show()

    print("Done")
