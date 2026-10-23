#!/usr/bin/env python3
# Fall26

# The usual imports
import numpy as np
from scipy.signal import StateSpace, lsim
import matplotlib.pyplot as plt

# Drawing helpers and car classes for Labs 6 and 7 and Homework 2.
#   For this assignment we're going to treat a class as basically a glorified dictionary.
#   1) Instead of doing, eg, dict["my_key"] = 3, we will do self.my_key = 3.
#   2) Each function is now inside of the class (indented once) and the first parameter of most functions is "self"
#      - don't change this
#   3) Instead of creating a dictionary by, eg, my_dict = {"my_key":3}, the initial data will
#       be created in the __init__ function
#
#   That's it. The most common problem will be you'll forget the self. in front of a variable name
#
# Work in this file is labeled by assignment:
#   Lab 5  - copy draw_* from the lab notebook, then fill in QuarterCar drawing (__init__ and draw)
#   Lab 6  - copy interpolate_road, then add physics parameters, A/B/C/D, and simulate to QuarterCar
#   HW 2a  - half-car drawing mode in QuarterCar.draw, plus the HalfCar class (draw, B, simulate, ...)
#   HW 2b  - Iy fix and sprung_mass_displacement on HalfCar


# =============================================================================
# Lab 5: copy your draw_* functions from the Lab 5 notebook into this file.
# =============================================================================

# GUIDE Lab 5: Paste draw_spring, draw_damper, draw_rectangle, and draw_tire from the lab notebook.
#  QuarterCar.draw will call these functions, so they need to live here (not just in the notebook).
# GUIDES: Copy the four functions you wrote in Lab 5 Parts 1-4.
def draw_spring(axs, width, height, x=0, y=0):
    """
    Draws a spring, starting at x and y, with the given width and height.
    The spring ends in two rods that are each 5% of the total height, and the middle contains
    three coils.
    """
    # GUIDE Lab 5: Paste your draw_spring implementation from the lab notebook.
    ...
    # YOUR CODE HERE


def draw_damper(axs, x, y_u, y_s, width, height, rod_u_height, rod_s_height):
    """
    Draw a damper.
    @param axs The axs to draw the damper in.
    @param x the x coordinate to draw the damper at. the damper should be centered at x.
    @param width the width of the damper
    @param height the height of the damper.
    @param y_u the y coordinate of the unsprung mass,
    @param y_s the y coordinate of the sprung mass.
    @param rod_u_height the height of the rod stuck in the unsprung mass, and
    @param rod_s_height the height of the rod stuck in the sprung mass.
    """
    # GUIDE Lab 5: Paste your draw_damper implementation from the lab notebook.
    ...
    # YOUR CODE HERE
    # Make piston 60% of the width of the cylinder, and center it within the cylinder.


def draw_rectangle(axs, width, height, x, y, color):
    """
    Draw a rectangle with the given `width` and `height` at the given `x` and `y` coordinates.
    The lower-left corner of the rectangle should be at (x, y).
    """
    # GUIDE Lab 5: Paste your draw_rectangle implementation from the lab notebook.
    ...
    # YOUR CODE HERE


def draw_tire(axs, x, y):
    """
    Draw a tire at (x, y).
    """
    # GUIDE Lab 5: Paste your draw_tire implementation from the lab notebook.
    ...
    # YOUR CODE HERE


# =============================================================================
# Lab 6: copy interpolate_road from the Lab 6 notebook.
# HW 2a: add start_offset and stop_offset (both default to 0).
# =============================================================================

# GUIDE Lab 6: Paste interpolate_road from the Lab 6 notebook.
# GUIDE HW 2a: Add optional arguments start_offset=0 and stop_offset=0 that shift the start and end of the interpolated X coordinates.
def interpolate_road(X_r, Y_r, velocity, dt, start_offset=0, stop_offset=0):
    """
    Interpolate the road (X_r and Y_r) for a car traveling with
    the given velocity (in m/s) at timestamps every dt milliseconds.
    @param X_r numpy array containing the X coordinates of the road (in meters)
    @param Y_r numpy array containing the Y coordinates of the road (in meters)
    @param velocity of the car in m/s
    @param dt Change in time in milliseconds between interpolation points.
    @param start_offset added to the first X coordinate (HW 2a)
    @param stop_offset added to the last X coordinate (HW 2a)
    @return (X, Y) of the interpolated road, as a Python tuple
    """
    # GUIDES Lab 6: Copy your interpolate_road body from the lab notebook.
    # GUIDES HW 2a: Use start_offset and stop_offset when building the interpolated X coordinates:
    #   np.arange(X_r[0] + start_offset, X_r[-1] + stop_offset, x_dt)
    ...
    # YOUR CODE HERE


