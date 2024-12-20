#!/usr/bin/env python3
# TAF4

# The usual imports
import numpy as np
import matplotlib.pyplot as plt

# The matrix routines
import matrix_routines as mt

# Class that can handle creating shapes (square and wedge)
#  and re-shaping those
class ArmComponent:
    def __init__(self, name, pts, color="Grey"):
        # TODO 
        #  Start by copying in the code from create_arm_component
        #  Instad of storing as a dictionary, store as variables
        #   in the class
        #  name and pts are done for you; do color, angle, and the two matrices
        # Use the variables names color, angle, matrix_shape, and matrix_pose
        self.name = name

        # Put other variables here

        # YOUR CODE HERE

        # Points
        n_points = pts.shape[1]
        self.pts = np.ones((3, n_points + 1))
        self.pts[0:2, 0:n_points] = pts[0:2, 0:n_points]
        # Duplicate the last point
        self.pts[0:2, n_points] = pts[0:2, 0]

    # TODO: Copy in points_in_a_square as a static method
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

    # TODO: Create the following methods here
    #  - matrix_shape_base
    #  - matrix_shape_link
    #  - matrix_shape_palm
    #  - matrix_shape_finger

    # YOUR CODE HERE

    def plot(self, axs, b_do_pose_matrix=False):
        """Plot the object in the world by applying Matrix_shape then Matrix_pose (if in_b_do_pose_matrix is True)
        @param axs - the axes of the figure to plot in
        @param b_do_pose_matrix - if True, do Matrix_pose @ Matrix_shape, otherwise, just do Matrix_shape"""

        matrix = np.identity(3)
        matrix = self.matrix_shape @ matrix
        if b_do_pose_matrix == True:
            matrix = self.matrix_pose @ self.matrix_shape

        try:
            # This multiplies the matrix by the points
            # matrix had better be 3x3 and obj["Pts"] 3 x n, otherwise this will fail
            pts_in_world = matrix @ self.pts
        except:
            # Something is wrong - draw a triangle
            pts = np.ones((3, 3))
            pts[0, 0] = -1
            pts[1, 0:1] = -1
            pts[2, 1] = 1
            print(f"Either your matrix is not 3x3 {matrix.shape} or your points are not 3xn {obj['Pts'].shape}")
            pts_in_world = matrix @ np.identity(3) @ pts

        axs.plot(pts_in_world[0, :], pts_in_world[1, :], color=self.color, linestyle='solid', label=self.name)
        axs.axis('equal')


if __name__ == '__main__':
    arm_component = ArmComponent("check_name", ArmComponent.points_in_a_wedge(), "Grey")

    # Step 1: Check that variable names are created correctly
    assert arm_component.name == "check_name"
    assert arm_component.color == "Grey"
    assert np.all(np.isclose(arm_component.matrix_shape, np.identity(3)))
    assert np.all(np.isclose(arm_component.matrix_pose, np.identity(3)))

    fig, axs = plt.subplots(1, 1, figsize=(1, 1))
    arm_component.plot(axs)
    plt.show()

    print(f"Done!")
