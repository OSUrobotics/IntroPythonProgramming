#!/usr/bin/env python3

import numpy as np
from scipy.integrate import quad


# ---------------------- Numeric integration ------------------------
#
# Slides: https://docs.google.com/presentation/d/1-I407aSQVEo_WJPGlZlG3Dh4AJ5vZa0rl_pXxELR2ic/edit?usp=sharing

# Compute the integral of cosine from a to b in 3 ways
#  trapz (generate samples, sum samples)
#  quad (use a function)
#  analytical - use the fact that the integral of cosine is sine


if __name__ == '__main__':
    # Integration limits - make sure the code works with any values of a and b
    #  TODO: if you make the interval really big (or the number of samples in trapz much smaller) how does the
    #   accuracy degrade?
    a = -np.pi / 2.0
    b = 2.0 * np.pi

    # Using trapz (TODO)
    #  Use linspace to generate samples from a to b
    #  Calculate cosine of those samples
    #  Use numpy's trapz to calculate the integral
    #    Don't forget that trap z takes the y's then the x's
    n_samples = 100
    area_trapz = 0.0
    # BEGIN SOLUTION
    ts = np.linspace(a, b, n_samples)
    ys = np.cos(ts)
    area_trapz = np.trapz(ys, ts)
    # END SOLUTION
    print(f"Area with {n_samples} samples, trapz {area_trapz:0.4f}")

    # Using quad (TODO)
    #  You can use np.cos as the function...
    #  Remember that quad returns several parameters - you want the first
    area_quad = [0.0, 0.0]
    # BEGIN SOLUTION
    area_quad = quad(np.cos, a, b)
    # END SOLUTION
    print(f"Area with quad {area_quad[0]:0.4f}")

    # Using analytical integration
    # TODO: Remember, integral of cosine is sine
    #   Evaluate sine at the two end points... b - a
    area_analytic = 0.0
    # BEGIN SOLUTION
    area_analytic = np.sin(b) - np.sin(a)
    # END SOLUTION
    print(f"Area analytic {area_analytic:0.4f}")

    # ---------------------------- Answers ---------------------------
    # Using trapz
    ts = np.linspace(a, b, n_samples)
    ys = np.cos(ts)
    area_trapz = np.trapz(ys, ts)

    # Using quad
    area_quad = quad(np.cos, a, b)

    # Analytic
    area_analytic = np.sin(b) - np.sin(a)

