#!/usr/bin/env python3
# I25

# The usual imports
import numpy as np
import matplotlib.pyplot as plt

# The matrix routines
import matrix_routines as mt

# Class that can handle creating shapes (square and wedge) and re-shaping those to be the arm components
#   For this assignment we're going to treat a class as basically a glorified dictionary.
#   1) Instead of doing, eg, dict["my_key"] = 3, we will do self.my_key = 3. 
#   2) Each function is now inside of the class (indented once) and the first parameter of most functions is "self"
#      - don't change this
#   3) Instead of creating a dictionary by, eg, my_dict = {"my_key":3}, the initial data will 
#       be created in the __init__ function
#
#   That's it. The most common problem will be you'll forget the self. in front of a variable name
class ArmComponent:
    def __init__(self, name, color="Grey", shape_to_use="square"):
        """ Initialize the arm component with the parts every link needs; the actual matrices will be
              Created in the make_shape_* methods below
             @param name - name for the shape
             @param pts - the points (either wedge or square) to use for the shape
             @param color - what color to draw the shape in 
             @param shape_to_use - one of "square" or "wedge"
             @returns None"""
        # TODO 
        #   Create all of the variables an arm component needs. I've done the first few for you.
        #   Notice the self. - this says store that data here. 
        #    NOTE: self.name is NOT the same as name - name is the input variable, self.name is a variable "name"
        #          stored in the class
        self.name = name
        self.color = color

        # Points - one of the nice things about using a class is you can do some "fancy" initialization. In
        #  this case we're going to duplicate the last point in pts and make sure we have a 3xn+1 matrix
        if shape_to_use == "square":
            pts = ArmComponent.points_in_a_square()
        elif shape_to_use == "wedge":
            pts = ArmComponent.points_in_a_wedge()
        else:
            print(f"Arm component: You asked for a shape {shape_to_use}, but I do not know that shape")
            pts = ArmComponent.points_in_a_square()
            
        self.shape_name = shape_to_use
        n_points = pts.shape[1]
        # make the pts variable for the class
        self.pts = np.ones((3, n_points + 1))
        self.pts[0:2, 0:n_points] = pts[0:2, 0:n_points]
        # Dupliczte teh last point
        self.pts[0:2, n_points] = pts[0:2, 0]
        # Put other variables here

        # TODO Step 2: create variables for the other things you might want to keep in an arm component
        #  You will need (at least)
        #     A 3x3 matrix for shaping the square/wedge (this is mat_shape_square_* from the lecture activity)
        #     A 3x3 matrix for rotating/translating the shape based on the current angle (this is the mat_pose_* from
        #           the lecture activity)
        #  You will might also want to save length and width and current angle
        #  For each variable, define a default value (eg, self.angle = 0.0). For any matrix, set it to be the identity
        #    Why isn't there a length/width input? We'll set those later in the make_shape_* methods
        # TODO Step 2: Make sure you change get_shape_matrix and get_pose_matrix to return the matrices you create
        # YOUR CODE HERE


    # Using the staticmethod decorator like this means that this method does not
    #  have/need a self pointer (notice no self)
    @staticmethod
    def points_in_a_wedge():
        """ Returns a 3x4 array of points in the shape of a wedge, with the bottom at -1, -1 to 1, -1 and the top squished in"""
        pts_wedge = np.ones((3, 4))
        pts_wedge[0:2, 0] = [-1, -1]
        pts_wedge[0:2, 1] = [ 1, -1.0]
        pts_wedge[0:2, 2] = [ 0.8,  1.0]
        pts_wedge[0:2, 3] = [-0.8,  1.0]
        return pts_wedge

    @staticmethod
    def points_in_a_square():
        """ Returns a 3x4 array of points in the shape of a square, from -1,1 to 1,1"""
        # TODO STEP 1: Take your pts_square = ... code from the lecture activity and copy it in here.
        #  Make sure it's indented at this leve
        #  Add a return statement at the end
        #  If you're confused, look at points_in_a_wedge, above
        # YOUR CODE HERE

    def get_shape_matrix(self):
        """ Return the shape matrix"""
        # YOUR CODE HERE
        # TODO STEP 2: Change this to return your shape matrix
        return ...
    
    def get_pose_matrix(self):
        """ Return the pose matrix"""
        # YOUR CODE HERE
        # TODO STEP 2: Change this to return your pose matrix
        return ...

    def matrix_shape_base(self, base_width=1.0, base_height=0.5):
        """ Position and orient the base of the arm (the wedge-shape at the bottom)
        Base middle should be at 0,0, wedge pointed up, base_width wide, base_height tall
        @param base_width - width of the base
        @param base_height - height of the base"""

        # TODO STEP 3a: Copy the code from the lab question here, and set the matrix shape variable
        # YOUR CODE HERE
        ... # Replace with real code

    def matrix_shape_link(self, link_length, link_width):
        """ This is one of the arm components - since they're all kinda the same (just different sizes) just have
        one function to create them
        The link should have the middle of the left hand side at 0,0 and extend along the x_axis by link_length
        @param link_length - the desired length of the link
        @param link_width - the desired height of the link"""

        # TODO STEP 3b: Make the link shape matrix 
        # YOUR CODE HERE
        ... # Replace with real code

    def matrix_shape_palm(self, palm_width):
        """ This is palm of the gripper - a rectangle palm_width tall, centered at the origin, 1/10 as wide as it is tall
        @param palm_width - the desired separation of the two fingers
        @return the 3x3 matrix"""

        # TODO STEP 3c: Make the palm shape matrix
        # YOUR CODE HERE
        ... # Replace with real code

    def matrix_shape_finger(self, palm_width, finger_length, finger_width, b_is_top):
        """ This is one of the fingers. Each finger is a wedge, separated by the palm width
        The base of the finger is the bottom of the wedge; it tapers toward the finger timp
        The fingers point to the right with the base at 0, +- palm_width / 2
        @param palm_width - the desired separation of the two fingers
        @param finger_length - how long to make the finger
        @param finger_width - how wide to make the finger
        @param b_is_top - is this the top or the bottom finger?"""

        # TODO STEP 3c: Make the finger shape matrix
        # YOUR CODE HERE
        ... # Replace with real code

    def set_pose_matrix(self, pose_matrix):
        """Set the pose matrix to the given one
        @param pose_matrix - a 3x3 matrix that positions the arm
        """
        # TODO Step 4: set your matrix here
        # YOUR CODE HERE
        ... # Replace with real code

    def set_pose_rotation(self, rot_amt=0.0):
        """ Set the pose matrix for the component
        @param rot_amt - how much to rotate by"""

        # TODO Step 4: Set your pose matrix to be a rotation by the given amount
        # Optional: If this is a finger then rotate the finger properly. Translate the base to the
        #   origin, rotate, then translate back. Where is the base? You can use get_dx_dy_from_matrix() in
        #   matrix_routines to get the point OR just store it in the class as a variable...
        #  NOTE: You'll need to figure out that this is a finger, and if it's the top or the bottom...
        #   There are lots of ways to do this - don't forget you can add more variables in __init__
        pose_matrix = np.identity(3)   # fix this
        # YOUR CODE HERE
        # Call the set_pose_matrix method to actually save the matrix
        self.set_pose_matrix(pose_matrix=pose_matrix)

    def plot(self, axs, b_do_pose_matrix=False):
        """Plot the object in the world by applying Matrix_shape then Matrix_pose (if in_b_do_pose_matrix is True)
        @param axs - the axes of the figure to plot in
        @param b_do_pose_matrix - if True, do Matrix_pose @ Matrix_shape, otherwise, just do Matrix_shape"""

        # Plot with only the shape matrix
        plot_matrix = self.get_shape_matrix()

        # Plot with the shape matrix and the pose matrix
        if b_do_pose_matrix == True:
            plot_matrix = self.get_pose_matrix() @ self.get_shape_matrix()

        try:
            # This multiplies the matrix by the points
            # matrix had better be 3x3 and obj["Pts"] 3 x n, otherwise this will fail
            pts_in_world = plot_matrix @ self.pts
        except:
            # Something is wrong - draw a triangle
            pts = np.ones((3, 3))
            pts[0, 0] = -1
            pts[1, 0:1] = -1
            pts[2, 1] = 1
            print(f"Either your matrix is not 3x3 {plot_matrix.shape} or your points are not 3xn")
            pts_in_world = plot_matrix @ np.identity(3) @ pts

        axs.plot(pts_in_world[0, :], pts_in_world[1, :], color=self.color, linestyle='solid', label=self.name)
        axs.axis('equal')

    def __str__(self):
        """ This creates a string from the class. I've set it up to print out key, value pairs for you. See
        https://www.digitalocean.com/community/tutorials/python-str-repr-functions for more information on this method; 
        TLDR: you can do print(class instance name)
        @returns string"""
        str_out = f"Class name: {self.name}, color: {self.color}, shape: {self.shape_name}\n"

        # See, for example, https://www.geeksforgeeks.org/how-to-get-a-list-of-class-attributes-in-python/
        #   Since classes are (more or less) dictionaries with variables and method, we just have to list them...
        # Print matrices with 4 decimal places
        np.set_printoptions(formatter={'float': lambda x: "{0:0.6f}".format(x)})
        for k, v in self.__dict__.items():
            if not (k == "name" or k == "color" or k == "shape_name"):
                if isinstance(v, np.ndarray):
                    str_out = str_out + f"Key: {k}, Value:\n{v}\n"
                else:
                    str_out = str_out + f"Key: {k}, Value: {v}\n"
        return str_out


