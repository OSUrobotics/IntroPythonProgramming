#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fminbound
from scipy.integrate import quad

# -------------------------lecture activity: calculus ----------------
# Practice calculus with this function:
#   f(x) = (3/x) ln(x) - x^2 / 10.0 - x / 3.0 + (x-3) * x * x

# YOUR CODE HERE


if __name__ == '__main__':
    # TODO: Plot your function to make sure it's correct
    # TODO: Find the x values of the maxima and minima between the bounds
    # TODO: Calculate the derivatives at those points (what should they be?)
    # TODO: Calculate the area under the curve

    # Check your function
    print(f"Func at 1.0 is {my_func(1.0)}, expected -2.433333")
    print(f"Func at 2.0 is {my_func(2.0)}, expected -4.02694589")

    # Integration limits
    a = 0.5
    b = 3.0

    area_under_curve = 0.0
    deriv_max = 0.0
    deriv_min = 0.0

# YOUR CODE HERE
    print(f"Max {first_max}, expected 0.94813, Min {first_min}, expected 2.091114")
    print(f"Area {area_under_curve[0]}, expected -7.90504")

    assert(np.isclose(area_under_curve[0], -7.90504, atol=0.001))
    assert(np.isclose(deriv_max, 0.0, atol=0.0001))
    assert(np.isclose(deriv_min, 0.0, atol=0.0001))
    assert(deriv_min is not 0.0)
    assert(deriv_max is not 0.0)
    print("Done")


