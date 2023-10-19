#!/usr/bin/env python3

import numpy as np

# ----- Predator-prey iterative functions ----------
#
#  We're going to start implementing a simple version of the predator/prey relationship, a classic differential
#  equations problem also known as the Lotka-Volterra equations. You don't need to know a whole lot about them,
#  except that there are two variables to track - prey and predator - and that how the numbers of prey/predator
#  changes depends on both the current prey values AND the predator values
#  Resources:
#   https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations for a more general theoretical introduction
#   https://www.kristakingmath.com/blog/predator-prey-systems a better "what is it" description
#   https://scientific-python.readthedocs.io/en/latest/notebooks_rst/3_Ordinary_Differential_Equations/02_Examples/Lotka_Volterra_model.html -
#    implementation in sci-py (which is what you should really use for this - the ode solver)

# In this pre-lecture activity: You're going to 1) practice writing a function from a function description 2) practice
#  turning a bit of math into an iterative function 3) practice calling functions from functions
#
# Also see the slides for the lab: https://docs.google.com/presentation/d/1wd1SpTJiezfroDizaFkA6UxCgMQE_A4ZKCyJoNfa0cM/edit?usp=sharing
#
#  Note: You can write the entire solver in one function. But that's a) rather hard to debug and b) can result in
#   making the most common mistake with iterative functions - not computing the new values from the old ones.

# TODO: Fill in these three functions
# First function - compute the new prey value from the prey and predator
#   Input: Current prey value (number), current predator value (numer), the parameters as a dictionary (see calling
#     function)
#   Output: New prey value (number)
#   Equation:
#      dprey/dt = "Prey reproduce" * prey - "Prey eaten" * prey * predator
#      prey = prey + delta_t * dprey/dt
#   Function name: Use compute_prey_from_prey_and_predator

# YOUR CODE HERE

# Second function - compute the new predator value from the prey and predator
#   Input: Current prey value (number), current predator value (numer), the parameters as a dictionary (see calling
#     function)
#   Output: New predator value (number)
#   Equation:
#      dpredator/dt = - "Predator loss" * predator + "Predator reproduce" * prey * predator
#      predator = predator + delta_t * dpredator/dt
#   Function name: Use compute_predator_from_prey_and_predator
# YOUR CODE HERE


# Third function - Put the two functions together
#   Input: Current prey value (number), current predator value (numer), the parameters as a dictionary (see calling
#     function)
#   Output: New prey, predator values (tuple)
#   Equations: See above
#   Function name: Use compute_one_time_step
# YOUR CODE HERE


# Check functions
if __name__ == '__main__':
    # Make some variables - note, these values are set in order to create noticeable differences in the values, not
    #  to make a stable system (i.e., do NOT use them in the lab)
    delta_t = 0.1
    n_days = 40
    n_time_steps = int(n_days / delta_t)
    params = {"Prey reproduce":1.0,
              "Prey eaten":0.02,
              "Predator loss":1.2,
              "Predator reproduce":0.03,
              "delta t": delta_t,   # day
              "n time steps":n_time_steps}

    prey_initial = 100
    predator_initial = 100

    prey_new = compute_prey_from_prey_and_predator(prey=prey_initial, predator=predator_initial, params=params)
    predator_new = compute_predator_from_prey_and_predator(prey=prey_initial, predator=predator_initial, params=params)

    print(f"Checking prey new {prey_new}, should be 90 predator new {predator_new}, should be 118")
    assert(np.isclose(prey_new, 90))
    assert(np.isclose(predator_new, 118))

    prey_new2, predator_new2 = compute_one_time_step(prey_initial, predator_initial, params)
    assert(np.isclose(prey_new, prey_new2))
    assert(np.isclose(predator_new, predator_new2))
    print(f"Checking prey new {prey_new2}, should be 90 predator new {predator_new2}, should be 118")

    print("Done")