class QuarterCar:
    """
    One quarter of a car: geometry for drawing, plus the masses/springs/damper used to simulate it.

    Lab 5 fills in the drawing parameters and draw().
    Lab 6 adds the physical parameters (m_s, m_u, c_s, k_s, k_t) and the state-space simulation.
    HW 2a extends draw() so the same class can be used as the front or back of a HalfCar.
    """

    def __init__(
        self,
        w_s=1.4,
        h_s=0.1,
        w_u=0.5,
        h_u=0.1,
        w_ss=0.1,
        w_ts=0.07,
        w_c=0.14,
        h_c=0.5,
        h_rs=0.49,
        h_ru=0.09,
        d_s=0.3,
        y_s_static=1.6,
        y_u_static=0.7,
        
        # Lab 6
        m_s=210,
        m_u=53,
        c_s=10000,
        k_s=10000,
        k_t=200000,
    ):
        """
        Initialize a quarter car.
        Drawing parameters (Lab 5):
          @param w_s, h_s width/height of the sprung mass
          @param w_u, h_u width/height of the unsprung mass
          @param w_ss width of the suspension spring
          @param w_ts width of the tire spring
          @param w_c, h_c width/height of the damper cylinder
          @param h_rs, h_ru heights of the sprung/unsprung damper rods
          @param d_s distance between the suspension spring and damper
          @param y_s_static, y_u_static at-rest heights of the sprung/unsprung masses
          
        Physics parameters (Lab 6):
          @param m_s Sprung mass in kg
          @param m_u Unsprung mass in kg
          @param c_s Damping constant in Ns/m
          @param k_s Spring constant for the suspension spring in N/m
          @param k_t Spring constant for the tire in N/m
        """
        # GUIDE Lab 5: Store the drawing parameters on self (self.w_s = w_s, etc).
        # GUIDE Lab 6: Also store the physics parameters on self (self.m_s = m_s, etc).
        ...
        # YOUR CODE HERE

    def draw(self, axs, x, y_s, y_u, y_r):
        """
        Draw the quarter car at the given road location.
        @param axs axes to draw on
        @param x x position of the tire
        @param y_s adjustment of the sprung mass from y_s_static
        @param y_u adjustment of the unsprung mass from y_u_static
        @param y_r y position of the road under the tire
        """
        # y_s and y_u are adjustments over y_u_static / y_s_static.
        y_u = y_u + self.y_u_static
        y_s = y_s + self.y_s_static

        # Draw tire on the road.
        draw_tire(axs, x, y_r)

        # GUIDE Lab 5: Draw a normal quarter car (sprung mass, unsprung mass, both springs, damper).
        # GUIDE HW 2a: Extend this method so the same QuarterCar can be drawn as the front or back of a HalfCar.
        #   HalfCar sets w_s to 0 in both of its quarter cars, and sets d_s to be negative for the front one.
        # GUIDES HW 2a:
        #   1. When w_s is 0, skip drawing the sprung mass (HalfCar draws the shared, possibly tilted body).
        #   2. When w_s is 0, draw the suspension's spring directly at x.
        #   3. When w_s is 0, draw the unsprung mass so that it completely contains both the suspension's
        #      spring and damper. You will need to change its starting x value differently depending on if it's
        #      the front or back QuarterCar. You can assume that when d_s < 0, the code is dealing with a
        #      front QuarterCar.
        #   4. When d_s is negative, draw the damper in front of the spring instead of behind it
        #      (x_ss + self.d_s still works, since d_s is already negative).
        ...
        # YOUR CODE HERE
            # Draw the sprung mass, and make it red ('r'). We move the x position to be in the middle of the sprung mass.
                # Unsprung mass begins at x, with enough width to draw the spring.
        # Draw the tire spring from the road to the unsprung mass
        # Draw the damper from the unsprung mass to the sprung mass.

    def A(self):
        """Return the A matrix of the quarter-car state space model (Lab 6)."""
        # GUIDE Lab 6: Return the A matrix in the state system.
        ...
        # YOUR CODE HERE

    def B(self):
        """Return the B matrix of the quarter-car state space model (Lab 6)."""
        # GUIDE Lab 6: Return the B matrix in the state system.
        ...
        # YOUR CODE HERE

    def C(self):
        """Return the C matrix of the quarter-car state space model (Lab 6)."""
        return np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
        ])

    def D(self):
        """Return the D matrix of the quarter-car state space model (Lab 6)."""
        return np.array([[0], [0]])

    def simulate(self, velocity, dt, x_r, y_r):
        """
        Simulate the quarter car traveling down the road (Lab 6).
        Stores the results on this object (self.time, self.y_s, self.y_u, ...) instead of
        returning a separate output class.
        @param velocity Velocity of the car in the x direction in m/s.
        @param dt Timestep of the simulation in milliseconds
        @param x_r, y_r The road
        @return self (so you can write car.simulate(...).y_s if you want)
        """
        sys = StateSpace(self.A(), self.B(), self.C(), self.D())

        # GUIDE Lab 6: Use interpolate_road (the copy in this file) to interpolate the road.
        x_c, y_c = (..., ...)
        # YOUR CODE HERE

        # We need to translate x_c from an array of positions to an array of timestamps.
        # Since the car is traveling at a constant velocity, we can divide the car's
        # distance by its velocity to recover the current time (in seconds)
        time = x_c / velocity

        [_, y_out, _] = lsim(sys, y_c, time)

        # Extract the output variables
        y_s = y_out[:, 0]
        y_u = y_out[:, 1]

        # Store the simulation on this quarter car
        self.velocity = velocity
        self.time = time
        self.dt = dt
        self.x_r = x_c
        self.y_s = y_s
        self.y_u = y_u
        self.y_r = y_c
        return self


