#!/usr/bin/env python3

# -------------------HW 2: Analysis of a mass-damped system
# Resources: Lecture slides describing the homework: https://docs.google.com/presentation/d/1MwF34w30rjzLS5-IYj0ZWT5CjsLeFc7qlG_Eq9rFdZ8/edit?usp=sharing
#
# Part 1/week 3 does not build on anything specific in lab 3, but uses code from labs 1-3
# Part 2/week 4: Do lab 4 before hwk 4
#
# In the first part of this homework the focus is on doing an analysis "from scratch", in the sense that we will not be
# providing a lot of shell code. The second half is on how to translate a general equation of the form
#   state at time t+delta_t = f( state at time t )
# into code (also known as simulation).
#
# Programming practice: The focus in this assignment is on deciding when to create a function and what parameters to
#   pass in and out of the function.
#
# Following on from lab 4, the second part will be an example of writing an iterative function - one where the intention is to
#  call the function multiple times, each time passing in the values returned from the previous function call. This
#  can be a bit difficult to wrap your head around, so if you get stuck go back to the simpler examples and/or do it
#  on paper yourself a few iterations.

# We've provided results (as a json file) for two of the included data sets. We will, however, be testing on
#   different data sets, so make sure your code works for any data file of the correct format.


# Helper function 1 - load the data and check that it's valid
#  Input: File name (with path)
#  Output: Two numpy arrays, floats
#    1st numpy array: The time values
#    2nd numpy array: The function values that correspond to the time values
#  Lists should be of the same length
#
# Some expectations on the data files
#   Always has at least three rows
#     First row is a header row
#   The first column is the time values (will be monotonically increasing)
#   The second column is the values that correspond to the time values (final value of this will be greater than initial)
#
#  A good habit is to check that this is true, and throw an error if it's not

# YOUR CODE HERE
# You must name your function this
# You might also want to write some test code...
def load_data_from_file(fname):
    pass

# Helper function 2 - get the index of the first number greater than or equal the input number x
# Input: A numpy array, a single number x
# Output: The index of the first number greater than or equal to x (or None if no such number)

# YOUR CODE HERE
# You must name your function this
def greater_than_index(in_list, in_x):
    pass


# Write a function that takes in a file name and outputs a dictionary with the following values
#   You must use the names given
#      See homework slides for further definitions/equations
#   Check the corresponding json file and plot for the correct values
#
#   System values
# c_initial - the initial position of the system (the first value)
# c_max - the largest position of the system (the maximum value, see Figure 4.14)
# c_final - the final, steady-state position of the system (the last value, see Figure 4.14)
#      Note: For this assignment we'll just use the last value, but you could also average the last few values
#
#   Estimate characteristics
# rise_time - The rise time, Tr this is the time that it takes to go from 10% to 90% of the way from c_initial to c_final
#             (item 1 on Figure 4.14 - refer to plot)
#      The “10% time” is defined as the first time at which the system obtains a value greater than or equal to the
#      value which is 10% between c_initial and c_final. Same with the 90% time.
# peak_time - The peak time, Tp. This is the time at which the position has the maximal value (item 2 on Figure 4.14)
# perc_overshoot - percentage over shoot (% OS). This is the amount that the system overshoots c_final, expressed as a
#   percentage of the range c_initial to c_final.
# settling_time - The settling time, Ts. Estimate the 2% Settling Time, T_s.  This is the earliest time when the
#   current and all subsequent positions of the system are within a certain threshold of c_final. This threshold is
#   defined by 2% of the range between c_initial and c_final.
# For example, if c_initial = -1 and c_final = 1, the 2% threshold would be (0.96, 1.04) (non-inclusive of endpoints).
#
#    Estimate model values
# system_mass - assume the mass is 1
# system_spring - this is omega_n^2 (see slides)
# system_damping - the damping term (the linear coefficient, see slides)

# You should NOT write this all in one file...



# YOUR CODE HERE
# Open the filename and create a dictionary with all of the parameters
def analyze_data(fname):
    pass


# A check function for your use
# Couple notes:
#   1) Notice setting a return value to True at the top and then setting it to False at any failed test. This is a
#      common way to do this
#   2) Notice the try-except to handle a missing key, rather than using a nested if
#
def compare_dictionaries(fname_dictionary, my_dict):
    """ Open up the json file in fname and compare to my_dict
    @param fname_dictionary one of dataX.json
    @param my_dict - your dictionary with parameters
    @returns True or False if the same (within epsilon)"""
    from json import load
    with open(fname_dictionary, 'r') as fp:
        answ_dict = load(fp)

    b_ret = True
    for k, v in answ_dict.items():
        try:
            if not np.isclose(v, my_dict[k]):
                print(f"Key {k} is not close, correct value {v}, incorrect {my_dict[k]}")
                b_ret = False
        except KeyError:
            print(f"Key {k} not found in your dictionary")
            b_ret = False
    return b_ret

