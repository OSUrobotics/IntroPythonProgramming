#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt

# All of the matrix routines are in here - we can import the Python (.py) file just like the imports above
#  All of the functions in there will be accessed as mr.
import matrix_routines as mr


# ------------------------- Practice --------------------------------
#
# The two examples here are common things that can go wrong when you create a matrix "incorrectly". Not that the
#  matrix is actually incorrect, just that it isn't what you (usually) want for moving objects around.
#

def example_weird_geometry():
    """ Create a mirrored and a non-angle preserving example """
    # Make the plot that shows the difference between rotate-translate and translate-rotate
    fig, axs = plt.subplots(1, 2, figsize=(8, 4))

    # TODO: Make seq_mirrored so that the x,y axes are flipped, and the x axis is twice as big as it was before.
    #  Draw the the flipped geometry at 2.5 2.5
    #  (see mirrored figure in slides https://docs.google.com/presentation/d/12p3VOVT5yL14-1z5T20hTscpVC0hsxjtvMLHmQLFITk/edit?usp=sharing)
    # Should be a scale followed by a translate
    mat_mirror = np.identity(3)

    # print(f"{mat}")
    axs[0].set_title("Mirrored")
    mr.plot_axes_and_circle(axs[0], mat_mirror)
    mr.plot_zigzag(axs[0], mat_mirror)

    # TODO: Make seq_skew so that the axes (red blue) are no longer 90 degrees. There are multiple solutions to this, btw.
    #  One of the simplest is to rotate then scale x differently than y
    #  Draw the the flipped geometry at 2.5 2.5 (see skewed figure in slides https://docs.google.com/presentation/d/12p3VOVT5yL14-1z5T20hTscpVC0hsxjtvMLHmQLFITk/edit?usp=sharing)
    mat_skew = np.identity(3)

    # print(f"{mat_skew}")
    axs[1].set_title("Skewed")
    mr.plot_axes_and_circle(axs[1], mat_skew)
    mr.plot_zigzag(axs[1], mat_skew)


def example_uncentered_geometry():
    """ Same matrix tranforms - but the object in a different place """
    # First plot is the "normal" one
    fig, axs = plt.subplots(1, 4, figsize=(16, 4))

    pts_circle = mr.make_pts_representing_circle(25)
    pts_zigzag = mr.plot_zigzag(axs[0], np.identity(3))

    # TODO: create the pts_circle_* and pts_zigzag_* by
    #  Moving the original geometry so that the origin is at the lower left corner of the circle
    #  Rotating the original geometry so that the x axis is "up"
    # Note: You can use the make_x_matrix commands to move the points
    pts_circle_lower_left_origin = pts_circle  # Put a matrix before pts_circle
    pts_zigzag_lower_left_origin = pts_zigzag

    pts_circle_x_up = pts_circle
    pts_zigzag_x_up = pts_zigzag

    pts_circle_x_up_lower_left_origin = pts_circle
    pts_zigzag_x_up_lower_left_origin = pts_zigzag

    mat_scl_rot_trans = mr.make_translation_matrix(-1, 2) @ \
                        mr.make_rotation_matrix(np.pi / 3.0) @ \
                        mr.make_scale_matrix(0.5, 0.75)   # pts go here

    # First plot - what happens if the circle and zig zag are centered
    mr.plot_axes_and_circle(axs[0], mat_scl_rot_trans)
    mr.plot_zigzag(axs[0], mat_scl_rot_trans)
    axs[0].set_title("Geometry centered")

    # Fancy Python looping - create 3 lists, one with the name to put in the title, the second and third
    #   with the three point matrices created above.
    list_names = ['Origin lower left', 'x up', 'x up and lower left origin']
    list_pts_circle = [pts_circle_lower_left_origin, pts_circle_x_up, pts_circle_x_up_lower_left_origin]
    list_pts_zigzag = [pts_zigzag_lower_left_origin, pts_zigzag_x_up, pts_zigzag_x_up_lower_left_origin]
    for i, (n, c, z) in enumerate(zip(list_names, list_pts_circle, list_pts_zigzag)):
        # Plot the points in their original location
        axs[i+1].plot(c[0, :], c[1, :], linestyle='solid', color='green')
        axs[i+1].plot(z[0, :], z[1, :], linestyle='dashed', color='grey')

        # Plot the points in their scale-rotate-translated location (mat)
        pts_moved = mat_scl_rot_trans @ c
        axs[i+1].plot(pts_moved[0, :], pts_moved[1, :], ':g')
        pts_moved = mat_scl_rot_trans @ z
        axs[i+1].plot(pts_moved[0, :], pts_moved[1, :], linestyle='dashed', color='grey')

        # Draw the axes and the box
        mr.plot_axes_and_box(axs[i+1], mat_scl_rot_trans)
        axs[i+1].set_title(n)


if __name__ == '__main__':
    # Mirroring and skewing
    example_weird_geometry()

    # What happens if your geometry is not centered at the origin
    example_uncentered_geometry()

    # Depending on if your mac, windows, linux, and if interactive is true, you may need to call this to get the plt
    # windows to show
    plt.show()
    print("Done")


#-------------- answers--------------------------

# Mirror and skewed
#     mat_mirror = mr.make_translation_matrix(2.5, 2.5) @ mr.make_scale_matrix(-2.0, 1.0)
#     mat_skew = mr.make_translation_matrix(2.5, 2.5) @ mr.make_scale_matrix(2.0, 1.0) @ mr.make_rotation_matrix(np.pi/4.0)

# Uncentered geometry
#    pts_circle_lower_left_origin = mr.make_translation_matrix(1, 1) @ pts_circle
#    pts_zigzag_lower_left_origin = mr.make_translation_matrix(1, 1) @ pts_zigzag

#    pts_circle_x_up = mr.make_rotation_matrix(-np.pi/2.0) @ pts_circle
#    pts_zigzag_x_up = mr.make_rotation_matrix(-np.pi/2.0) @ pts_zigzag

#    pts_circle_x_up_lower_left_origin = mr.make_translation_matrix(1, 1) @ mr.make_rotation_matrix(-np.pi/2.0) @ pts_circle
#    pts_zigzag_x_up_lower_left_origin = mr.make_translation_matrix(1, 1) @ mr.make_rotation_matrix(-np.pi/2.0) @ pts_zigzag