class HalfCar:
    """
    A half car: two QuarterCar suspensions plus one shared (possibly tilted) sprung mass.

    HW 2a implements drawing, the B matrix, and simulate().
    HW 2b fixes Iy and adds sprung_mass_displacement().
    """

    def __init__(
        self,
        h_s=0.1,
        w_u=0.5,
        h_u=0.1,
        w_ss=0.1,
        w_ts=0.07,
        w_c=0.14,
        h_c=0.5,
        h_rs=0.49,
        h_ru=0.09,
        d_s=0.3,
        y_s_static=1.6,
        y_u_static=0.7,
        front=None,
        back=None,
        a_f=1.4,
        a_b=1.47,
    ):
        """
        Initialize a half car.
        @param front, back optional QuarterCar instances. If not given, default ones are created
          (HW 2b Part 5 passes these in to set the physics of each half of the car).
        @param a_f, a_b distance from the center of gravity to the front and back
        The remaining parameters are the QuarterCar drawing parameters, used for the default front/back.
        """
        # GUIDE HW 2a: Create properties on self named front and back that are each a QuarterCar.
        # GUIDES HW 2a:
        #   - If front (or back) was passed in, use it. Otherwise, create a QuarterCar from the drawing
        #     parameters above with these default physics:
        #       front: m_u=53, k_s=10000        back: m_u=76, k_s=13000
        #   - Set w_s to 0 in both the front and back QuarterCar (HalfCar.draw draws the sprung mass instead).
        #   - Set d_s, the distance between the spring and damper in the suspension, to be _negative_ for the
        #     front quarter car (d_s=-d_s). QuarterCar.draw uses this to put the damper in front of the spring.
        ...
        # YOUR CODE HERE
        self.a_f = a_f
        self.a_b = a_b
        # GUIDE HW 2a: Leave Iy hardcoded at 1100 for now so Part 2 runs.
        # GUIDE HW 2b: Replace the hardcoded Iy with an approximation of the car's mass moment of inertia.
        # GUIDES HW 2b: Treat the car as a rod with an evenly distributed mass rotating about its end.
        #   The rod's length is the length of the car (a_f + a_b), and its mass is the total sprung mass
        #   (front m_s + back m_s).
        self.Iy = 1100
        # YOUR CODE HERE

    def draw(self, axs, x, y_rf, y_uf, y_rb, y_ub, y_s, a_f, a_b, theta):
        """
        Draw the half car. x is the x position of the rear tire.
        @param a_f, a_b distances from the center of gravity (usually self.a_f / self.a_b)
        """
        length = a_f + a_b

        # Calculate position of sprung mass in front and back
        y_sf = y_s - (a_f * theta)
        y_sb = y_s + (a_b * theta)

        # GUIDE HW 2a: Draw the sprung mass.
        # HINT: You cannot use draw_rectangle because the sprung mass may be at an angle,
        # and draw_rectangle does not support that. You will need to directly call axs.fill.
        ...
        # YOUR CODE HERE

        self.front.draw(axs=axs, x=x + length, y_s=y_sf, y_u=y_uf, y_r=y_rf)
        self.back.draw(axs=axs, x=x, y_s=y_sb, y_u=y_ub, y_r=y_rb)

    def m_s(self):
        """Total sprung mass (front plus back)."""
        # GUIDE HW 2a: Return the sum of the front and back m_s.
        ...
        # YOUR CODE HERE

    def A(self):
        """Return the A matrix of the half-car state space model (given)."""
        # Assigning these to a local variable makes the code below smaller.
        front = self.front
        back = self.back
        return np.array([
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [
                -(front.k_s + back.k_s) / self.m_s(),
                (front.k_s * self.a_f - back.k_s * self.a_b) / self.m_s(),
                front.k_s / self.m_s(), back.k_s / self.m_s(),
                -(back.c_s + front.c_s) / self.m_s(),
                (front.c_s * self.a_f - back.c_s * self.a_b) / self.m_s(),
                front.c_s / self.m_s(),
                back.c_s / self.m_s()
            ],
            [
                (self.a_f * front.k_s - self.a_b * back.k_s) / self.Iy,
                -(self.a_f ** 2 * front.k_s + self.a_b ** 2 * back.k_s) / self.Iy,
                -self.a_f * front.k_s / self.Iy,
                self.a_b * back.k_s / self.Iy,
                (self.a_f * front.c_s - self.a_b * back.c_s) / self.Iy,
                -((self.a_f ** 2 * front.c_s) + (self.a_b ** 2 * back.c_s)) / self.Iy,
                -self.a_f * front.c_s / self.Iy,
                self.a_b * back.c_s / self.Iy
            ],
            [
                front.k_s / front.m_u,
                -self.a_f * front.k_s / front.m_u,
                -(front.k_s + front.k_t) / front.m_u,
                0,
                front.c_s / front.m_u,
                -self.a_f * front.c_s / front.m_u,
                -front.c_s / front.m_u,
                0
            ],
            [
                back.k_s / back.m_u,
                back.k_s * self.a_b / back.m_u,
                0,
                -(back.k_s + back.k_t) / back.m_u,
                back.c_s / back.m_u,
                back.c_s * self.a_b / back.m_u,
                0,
                -back.c_s / back.m_u
            ],
        ])

    def B(self):
        """Return the B matrix of the half-car state space model (HW 2a)."""
        # GUIDE HW 2a: Define B.
        ...
        # YOUR CODE HERE

    def C(self):
        """Return the C matrix of the half-car state space model (given)."""
        return np.array([
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
        ])

    def D(self):
        """Return the D matrix of the half-car state space model (given)."""
        return np.zeros((4, 2))

    def simulate(self, velocity, dt, x_r, y_r):
        """
        Simulate the half car traveling down the road (HW 2a).
        Stores the results on this object (self.y_s, self.theta, self.y_uf, ...) instead of
        returning a separate output class.
        @param velocity Velocity of the car in the x direction in m/s.
        @param dt Timestep of the simulation in milliseconds
        @param x_r, y_r The road
        @return self
        """
        # State space model
        sys = StateSpace(self.A(), self.B(), self.C(), self.D())

        # We need the x and y positions of both tires on the road. In the real world, the angle of the car
        # would influence the x displacement between the front and rear tire. But in our simplified model,
        # the x displacement between the tires is always the length of the car:
        #   x_rf - x_rb = a_f + a_b
        #
        # So, when traveling down our road:
        # * The rear tire will travel from first_road_position to final_road_position - self.a_f - self.a_b
        # * The front tire will travel from first_road_position + self.a_f + self.a_b to final_road_position

        # GUIDE HW 2a: Use interpolate_road to define x_rb, y_rb, x_rf, and y_rf.
        # GUIDES HW 2a: Use the start_offset and stop_offset arguments you added to interpolate_road to shift
        #   where each tire starts and stops (see the comment above). Both tires use the same x_r, y_r,
        #   velocity, and dt.
        #   Note: x_rf will never actually be used.
        x_rb, y_rb = (..., ...)
        x_rf, y_rf = (..., ...)
        # YOUR CODE HERE

        # Input variables are in a matrix where each column is an input variable,
        # and the `i`th row is the value of those input variables at time `time[i]`.
        y_c = np.array([
            y_rf,
            y_rb,
        ]).transpose()

        # Since x_rb begins at first_road_position, we'll use it to define time and as the x position of the car.
        time = x_rb / velocity
        [_, y_out, _] = lsim(sys, y_c, time)

        # Extract the output variables. Each column is a specific output variable over time.
        y_s = y_out[:, 0]
        theta = y_out[:, 1]
        y_uf = y_out[:, 2]
        y_ub = y_out[:, 3]

        self.velocity = velocity
        self.time = time
        self.dt = dt
        self.x_r = x_rb
        self.y_rf = y_rf
        self.y_rb = y_rb
        self.y_s = y_s
        self.theta = theta
        self.y_uf = y_uf
        self.y_ub = y_ub
        return self

    def sprung_mass_displacement(self):
        """
        Vertical vibration of the sprung mass relative to the road under the rear tire (HW 2b).
        Call simulate() first so self.y_s, self.theta, and self.y_rb exist.
        """
        # GUIDE HW 2b: Return y_s + (a_b * theta) - y_rb using the values stored on self.
        # GUIDES HW 2b: This is the same calculation you did in the HW 2b notebook (Part 4), but using
        #   self.y_s, self.theta, self.y_rb, and self.a_b.
        ...
        # YOUR CODE HERE