# ----------------------- Plot the data and the system parameters --------------------
#
# Part II Plot the data with the parameters, similar to the figure 4.14
#  Refer to figure in slides for what the figure should look like
# You should at least have c final plotted
#  - matplot lib has a text function for placing text


# An example of a "helper" function for plotting
def draw_corner(axs, x_values, y_values, ls, col):
    axs.plot([x_values[0], x_values[1]], [y_values[1], y_values[1]], linestyle=ls, color=col)
    axs.plot([x_values[1], x_values[1]], [y_values[0], y_values[1]], linestyle=ls, color=col)


# YOUR CODE HERE
# Define plot function(s) here 

# ------------------------------------ Spring-mass damp system: Creating data --------------------
#
#  In this part of the assignment you'll simulate the spring-mass system yourself. We'll follow the second half of
#  Lab 4 - using ode to do the simulation (you just have to write the derivative function and the set-up code).
#
#  This should be nearly identical to the predator_prey_derivative ode example (from a coding standpoint). The
#   equations and the meanings of the variables will be different, however
#   1) Like the c_tutorial_iterative_systems example, you will need to calculate two values dx/dt and dx2/dt2
#   2) Like the predator_prey_derivative example, you will
#        a) create a derivative function that takes in a 2 dimensional current state (x, dx/dt), t (not used), and params (c, k, and m)
#              and returns dx/dt and dx^2/d^2t
#        b) params will be a dictionary that you create in the calling code
#        c) create a set of time values to evaluate the system at
#        d) use ode to do the actual forward simulation
#  Functions you'll need
#   a) a derivative function (like predator_prey_derivative)
#   b) a function/cell to create the initial data to simulate and write out/save the results
#   c) a function that calls your code from part 1 to analyze and plot the data (do NOT write new plotting/analysis code)
#       Option 1: Write the data out to a file then read it back in using the code you just wrote in the previous part
#       Option 2: If you split up your plot function the right way, you can just pass the data directly to the plot function
#
#  Parameters:
#    c: damping term (system_damping in json file)
#    k: spring term (system_spring in json file)
#    m: mass
# Equation:
#   dx/dt = dx/dt
#   d^2x/d^2t = (-c * dx/dt - k * x) / m
#
# YOUR CODE HERE

# YOUR CODE HERE
# Re-create the plot for data 1 using the parameters you extracted in part 1 and your simulation function
#   Simulate/Plot from time 0 to time 10
#
# Create a different system with zeta 1.1, k 80, starting position -1.5 



if __name__ == '__main__':

    # load_data: load_data tests
    ts, vs = load_data_from_file("data/data1.csv")
    assert(len(ts) == len(vs))
    assert(len(ts) == 20000)
    assert(vs[-1] > vs[0])

    # get_index: get_index tests
    assert(greater_than_index(np.array([1.0, 3.0, 4.0, 7.0, 10.0]), 6.0) == 3)
    assert(greater_than_index(np.array([-2.5, 1.0, 4.0, 8.0, 4.0, 1.0, -2.5]), 4.0) == 2)
    assert(greater_than_index(np.array([1.1, 2.2, 3.3, 4.4, 5.5]), 100.5) == None)

    # analysis: analyze data tests
    assert(compare_dictionaries('Data/data1.json', analyze_data('Data/data1.csv')))
    assert(compare_dictionaries('Data/data2.json', analyze_data('Data/data2.csv')))
    assert(compare_dictionaries('Data/data3.json', analyze_data('Data/data3.csv')))

    # plot_data: Call your plot function here with each of the 3 data functions
    # plot data 1... etc

    # Begin week 2
    # ode_functions:

    # Run the ode with the following parameters and store the answer in dict_answ
    # Make sure you run the simulation long enough for it to stabilize
    # zeta = 1.1, m = 2.0, spring constant (k) = 50.0
    # set dict_answ = to be the dictionary containing the analysis of your system
    assert(compare_dictionaries('Data/sim_and_plot_answer_a.json', dict_answ))

    # plot_data1_recreate:
    # Run your simulation, analyze it, and plot the results
    # This SHOULD just be calling existing functions

    # bigger_mass:
    # Change the mass to 10, adjust the simulation time, then plot the result. Save the analysis in dict_bigger_mass
    dict_bigger_mass_analysis = {}
    # Note: this will only work in the autograder
    assert(compare_dictionaries('Data/sim_and_plot_answer_c.json', dict_bigger_mass_analysis))

    assert(np.isclose(dict_bigger_mass_analysis["settling_time"], 74.89, atol=0.1))

    print("Done")
