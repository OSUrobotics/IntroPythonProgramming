#!/usr/bin/env python3

# ---------------------- Numeric differentiation ------------------------
# Derivatives are pretty simple if you have a function - the only tricky bit is determining a good value for
#  h. Too small, and you get numerical errors. Too big and you get a poor approximation
#
# Slides: https://docs.google.com/presentation/d/1-I407aSQVEo_WJPGlZlG3Dh4AJ5vZa0rl_pXxELR2ic/edit?usp=sharing

# A generic function that we want to find the derivative of. Note that this is an actual function in this case,
# but this works for any Python function, regardless of what's in it
def my_func(x):
    """A quadratic function
    @param x the input x value
    @returns f(x)"""
    return (x-2)**2 - 3


# The analytical derivative for the function, since we can
def my_func_deriv(x):
    """A linear function
    @param x the input x value
    @returns f(x)"""
    return 2 * x - 4


if __name__ == '__main__':
    # I like to use this as a good guess for h
    h = 1e-6

    # Do derivatives at x = 0.2
    x = 0.2

    # Forward difference
    deriv_forward = (my_func(x + h) - my_func(x)) / h
    # Backwards
    deriv_backwards = (my_func(x) - my_func(x-h)) / h
    # Central
    deriv_central = (my_func(x+h) - my_func(x-h)) / (2.0 * h)

    # Analytic
    deriv_actual = my_func_deriv(x)

    print(f"Forward { deriv_forward:0.6f}")
    print(f"Backwards { deriv_backwards:0.6f}")
    print(f"Central { deriv_central:0.6f}")
    print(f"Analytic { deriv_actual:0.6f}")
