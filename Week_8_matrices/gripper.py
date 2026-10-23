#!/usr/bin/env python3
# Fall26

# The usual imports
import numpy as np
import matplotlib.pyplot as plt

# The matrix routines. You must use these to build the matrices
import matrix_routines as mt
from arm_component import ArmComponent 

"""                    THIS IS EXTRA CREDIT                       """

# Class that handles making the gripper (palm plus fingers) THIS IS EXTRA CREDIT - you don't have to do it
#   1) The palm is a long thin rectangle that is centered at the origin and is palm_size in y and 1/20 palm_size in x
#.  2) The fingers are wedges that attach at the top/bottom of the palm (0, +-palm_size/2). 
#        The base of the finger is the bottom of the wedge; it tapers toward the finger tip
#        The fingers point to the right with the base at 0, +- palm_width / 2
#        The finger is 1/3 as wide as it is tall
#   3) The gripper gets two rotation values - one to rotate the palm, one to rotate the fingers at the base
#.  4) The fingers rotate in opposite direction (top rotates down, bottom rotates up)
class Gripper:
    def __init__(self, palm_size: float, finger_length: float):
        """ Create the gripper (palm and two fingers)
             @returns None"""
        # GUIDE
        #   Create three shapes - one for the palm, and one for each finger
        #.  You can (and should) re-use the create points methods in ArmComponent (see below)
        #   Exactly how you want to store the 3 shapes (and pose/shape matrices) is up to you. 
        #.   Your code will be checked/plotting will happen through the get_* methods
        self.name = "Gripper"  
        self.color = ...      # GUIDE: Set to an actual color

        # Note: This works because points_in_a_square() is a static method - it doesn't need a self pointer
        # Note 2: If this fails, it's probably because arm_component.py is not in the same folder as this file
        pts_in_square = ArmComponent.points_in_a_square()
        pts_in_wedge = ArmComponent.points_in_a_wedge()
            
        # GUIDES Step 1: create variables for the points/matrices for the palm/fingers
        #  For each of the palm/fingers You will need
        #.    The points that make up the shape
        #     A 3x3 matrix for shaping the square/wedge (set this here - there will not be a separate call for making the griper shapes)
        #     A 3x3 matrix for rotating/translating each shape based on the current palm and finger angles
        #  You might also want to save the palm size and finger length
        #  See comments at the top for how to size/shape the palm/finger
        # YOUR CODE HERE
        # Make the shapes with duplicate points
            # Duplicate the last point

    def get_palm_pts(self):
        """ Return the points for the palm"""
        # YOUR CODE HERE
        # GUIDE STEP 1: Change this to return your palm points
        return ...
    
    def get_finger_pts(self, is_top: bool):
        """ Return the points for the top or bottom finger"""
        # YOUR CODE HERE
        # GUIDE STEP 1: Change this to return your finger points
        return ...
    
    def get_palm_shape_matrix(self):
        """ Return the shape matrix for the palm"""
        # YOUR CODE HERE
        # GUIDE STEP 2: Change this to return your palm shape matrix
        return ...
    
    def get_finger_shape_matrix(self, is_top: bool):
        """ Return the shape matrix for the top or bottom finger"""
        # YOUR CODE HERE
        # GUIDE STEP 2: Change this to return your top/bottom finger shape matrix
        return ...
    
    def get_palm_pose_matrix(self):
        """ Return the pose matrix for the palm"""
        # YOUR CODE HERE
        # GUIDES STEP 2: Change this to return your pose matrix
        return ...

    def get_finger_pose_matrix(self, is_top: bool):
        """ Return the pose matrix for the finger(s)"""
        # YOUR CODE HERE
        # GUIDES STEP 2: Change this to return your pose matrix for the appropriate finger
        return ...

    def set_rotations(self, palm_rot_amt=0.0, finger_rot_amt=0.0, link_to_base_matrix=np.identity(3)):
        """ Set the pose matrix for the palm and fingers
        @param palm_rot_amt - how much to rotate the palm by (rotates around the origin)
        @param finger_rot_amt - how much to rotate the fingers by. Top finger rotates down, bottom rotates up
        @param link_to_base_matrix - the matrix that is the. omposition of all the matrices up to the palm"""

        # GUIDE
        # The finger matrix rotates the finger, then adds the palm rotation.
        # For the finger to rotate properly: Translate the base to the origin, rotate, then translate back. 
        # Where is the base of the finger? Hint: You should have saved this in the _init_  method; it's 1/2 the palm siae
        #  Again, use the mt.make_xx_matrix routines, don't just make an array
        # YOUR CODE HERE
        pass

    def plot(self, axs, b_do_pose_matrix=False):
        """Plot the gripper in the world by applying the matrix returned by get_shape_*_matrix() then 
           the matrix returned by get_pose_*_matrix() (if in_b_do_pose_matrix is True)
        @param axs - the axes of the figure to plot in
        @param b_do_pose_matrix - if True, do get_shape_matrix() @ get_shape_matrix(), otherwise, just do get_shape_matrix()"""

        shape_pts = [self.get_palm_pts(), self.get_finger_pts(True), self.get_finger_pts(False)]
        shape_matrices = [self.get_palm_shape_matrix(), self.get_finger_shape_matrix(True), self.get_finger_shape_matrix(False)]
        pose_matrices = [self.get_palm_pose_matrix(), self.get_finger_pose_matrix(True), self.get_finger_pose_matrix(False)]

        for pts, shape_matrix, pose_matrix in zip (shape_pts, shape_matrices, pose_matrices):
            # Plot with only the shape matrix
            plot_matrix = shape_matrix

            # Plot with the shape matrix and the pose matrix
            if b_do_pose_matrix == True:
                plot_matrix = pose_matrix @ shape_matrix

            try:
                # This multiplies the matrix by the points
                # matrix had better be 3x3 and obj["Pts"] 3 x n, otherwise this will fail
                pts_in_world = plot_matrix @ pts
            except:
                # Something is wrong - draw a triangle
                pts = np.ones((3, 3))
                pts[0, 0] = -1
                pts[1, 0:1] = -1
                pts[2, 1] = 1
                print(f"Either your matrix is not 3x3 {plot_matrix.shape} or your points are not 3xn {pts.shape}")
                pts_in_world = np.identity(3) @ pts

            axs.plot(pts_in_world[0, :], pts_in_world[1, :], color=self.color, linestyle='solid')
        axs.axis('equal')

    def __str__(self):
        """ This creates a string from the class. I've set it up to print out key, value pairs for you. See
        https://www.digitalocean.com/community/tutorials/python-str-repr-functions for more information on this method; 
        TLDR: you can do print(class instance name)
        @returns string"""
        str_out = f"Class name: {self.name}, color: {self.color}\n"

        # See, for example, https://www.geeksforgeeks.org/how-to-get-a-list-of-class-attributes-in-python/
        #   Since classes are (more or less) dictionaries with variables and method, we just have to list them...
        # Print matrices with 4 decimal places
        np.set_printoptions(formatter={'float': lambda x: "{0:0.6f}".format(x)})
        for k, v in self.__dict__.items():
            if not (k == "name" or k == "color"):
                if isinstance(v, np.ndarray):
                    str_out = str_out + f"Key: {k}, Value:\n{v}\n"
                else:
                    str_out = str_out + f"Key: {k}, Value: {v}\n"
        return str_out


