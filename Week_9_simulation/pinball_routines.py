#!/usr/bin/env python3

import numpy as np

# This bit of crazy code ensures that we can access the files in Week_6_matrices
# Important: If current directory is IntroPythonProgramming and NOT Week_8_simulation, then you need
#   to change the python setting (extensions->python->gear box ->Execute in file Dir) to execute in the 
#   current directory (see https://docs.google.com/document/d/1Cp4uuRHMWHfKTAbYAV14y2tMWslmj_-bv_xo3CxYGAo/edit?usp=sharing)
import os 
import sys
if "Week_6_matrices" not in sys.path:
    sys.path.insert(0, os.path.abspath('../Week_6_matrices'))


# ----- iterative systems part II ----------
# These are the routines used in this week's assignments. Copy them, or include this .py file
def acceleration_due_to_gravity():
    """Somewhat silly - but if we need to change it, then we can  change it just here"""
    gravity = -9.8     # m/s
    return gravity


# ------------------------ iterating --------------------------
# Only one method defined for you here - doing one time step
#

# It seems a bit overkill to make a functions for the update, but it *does* make it easier to
#  debug, because you can check if this function is correct with some known values
def compute_next_step(current_state, delta_t=0.1):
    """ How to compute the next position and velocity from this one
    @param current_state - the pose (x, y) and velocity (vx, vy) and acceleration (ax, ay) as a numpy array
    @param delta_t - the time step to use. Define a default t value that you've determined works well
    @return the new position, velocity as a tuple"""

    # TODO: This is compute_next_position_and_velocity from a_tutorial_functions in week 4.
    #  Changes: Keep the pose and the velocity and acceleration in a 3x2 numpy array
    #  Position is position + dt * velocity
    #  Velocity is velocity + dt * acceleration
    #  Acceleration is gravity (optional HWK: Add drag, which is a fraction of velocity in the opposite direction)
    result = np.zeros(current_state.shape)
    # BEGIN SOLUTION
    # The new position (for both x and y) is just p + dt * v - current position + delta t * velocity
    result[0, :] = current_state[0, :] + delta_t * current_state[1, :]   # Numpy arrays will handle doing both x and y

    # The new velocity for x is the old velocity plus some of the acceleration
    # result[1, :] = current_state[1, :] + (delta_t ** 2.0) * current_state[2, :] / 2.0
    result[1, :] = current_state[1, :] + delta_t * current_state[2, :]

    # Acceleration does not change
    result[2, :] = current_state[2, :]
    # END SOLUTION

    return result


# ---------------------- Run into the walls logic/functions ----------
#
# "Fancy" math using the formula ax + by + c = 0 half plane.
# See the slides for more details.
#
#
# This is a generalization trade-off - doing it with a half plane means I could, in theory, make any convex shape
#  instead of just a box... say a trapezoid

# BEGIN SOLUTION NO PROMPT
def outside_wall(x_y, a_b_c):
    """ Is the point outside of this half/plane representing the wall?
    @param x_y numpy array/tuple for the current location
    @param a_b_c triplet of numbers a b c
    @return True or False"""
    # TODO Return true if x_y is on the other side of the wall
    res = a_b_c[0] * x_y[0] + a_b_c[1] * x_y[1] + a_b_c[2]
    return res >= 0.0


def reflect_wall(x_y, vx_vy, a_b_c):
    """ assuming the point is outside of the half wall, reflect it back in
    @param x_y numpy array/tuple for the current location
    @param vx_vy numpy array/tuple for the current velocity
    @param a_b_c triplet of numbers a b c (a*x+b*y+c = 0 is the equation for the wall)
    @return new position, new velocity"""

    # BEGIN SOLUTION
    a = a_b_c[0]
    b = a_b_c[1]
    c = a_b_c[2]
    x = x_y[0]
    y = x_y[1]

    # The distance between the point and the wall.
    d = np.abs(a*x + b*y + c)/np.sqrt(a**2 + b**2)

    # The unit vector normal to the sloped wall.
    u_n = np.array([a,b])
    u_n = u_n / np.linalg.norm(u_n)

    # The normal element to the sloped wall of the velocity vector.
    v_n = np.dot(u_n, vx_vy)*u_n

    # Change the sign of the normal element of the velocity by subtracting doubled it.
    v_reflect = vx_vy - 2*v_n

    # Reflect the normal element of the position by subtracting the doubled normal offset.
    pt_reflect = x_y - 2*d*u_n
    
    return pt_reflect, v_reflect

    # END SOLUTION
    return x_y, vx_vy


# When you're starting, it might be easier to write a function for, eg, JUST the top wall
def outside_top_wall(x_y, y_height):
    """ Did the ball hit the "top" wall?
    @param x_y - position
    @param y_height
    @return True/False"""
    # TODO return true if x_y is on the other side of the wall
    # BEGIN SOLUTION
    return outside_wall(x_y, [0, 1, -y_height])
    # END SOLUTION
    return False


def outside_left_wall(x_y, x_wall):
    """ Did the ball hit the "left" wall?
    @param x_y - position
    @param x_wall
    @return True/False"""
    # TODO return true if x_y is on the other side of the wall
    # BEGIN SOLUTION
    return outside_wall(x_y, [-1, 0, x_wall])
    # END SOLUTION
    return False


def outside_right_wall(x_y, x_wall):
    """ Did the ball hit the "right" wall?
    @param x_y - position
    @param x_wall
    @return True/False"""
    # TODO return true if x_y is on the other side of the wall
    # BEGIN SOLUTION
    return outside_wall(x_y, [1, 0, -x_wall])
    # END SOLUTION
    return False