if __name__ == '__main__':
    # Step 1: Check that points_in_a_square is correct
    pts_in_a_square = ArmComponent.points_in_a_square()
    assert pts_in_a_square.shape == (3, 4) or pts_in_a_square.shape == (3, 5)
    assert np.count_nonzero(pts_in_a_square[0:2, 0:4] == 1) == 4    
    assert np.count_nonzero(pts_in_a_square[0:2, 0:4] == -1) == 4

    print("Step 1: Points in a square passed!")

    # Step 2: Check that variable names created correctly and get_* methods correct
    arm_component_blank = ArmComponent("check_name", color="Grey", shape_to_use="wedge")

    assert arm_component_blank.name == "check_name"
    assert arm_component_blank.color == "Grey"
    assert arm_component_blank.shape_name == "wedge"

    # Check that returning a 3x3 identity matrix
    mat_shape = arm_component_blank.get_shape_matrix()
    mat_pose = arm_component_blank.get_pose_matrix()

    assert np.all(np.isclose(mat_shape, np.identity(3)))
    assert np.all(np.isclose(mat_pose, np.identity(3)))

    print("Your arm component is:")
    print(arm_component_blank)   # Yes, printing works (see __str__ method above)
    print("Step 2: Init passed!")

    # STEP 3a: Check that the base matrix is correct
    base_width = 1.0
    base_height = 0.5
    mat_base_check = np.array([[0.5, 0.0, 0], [0.0, 0.25, 0.25], [0.0, 0.0, 1.0]])
    arm_component_base = ArmComponent(name="Base", color="black", shape_to_use="wedge")
    arm_component_base.matrix_shape_base(base_width=base_width, base_height=base_height)

    assert np.all(np.isclose(arm_component_base.get_shape_matrix(), mat_base_check))        
    print("Step 3a: base passed!")

    # STEP 3b: Check that the link matrix is correct
    # The size of the link 
    link1_length = 0.5
    link1_width = 0.25
    mat_link1_check = np.array([[0.25, 0.0, 0.25], [0.0, 0.125, 0.0], [0.0, 0.0, 1.0]])
    arm_component_link1 = ArmComponent(name="Link1", color="blue", shape_to_use="square")
    arm_component_link1.matrix_shape_link(link_length=link1_length, link_width=link1_width)

    assert np.all(np.isclose(arm_component_link1.get_shape_matrix(), mat_link1_check))
    print("Step 3b: link passed!")

    # STEP 3c: Check that the gripper
    # The sizes for all of the components
    palm_width = 0.1
    finger_length = 0.075
    finger_width = 0.025

    # Create the three components
    arm_component_palm = ArmComponent(name="Palm", color="tomato", shape_to_use="square")
    arm_component_finger_top = ArmComponent(name="Finger top", color="green", shape_to_use="wedge")
    arm_component_finger_bot = ArmComponent(name="Finger bot", color="green", shape_to_use="wedge")

    # Set the shape matrix
    arm_component_palm.matrix_shape_palm(palm_width=palm_width)
    arm_component_finger_top.matrix_shape_finger(palm_width=palm_width, finger_length=finger_length, finger_width=finger_width, b_is_top=True)
    arm_component_finger_bot.matrix_shape_finger(palm_width=palm_width, finger_length=finger_length, finger_width=finger_width, b_is_top=False)

    # Check matrices
    mat_palm_check = np.array([[0.005, 0.0, 0.0], [0.0, 0.05, 0.0], [0.0, 0.0, 1.0]])
    mat_finger_top_check = np.array([[0.0, 0.0375, 0.0375], [-0.0125, 0.0, 0.05], [0.0, 0.0, 1.0]])
    mat_finger_bot_check = np.array([[0.0, 0.0375, 0.0375], [-0.0125, 0.0, -0.05], [0.0, 0.0, 1.0]])

    assert np.all(np.isclose(arm_component_palm.get_shape_matrix(), mat_palm_check))
    assert np.all(np.isclose(arm_component_finger_top.get_shape_matrix(), mat_finger_top_check))
    assert np.all(np.isclose(arm_component_finger_bot.get_shape_matrix(), mat_finger_bot_check))
    print("Step 3c: gripper passed!")

    fig, axs = plt.subplots(2, 4, figsize=(16, 4))

    # STEP 4 check: The bottom row should have all the components rotated clockwise by pi/4
    box_sizes = [1.1, 1.0, 1.0, 0.2]
    for irow, b_plot in enumerate((False, True)):
        for i, ac in enumerate((arm_component_blank, arm_component_base, arm_component_link1, arm_component_palm)):
            mt.plot_axes_and_big_box(axs[irow, i], box_size=box_sizes[i])
            ac.plot(axs[irow, i], b_do_pose_matrix=b_plot)
            axs[irow, i].set_title(ac.name)

            # Do rotation
            ac.set_pose_rotation(-np.pi/4)

        for ac in (arm_component_finger_top, arm_component_finger_bot):
            ac.plot(axs[irow, -1], b_do_pose_matrix=b_plot)
            ac.set_pose_rotation(-np.pi/4)

        axs[irow, -1].set_title("gripper")        

    fig.tight_layout()
    plt.show()

    print(f"Done!")