#!/usr/bin/env python3
# I25

import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import polynomial

"""
A 2d skiing simulation.

Components:
- Ground/terrain: the ground the skier is traveling over
- Skier: The skier is subject to gravity, skis until falls off the edge, and can become airborne if travelling fast enough: Optionally
  -- Stops if crashes into the ground too hard
  -- Can bounce when hitting ground
  -- Assuming mass of skier is 1

There are tests for the basic math components (computing the next time step, computing a crash, determining if airborne).
There is a class-based framework you can use to structure your code; you do not HAVE to use it, but the guided instructions assume
you are using it.

There is one class for the ground/terrain, and once class for the skier.
- Ground/terrain: Handles computing the slope of the terrain, and where the cliff/drop is
- Skier: Handles the simulation and saves the position/velocities
"""

class Skier:
    def __init__(self, x_y=(0, 0), vx_vy = (1, 0)):
        """ Initialize with position and velocity
        @param x_y x, y location
        @param vx_vy velocity"""

        # YOUR CODE HERE

    def turn_on_bounce(self):
        """ Turn bouncing on (off by default)"""
        # YOUR CODE HERE

    def set_crash_velocity(self, y_vel):
        """ Crashes if hits ground with y velocity bigger than y_vel
        @param y_vel - the velocity at which a crash happens"""
        # YOUR CODE HERE

    def position(self):
        """ Return the current position as a tuple"""
        # YOUR CODE HERE

    def velocity(self):
        """ Return the current velocity as a tuple"""
        # YOUR CODE HERE
    
    def acceleration(self):
        """ Return the current acceleration as a tuple"""
        # YOUR CODE HERE
    
    def n_saved_poses(self):
        """Return the number of saved poses"""    
        # YOUR CODE HERE
    
    def saved_poses(self):
        """Return the saved pose at the given index (may be a range)
        @returns - 2xn array of poses"""
        # YOUR CODE HERE
    
    def is_airborne(self):
        """ Return current airborne state (True/False)"""
        # YOUR CODE HERE

    def compute_next_state(self, ground, delta_t=0.01):
        """ 1) Save the last position/velocity/airborne
            2) Calculate the new position and velocity using Euler equations (x1 = x0 + v0 * delta_t)
            3) Calculate new airborne from new position
        NOTE: bouncing/collisions/acceleration will be handled after this
        @param ground - an instance of Ground
        @param delta_t - time step to use"""
        # A reminder to use np.copy if you are using numpy arrays
        # YOUR CODE HERE

    def compute_acceleration(self, ground):
        """ Calculate acceleration given the current position
        If airborne or past the end of the ground set acceleration to (0, gravity), otherwise, 
              calculate acceleration using slope of ground at current location 
        See any tutorial on calculating acceleration on an inclined plane (https://www.physicsclassroom.com/class/vectors/Lesson-3/Inclined-Planes)
        Friction: If doing friction, then friction resists the 
        @param ground - an instance of Ground"""

        # YOUR CODE HERE
            slope_theta = ground.slope(*self.current_state[0, :])   # slope (theta)

    def is_crash(self, ground):
        """ Determine if a crash happened between last time step and this
        Crash happened if: 1) were airborne last time step
                           2) now below/on ground
                           3) magnitude of velocity in y direction bigger than max allowed
                           [Note: y velocities will be negative, check magnitude]
        @param ground - an instance of ground
        @returns True if crash, False otherwise"""
        # YOUR CODE HERE

    def compute_bounce(self, ground):
        """ If doing a bounce, and skier has passed through the ground (last pose was airborne and now below or on ground)
        See, for example, https://www.contemporarycalculus.com/dh/Calculus_all/CC11_7_VectorReflections.pdf
        1) change the height to have bounced off the ground (however far traveled below ground, add to ground height)
        2) invert the y component of the velocity
        3) update airborne

        Note: Simplify the math by finding the rotate/translate that takes the point x, y_ground to the origin and 
        the normal of the ground to 0, 1 (rotate by -slope)
        Normal of the ground is -sin(theta), cos(theta)

        If NOT doing bounce, but under ground, just put the skier back on the ground
        @param ground - an instance of ground"""

        # YOUR CODE HERE
            

    def one_time_step(self, ground, delta_t=0.01):
        """Move the state forward one time step
          then, do in the following order
              1) determine if crash (hit ground harder than given y velocity max) - if crash, return False
              2) compute bounce (if any)
              3) compute new acceleration based on current location
        @ground - an instance of Ground
        @delta_t - the time step to use
        @returns True if stop simulation, False otherwise """
        # YOUR CODE HERE

    def simulate(self, ground, delta_t=0.01, eps=0.01):
        """
        Simulate forward, until either reach the end of the ground, stop moving, or crash (if enabled)
        @param ground the ground
        @param delta_t - the time step to use
        @param eps - fudge factor for determining if skier on the ground"""
        # YOUR CODE HERE
        # convert list to array

    def plot(self, axs):
        """ Plot the skier's path
        @param axs - the axes to plot into"""
        # YOUR CODE HERE