# ---------------------- Run into the bumpers functions ----------
#
# Similar to above, except these are circular bumpers, defined by a center x,y and a radius.

# TODO
# Define your own function here for calculating the intersection of the pinball with the bumper
# For bumper_reflection function, call the reflect_wall function but calculate a_b_c of the tangent line of the bumper.

# BEGIN SOLUTION
def inside_box(x_y, left, right, bottom, top):
    """Inside pinball box
    @param x_y point
    @param left left wall
    @param right right wall
    @param bottom bottom wall
    @param top top wall
    @ return true/false"""
    if x_y[0] < left:
        return False
    elif x_y[0] > right:
        return False
    elif x_y[1] < bottom:
        return False
    elif x_y[1] > top:
        return False
    return True


def outside_bumper(x_y, bumper):
    """Intersect with the circle of the bumper. Returns T if the point is outside the circle
    @param x_y the ball's location
    @param bumper - the bumper as a dictionary
    @ return True if outside"""
    vx = (x_y[0] - bumper["Center"][0]) ** 2
    vy = (x_y[1] - bumper["Center"][1]) ** 2
    f_xy = bumper["Radius"] ** 2 - vx - vy
    return f_xy < 0


def bumper_reflection(x_y, vx_vy, bumper):
    """Intersect with the circle of the bumper. Returns T/F if the point is inside the circle
    @param x_y the ball's location
    @param vx_vy is the ball's direction of travel
    @param bumper - the bumper as a dictionary
    @ return new x_y, vx_vy """

    # call reflect_wall (thought as the wall tangent to the bumper at the colliding point.)
    a_b_c = np.array([x_y[0] - bumper["Center"][0],x_y[1] - bumper["Center"][1],0])
    a_b_c[2] = -a_b_c[0]*x_y[0] - a_b_c[1]*x_y[1]

    return reflect_wall(x_y, vx_vy, a_b_c)
# END SOLUTION


# TODO: Put routines to check answers here
if __name__ == '__main__':
    # walls: top, left, right
    walls = [5.0, -3.0, 3.0]

    # BEGIN SOLUTION
    # Check the specialized functions
    # Checks for top wall
    assert(outside_top_wall([0, walls[0] - 0.5], y_height=walls[0]) == False)
    assert(outside_top_wall([0, walls[0] + 0.5], y_height=walls[0]) == True)

    top_wall_implicit = [0, 1, -walls[0]]
    assert(outside_wall([0, walls[0] - 0.5], top_wall_implicit) == False)
    assert(outside_wall([0, walls[0] + 0.5], top_wall_implicit) == True)

    # Left wall
    assert(outside_left_wall([walls[1] + 0.5, 0.0], x_wall=walls[1]) == False)
    assert(outside_left_wall([walls[1] - 0.5, 0.0], x_wall=walls[1]) == True)

    left_wall_implicit = [-1, 0, walls[1]]
    assert(outside_wall([walls[1] + 0.5, 0.0], left_wall_implicit) == False)
    assert(outside_wall([walls[1] - 0.5, 0.0], left_wall_implicit) == True)

    # Right wall
    assert(outside_right_wall([walls[2] - 0.5, 0.0], x_wall=walls[2]) == False)
    assert(outside_right_wall([walls[2] + 0.5, 0.0], x_wall=walls[2]) == True)

    right_wall_implicit = [1, 0, -walls[2]]
    assert(outside_wall([walls[2] - 0.5, 0.0], right_wall_implicit) == False)
    assert(outside_wall([walls[2] + 0.5, 0.0], right_wall_implicit) == True)

    # And last, but not least, the reflect function
    pt_back, vec_back = reflect_wall([0.2, walls[0] + 0.5], [0.3, 0.5], a_b_c=top_wall_implicit)
    assert(np.isclose(pt_back[0], 0.2))
    assert(np.isclose(pt_back[1], walls[0] - 0.5))
    assert(np.isclose(vec_back[0], 0.3))
    assert(np.isclose(vec_back[1], -0.5))

    pt_back, vec_back = reflect_wall([walls[1] - 0.5, 0.2], [-0.5, 0.3], a_b_c=left_wall_implicit)
    assert(np.isclose(pt_back[0], walls[1] + 0.5))
    assert(np.isclose(pt_back[1], 0.2))
    assert(np.isclose(vec_back[0], 0.5))
    assert(np.isclose(vec_back[1], 0.3))

    pt_back, vec_back = reflect_wall([walls[2] + 0.5, 0.2], [0.5, 0.3], a_b_c=right_wall_implicit)
    assert(np.isclose(pt_back[0], walls[2] - 0.5))
    assert(np.isclose(pt_back[1], 0.2))
    assert(np.isclose(vec_back[0], -0.5))
    assert(np.isclose(vec_back[1], 0.3))

    bumper = {"Center":[-3.0, 0.5], "Radius":1.0}
    assert(outside_bumper([bumper["Center"][0], bumper["Center"][1] + 0.1], bumper) == False)
    assert(outside_bumper([bumper["Center"][0] - 1.0, bumper["Center"][1] + 0.1], bumper) == True)
    pt_back, vec_back = bumper_reflection([bumper["Center"][0] + 0.9, bumper["Center"][1]], [-1.0, 0.0], bumper)
    assert(np.isclose(pt_back[0], bumper["Center"][0] + bumper["Radius"]))
    assert(np.isclose(pt_back[1], bumper["Center"][1]))
    assert(np.isclose(vec_back[0], 1.0))
    assert(np.isclose(vec_back[1], 0.0))

    # END SOLUTION
