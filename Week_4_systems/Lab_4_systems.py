#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# ----- Predator-prey iterative functions ----------
# Continuing on from lec_act_4_systems - we're going to add the compute n time steps and plotting
# Slides for lab: https://docs.google.com/presentation/d/1wd1SpTJiezfroDizaFkA6UxCgMQE_A4ZKCyJoNfa0cM/edit?usp=sharing
#
# TODO 1: Copy your three functions from lec_act_4_systems to here

# YOUR CODE HERE

# Note that you could use either the number of time steps OR total time for the last parameter
#  Timesteps is a bit safer because at least you know it will only go for so many time steps...
def calculate_n_time_steps(prey_initial, predator_initial, params):
    """ Call compute one time step multiple times and store it in a numpy array
    @param prey - the starting prey value
    @param predator - the ending predator value
    @param params - the four parameters of the Lotka-Volterra system, plus delta t and time step
    @return prey,predator values as a 2xtimesteps numpy array
    """
    # TODO:
    #   Allocate a 2xn time steps numpy array to put the data in
    #   Set the first element of that data to the initial prey/predator values
    #   for the remaining values
    #     Calculate the next from the previous
    #     Store the next values in the array
    #   return the array


# Plot the prey and predator cycles.
def plot_results(prey_pred_values, params):
    """ plot the results of running the system
    @param prey_pred_values - x y values in a 2xn numpy array
    @param params - the four parameters of the Lotka-Volterra system, plus delta t and time step
    @return Nothing
    """
    nrows = 1
    ncols = 1
    fig, axs = plt.subplots(nrows, ncols, figsize=(4, 4))

    ts = np.linspace(0, params["delta t"] * params["n time steps"], params["n time steps"])
    axs.plot(ts, prey_pred_values[0, :], '-k', label="Prey")
    axs.plot(ts, prey_pred_values[1, :], ':g', label="Predator")
    axs.set_xlabel('Days')
    axs.set_ylabel('Population')
    axs.set_title(f"d prey = {params['Prey reproduce']} x - {params['Prey eaten']} x y\nd pred = {-params['Predator loss']} y + {params['Predator reproduce']} x y")
    axs.legend()


#------------------------------- Part 2, implement with ODE solver -----------
# See the instructions here: https://scientific-python.readthedocs.io/en/latest/notebooks_rst/3_Ordinary_Differential_Equations/02_Examples/Lotka_Volterra_model.html
#  -

# An example of how generalization makes things a bit confusing - the function passed TO the ode solver to calculate
#  the derivitive is defined by
#    - what the current input value is. Because the ode solver can work in any dimension, this is a numpy array. In
#     our case, we only have two dimensions. But it's up to us to "unpack" the numpy array into our variables
#    - the current time with which to calculate the derivative. For example, if dx/dt = t * x + 3, then this would
#      be the t. In our case, the derivatives do NOT depend on t, just prey/predator values, so we can ignore t
#    - one (or more) parameters specified by YOU, the caller. This is how you get "arbitrary" values into your function...
#      In the example in the link above, they pass in each "user" parameter (alpha, beta, delta, gamma) as an
#      individual paramter, using the args = () mechanism. We are just going to pass all of our parameters in
#      as a dictionary, as we did above. Note that this is (somewhat) slower because of doing the key/value extraction
#      every call
#    - The derivative function should return a numpy array of the same dimension as the input array
#  Optional: use the args approach instead.
def predator_prey_derivative(prey_predator, t, params):
    """ Slightly modified version of the derivative function from the scipy example
    @param prey_predator is current prey and predator as a tuple (X in the example above)
    @param t is ignored/not used in the predator/prey derivative - but if dx/dt DID depend on t, then here it is
    @param params - our params from before (instead of alpha, beta, delta, gamma) """
    prey, predator = prey_predator   # Cute trick to get x and y out of the tuple

    # TODO dprey_dt should be dprey_dt from your compute_prey_from_prey_and_predator (no multiplication by dt)
    #  Note: The t in the input equation is t, NOT dt - so do NOT use it in your equation
    dprey_dt = ...
    dpredator_dt = ...

    # Stitch back together into a numpy array
    return np.array([dprey_dt, dpredator_dt])


# TODO: Play around with changing alpha, beta, delta and see what happens
#   Make delta really big - what happens?
#   Make delta really small and add lots of time steps - what happens?
if __name__ == '__main__':
    delta_t = 0.1
    n_days = 40
    n_time_steps = int(n_days / delta_t)
    params_check = {"Prey reproduce":1.0,
              "Prey eaten":0.02,
              "Predator loss":1.2,
              "Predator reproduce":0.03,
              "delta t": delta_t,   # unit: days
              "n days": n_days,     # unit: days
              "n time steps": n_time_steps}

    # Make some variables
    delta_t = 0.005
    n_days = 40
    n_time_steps = int(n_days / delta_t)
    params_full = {"Prey reproduce":1.0,
              "Prey eaten":0.01,
              "Predator loss":1.2,
              "Predator reproduce":0.02,
              "delta t": delta_t,   # day
              "n days": n_days,     # unit: days
              "n time steps":n_time_steps}

    prey_initial = 100
    predator_initial = 100

    new_populations_check = calculate_n_time_steps(prey_initial=prey_initial, predator_initial=predator_initial, params=params_check)
    print(f"Last time step should be [-1.10352058e-04  2.17613504e-01] {new_populations_check[:, -1]}")

    new_populations_full = calculate_n_time_steps(prey_initial=prey_initial, predator_initial=predator_initial, params=params_full)
    plot_results(new_populations_full, params_full)

    # Now do plot results with the ode solver
    #  Notice that we turn the input into a numpy array - ode can operate on any numpy array of any dimension...
    prey_predator_initial = np.array([prey_initial, predator_initial])
    # The ode solver will return the prey/predator values at these time values
    #   Note that the ode solver will do the integration between those time steps...
    ts = np.linspace(0.0, params_full["n days"], params_full["n time steps"])

    # Crazy python parameter passing
    #  First argument is a function that takes in x,y and returns dx/dt and dy/dt
    #  Second argument is the t values to calculate for
    #  Third argument is an (optional) list of parameters - could be more than one - that get passed to the
    #    list of parameters following X, t in predator_prey_derivative
    #  Yes, this is terribly confusing, and can cause a lot of errors that are challenging to debug
    #   Python quirks - args needs to be a tuple. To make a tuple with one element, add a comma
    # TODO: Try adding another parameter to the tuple - what error do you get and why?
    new_populations_ode = integrate.odeint(predator_prey_derivative, prey_predator_initial, ts, args=(params_full, ))
    # Why is this a transpose? Because ode outputs as an n_time_steps X 2 array
    plot_results(np.transpose(new_populations_ode), params_full)
    print("Done")