class GroundSection:
    def __init__(self, x_start, x_end, polynomial_coefs=(0, 0)):
        """
        @param x_start What x value to start at
        @param x_end What x value to end at
        @param polynomial coeficients for the section y(x) = a0 x^2 + a1 x + a2
        """
        # YOUR CODE HERE

    @staticmethod
    def gravity_acceleration():
        """Somewhat silly - but if we need to change it, then we can  change it just here"""
        gravity = -9.8     # m/s
        return gravity
    
    def is_between(self, x):
        """ Is the x value between the start and end x value?
        @param x the x value 
        @ return True or False
        """
        # YOUR CODE HERE

    def height(self, x):
        """ Return the height, given the x (assumes over the ground)
        @param x - x value
        @returns height f(x)"""
        # YOUR CODE HERE
    
    def is_over(self, x, y):
        """ Is the x,y point over the segment? 
        @param x - the x position
        @param y - the y position
        @ return True or False
        """
        # YOUR CODE HERE
    
    def is_on(self, x, y, eps=0.01):
        """ Is the x,y point on the segment within epsilon error? 
        @param x - the x position
        @param y - the y position
        @param eps - the allowable error
        @ return True or False
        """
        # YOUR CODE HERE

    # YOUR CODE HERE
    
    def plot(self, axs):
        """Plot the section
        @param axs the figure to plot into"""

        # YOUR CODE HERE


""" A sequence of GroundSections where the end of one section matches the start of the next
     always starts at a height of 10"""
class Ground:
    def __init__(self, x_breaks=(0, 1, 2), y_start = 10.0, slopes_or_curves=(-0.5, (0.5, 0.5))):
        """
        Ground - consists of linear pieces of ground with (optional) quadratic pieces

        @param x_breaks - the breaks between the sections
        @param y_start - the y value to start with
        @param slopes_or_curves - a list, with the slope of the line segment or the curve of the quadratic and where to start
        """
        # TODO Make one GroundSegment for each item in slopes_or_curves
        #    Make sure the end point of the last one matches up with the start point of the next one
        # YOUR CODE HERE

    # YOUR CODE HERE
    
    def is_airborne(self, x, y, eps=0.001):
        """ Is the location on the ground (or over), with epsilon error fudge
        @param x - x location of skier
        @param y - y location of skier
        @param eps - fudge factor, true if y > surface + eps
        @returns True if y > surface + eps (false otherwise)"""
        
        # YOUR CODE HERE
            
    def is_past_end_of_ground(self, x):
        """is the skier past the end of the ground?
        @param x - x location
        @returns True/False"""
        # YOUR CODE HERE
    
    def height(self, x):
        """ What is the height of the ground under the skier?
        @param x - x location of skier
        @returns f(x) for the current skier, or a big negative value if not over ground"""
        
        # YOUR CODE HERE

    def plot(self, axs):
        """Plot the section
        @param axs the figure to plot into"""

        # YOUR CODE HERE