if __name__ == '__main__':

    np.set_printoptions(precision=4, floatmode='fixed')  # Print out with 4 digits of precision

    # Checking the gripper
    # The sizes for all of the components
    palm_size = 0.1
    finger_length = 0.075

    # Create the gripper (calls the init function)
    #.  The shape matrices should be set at this point
    gripper = Gripper(palm_size=palm_size, finger_length=finger_length)

    # Check matrices
    mat_palm_check = np.array([[0.005, 0.0, 0.0], [0.0, 0.05, 0.0], [0.0, 0.0, 1.0]])
    mat_finger_top_check = np.array([[0.0, 0.0375, 0.0375], [-0.0125, 0.0, 0.05], [0.0, 0.0, 1.0]])
    mat_finger_bot_check = np.array([[0.0, 0.0375, 0.0375], [-0.0125, 0.0, -0.05], [0.0, 0.0, 1.0]])

    assert np.all(np.isclose(gripper.get_palm_shape_matrix(), mat_palm_check))
    assert np.all(np.isclose(gripper.get_finger_shape_matrix(is_top=True), mat_finger_top_check))
    assert np.all(np.isclose(gripper.get_finger_shape_matrix(is_top=False), mat_finger_bot_check))
    print("Step 1: gripper shape passed!")

    # ------- Check the matrices mathematically --------------
    # Rotate the palm and not the fingers
    #   If the fingers aren't rotating then the finger rotation matrices are just the palm ones
    rot_palm_amt = -np.pi/4
    rot_finger_amnt = 0.0
    gripper.set_rotations(palm_rot_amt=rot_palm_amt, finger_rot_amt=rot_finger_amnt)

    mat_pose_check_palm = mt.make_rotation_matrix(rot_palm_amt)

    assert np.all(np.isclose(gripper.get_palm_pose_matrix(), mat_pose_check_palm, atol=0.001))
    assert np.all(np.isclose(gripper.get_finger_pose_matrix(True), mat_pose_check_palm, atol=0.001))
    assert np.all(np.isclose(gripper.get_finger_pose_matrix(False), mat_pose_check_palm, atol=0.001))

    # Rotate the fingers and the palm
    rot_palm_amt = -np.pi/4
    rot_finger_amnt = np.pi/8
    gripper.set_rotations(palm_rot_amt=rot_palm_amt, finger_rot_amt=rot_finger_amnt)

    assert np.all(np.isclose(gripper.get_palm_pose_matrix(), mat_pose_check_palm, atol=0.001))
    mat_check_f1 = np.array([[0.9239, 0.383, 0.01622], [-0.3827, 0.9239, -0.01083], [0, 0, 1]])
    mat_check_f2 = np.array([[0.383, 0.9239, 0.01083], [-0.9239, 0.3827, -0.0162], [0, 0, 1]])
    assert np.all(np.isclose(gripper.get_finger_pose_matrix(True), mat_check_f1, atol=0.001))
    assert np.all(np.isclose(gripper.get_finger_pose_matrix(False), mat_check_f2, atol=0.001))

    print("Step 2: Wrist/finger poses passed!")

    # ------- Now put the gripper on the end of the arm and check it ------------- 
    from robot_arm import RobotArm2D
    # These are example inputs for the create_arm_geometry function. 
    base_size_param = (0.5, 1.0)   # Height, width
    link_sizes_param = [(0.5, 0.25), (0.3, 0.1), (0.2, 0.05)]

    robot_arm = RobotArm2D(base_arm_size=base_size_param, link_sizes=link_sizes_param)
    robot_arm.add_gripper(palm_size=palm_size, finger_length=finger_length)
    # Now set the arm angles and the gripper angles
    angles_check = [np.pi/2, -np.pi/4, -3.0 * np.pi/4, [np.pi/3.0, np.pi/4.0]]
    robot_arm.set_link_angles(link_angles=angles_check[0:-1], palm_angle=angles_check[-1][0], finger_angle=angles_check[-1][1])    

    # Now check matrices mathematically
    mat_check_wrist = np.array([[ 0.5, -0.8660,  -0.5121], \
                                [ 0.8660,  0.5,   0.7121], \
                                [ 0.0,  0.0,  1.0]])
    print(robot_arm.get_gripper().get_palm_pose_matrix())
    assert np.all(np.isclose(robot_arm.get_gripper().get_palm_pose_matrix(), mat_check_wrist, atol=0.01))    

    mat_check_f1 = np.array([[-0.25881, -0.965926,  -0.507137], \
                            [ 0.965926, -0.258819,   0.750073], \
                            [ 0.0,  0.0,  1.0]])
    print(robot_arm.get_gripper().get_finger_pose_matrix(is_top=True))
    assert np.all(np.isclose(robot_arm.get_gripper().get_finger_pose_matrix(is_top=True), mat_check_f1, atol=0.01))

    mat_check_f2 = np.array([[0.965926, -0.258819,  -0.481772], \
                         [0.258819, 0.965926,   0.735428], \
                         [ 0.0,  0.0,  1.0]])
    print(robot_arm.get_gripper().get_finger_pose_matrix(is_top=False))
    assert np.all(np.isclose(robot_arm.get_gripper().get_finger_pose_matrix(is_top=False), mat_check_f2, atol=0.01))

    # Plot the results
    fig, axs = plt.subplots(1, 4, figsize=(12, 4))

    # STEP 2 check: The left plot is the gripper in it's initial configuration; the right one has the palm rotated and the fingers
    gripper.set_rotations(palm_rot_amt=0.0, finger_rot_amt=0.0)
    mt.plot_axes_and_big_box(axs[0], box_size=0.2)
    gripper.plot(axs[0], b_do_pose_matrix=False)
    axs[0].set_title(gripper.name)

    # Do rotation of just the palm
    gripper.set_rotations(palm_rot_amt=-np.pi/4, finger_rot_amt=0.0)
    mt.plot_axes_and_big_box(axs[1], box_size=0.2)
    gripper.plot(axs[1], b_do_pose_matrix=True)
    axs[1].set_title(gripper.name)

    # Do rotation of fingers and palm
    gripper.set_rotations(palm_rot_amt=-np.pi/4, finger_rot_amt=np.pi/8)
    mt.plot_axes_and_big_box(axs[2], box_size=0.2)
    gripper.plot(axs[2], b_do_pose_matrix=True)
    axs[2].set_title(gripper.name)

    robot_arm.plot(axs=axs[-1])
    axs[3].set_title("Full arm")

    fig.tight_layout()
    plt.show()

    print(f"Done!")