if __name__ == '__main__':
    # Lab 5: drawing attributes exist on a default QuarterCar
    qc = QuarterCar()
    assert qc.w_s == 1.4
    assert qc.h_s == 0.1
    assert qc.y_s_static == 1.6
    assert qc.y_u_static == 0.7
    print("Lab 5: QuarterCar drawing init passed!")

    # Lab 6: physics attributes exist with the lab defaults
    assert qc.m_s == 210
    assert qc.m_u == 53
    assert qc.c_s == 10000
    assert qc.k_s == 10000
    assert qc.k_t == 200000
    assert qc.A().shape == (4, 4)
    assert qc.B().shape == (4, 1)
    print("Lab 6: QuarterCar physics init passed!")

    # Lab 6: interpolate_road and a short simulation
    x_road = np.array([0.0, 5.0, 11.0])
    y_road = np.array([0.0, 0.0, 0.0])
    x_c, y_c = interpolate_road(x_road, y_road, velocity=10, dt=10)
    assert len(x_c) == len(y_c)
    assert x_c[0] == 0.0
    qc.simulate(velocity=10, dt=10, x_r=x_road, y_r=y_road)
    assert qc.y_s is not None
    assert len(qc.y_s) == len(qc.time)
    print("Lab 6: interpolate_road and simulate passed!")

    # HW 2a: HalfCar defaults and B matrix
    hc = HalfCar()
    assert hc.front.w_s == 0
    assert hc.back.w_s == 0
    assert hc.front.d_s < 0
    assert hc.back.d_s > 0
    assert hc.a_f == 1.4
    assert hc.a_b == 1.47
    assert hc.B().shape == (8, 2)
    print("HW 2a: HalfCar init and B passed!")

    # HW 2a: half-car simulation stores results on self
    hc.simulate(velocity=10, dt=10, x_r=x_road, y_r=y_road)
    assert hc.y_s is not None
    assert hc.theta is not None
    assert len(hc.y_rf) == len(hc.y_rb)
    # paste_source_tracking: true
    print("HW 2a: HalfCar.simulate passed!")

    # HW 2b: Iy approximation and sprung-mass displacement (skipped until you start HW 2b)
    if hc.Iy == 1100:
        print("HW 2b: skipped (Iy is still hardcoded to 1100)")
    else:
        assert hc.Iy > 0, "Iy should be positive"
        longer_hc = HalfCar(a_f=hc.a_f * 2, a_b=hc.a_b * 2)
        assert longer_hc.Iy > hc.Iy, "A longer car should have a larger Iy"
        vib = hc.sprung_mass_displacement()
        assert vib is not Ellipsis, "sprung_mass_displacement still needs to be implemented"
        assert len(vib) == len(hc.y_s)
        print("HW 2b: Iy and sprung_mass_displacement passed!")

    print("Done!")