if __name__ == '__main__':
    # Plots for debugging
    fig, axs = plt.subplots(3, 4, figsize=(12, 8))

    # Create and test a single, horizontal linear segment at height 1
    #   polynomial is p0 + p1 x + p2 x^2... etc
    flat_bit = GroundSection(-0.5, 1.0, polynomial_coefs=(1, 0))
    assert flat_bit.is_on(0.0, 1.0)
    assert not flat_bit.is_between(-0.6)
    assert flat_bit.is_between(-0.5)
    assert flat_bit.is_between(0.0)    
    assert flat_bit.is_between(1.0)    
    assert not flat_bit.is_between(1.1)
    assert flat_bit.is_over(0.1, 1.2)
    assert np.isclose(flat_bit.height(0.0), 1.0)
    assert np.isclose(flat_bit.slope(0.0), 0.0)
    flat_bit.plot(axs[0, 0])
    axs[0, 0].set_title("Flat bit")

    # Create and test a slightly descending straight line
    #   Starts at 1 and drops by 0.25
    slope_down_bit = GroundSection(1.0, 1.5, polynomial_coefs=(1.0 + 0.25, -0.25))
    assert slope_down_bit.is_on(1.0, 1.0)
    assert slope_down_bit.is_on(1.5, -0.25 * 0.5)
    assert not slope_down_bit.is_between(0.9)
    assert slope_down_bit.is_between(1.0)
    assert slope_down_bit.is_between(1.25)    
    assert slope_down_bit.is_between(1.5)    
    assert not slope_down_bit.is_between(1.6)
    assert slope_down_bit.is_over(1.25, 1.0)
    assert np.isclose(slope_down_bit.height(1.0), 1.0)
    # YOUR CODE HERE
    slope_down_bit.plot(axs[0, 1])
    axs[0, 1].set_title("slope down bit")

    # Create and test a parabola
    #   Interpolates the points (0, 2), (1, 1), (3, 2)
    parabola = GroundSection(0.0, 2.0, polynomial_coefs=(2.0, -3.0/2.0, 1.0/2.0))
    assert parabola.is_on(0.0, 2.0)
    assert parabola.is_on(1.0, 1.0)
    assert not parabola.is_between(-0.1)
    assert parabola.is_between(1.0)
    assert not slope_down_bit.is_between(2.1)
    assert parabola.is_over(1.0, 1.5)
    assert np.isclose(parabola.height(0.0), 2.0)
    assert np.isclose(parabola.height(3.0), 2.0)
    # YOUR CODE HERE
    parabola.plot(axs[0, 2])
    axs[0, 2].set_title("parabola bit")

    # This ground is a straight line, x in (0,1), slope -0.5, and starting at y=10
    slope_ground_simple = -0.5
    ground_simple = Ground(x_breaks=(0.0, 10.0), y_start=10, slopes_or_curves=((slope_ground_simple,),))
    assert np.isclose(ground_simple.height(0.0), 10.0)
    assert np.isclose(ground_simple.height(1.0), 10.0 + slope_ground_simple)
    # YOUR CODE HERE
    # Next row of plots (on ground, airborne, airborne bounce, airborne crash)
    for ind in range(0, 4):
        ground_simple.plot(axs[1, ind])

    # Now build the ground out of a downward slope, a flat bit, then a "ski jump"
    ground = Ground(x_breaks=(0.0, 2.0, 4.5, 10.0), y_start=10, slopes_or_curves=((-2.0,), (0.0,), (3.5, -4.0)))
    ground.plot(axs[0, 3])
    axs[0, 3].set_title("Ground, three bits")

    """ Checking one time step calculation, bounce, and crash """
    # Same for all examples
    delta_t = 0.025
    eps = 0.001

    # Skier is airborne - check calculated position, velocity, acceleration, airborne
    x_y_a = (0, 10)
    vx_vy_a = (2.0, 2.0 * 4.0)
    skier_airborne = Skier(x_y_a, vx_vy_a)
    skier_airborne.one_time_step(ground_simple, delta_t=delta_t)
    assert skier_airborne.position() == (x_y_a[0] + delta_t * vx_vy_a[0], x_y_a[1] + delta_t * vx_vy_a[1])
    assert skier_airborne.velocity() == (vx_vy_a[0], vx_vy_a[1] + GroundSection.gravity_acceleration() * delta_t)
    assert skier_airborne.acceleration() == (0.0, GroundSection.gravity_acceleration())
    assert skier_airborne.is_airborne()
    skier_airborne.simulate(ground=ground_simple, delta_t=delta_t, eps=eps)
    skier_airborne.plot(axs[1, 0])
    axs[1, 0].set_title('Skier airborne')
    axs[1, 0].legend()

    # Skier is on ground - check calculated position, velocity, acceleration, airborne
    x_y_g = (0, ground_simple.height(0))
    vx_vy_g = (0.5, 0.5 * slope_ground_simple)   # slope 
    skier_ground = Skier(x_y_g, vx_vy_g)
    # Skier is on ground - check calculated position and velocity
    skier_ground.one_time_step(ground_simple, delta_t=delta_t)
    assert skier_ground.position() == (x_y_g[0] + delta_t * vx_vy_g[0], x_y_g[1] + delta_t * vx_vy_g[1])
    angle_ground = ground_simple.slope(x_y_g[0], x_y_g[1])

    assert not skier_ground.is_airborne()
    skier_ground.simulate(ground=ground_simple, delta_t=delta_t, eps=eps)
    skier_ground.plot(axs[1, 1])
    axs[1, 1].set_title('Skier not airborne')
    axs[1, 1].legend()

    # Skier starts airborne and crashes
    skier_crash = Skier(x_y_a, vx_vy_a)
    skier_crash.set_crash_velocity(y_vel=2.0)
    skier_crash.simulate(ground=ground_simple, delta_t=delta_t, eps=eps)
    assert skier_crash.saved_poses()[0, -1] < 10.0
    skier_crash.plot(axs[1, 2])
    axs[1, 2].set_title('Skier crashes')
    axs[1, 2].legend()

    # Skier starts airborne and bounces
    skier_bounce = Skier(x_y_a, vx_vy_a)
    # Should be bigger than the velocity at bounce
    skier_bounce.turn_on_bounce()    # tell the skier to bounce
    skier_bounce.simulate(ground=ground_simple, delta_t=delta_t, eps=eps)
    b_found_bounce = False
    for ind in range(10, skier_bounce.n_saved_poses()):
        if skier_bounce.saved_poses()[1, ind] > skier_bounce.saved_poses()[1, ind-1]:
            b_found_bounce = True
    assert b_found_bounce == True
    skier_bounce.plot(axs[1, 3])
    axs[1, 3].set_title('Skier bounces')
    axs[1, 3].legend()

    skier_jump = Skier(x_y_a, (1.3, 0.1))
    skier_jump.simulate(ground=ground, delta_t=delta_t, eps=eps)
    skier_jump.plot(axs[2, 0])
    axs[2, 1].set_title('Skier jump')
    ground.plot(axs[2, 0])
    axs[2, 0].legend()

    ground_zigzag = Ground(x_breaks=(0.0, 2.0, 8.0, 10.0), y_start=2, slopes_or_curves=((-0.25, ), (2, -2.0), (0.55, )))
    skier_zigzag = Skier((3.5, ground_zigzag.height(3.5)), (0.5, 0.0))
    skier_zigzag.simulate(ground=ground_zigzag, delta_t=delta_t, eps=eps)
    skier_zigzag.plot(axs[2, 1])
    axs[2, 1].set_title('Skier zig zag')
    ground_zigzag.plot(axs[2, 1])
    axs[2, 1].legend()

    axs[2, 2].set_title('Your plot here')
    axs[2, 3].set_title('Your plot here')

    fig.tight_layout()
    plt.show()
    print("Passed tests!")