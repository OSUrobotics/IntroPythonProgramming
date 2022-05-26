#!/usr/bin/env python3


# What is matplotlib?
#
# Matplotlib does, well, plotting. Pretty much every kind of plot, from bar charts to scatter plots to images/heat maps.
# There are a TON of examples on-line, see https://matplotlib.org/. They also have cheat sheets; I like this one for
#   basic how to make the plot look the way I want: https://matplotlib.org/cheatsheets/_images/cheatsheets-2.png
#
# There are a few "quirks" with matplotlib that can cause some headaches/frustrations, but most of the functionality
#   is pretty easy to understand/use - give it data, tell it how to plot it, put some labels on it, adjust colors,
#   line widths, etc until it's legible.
#

# Need to add another import: matplotlib. If you are not in a Jupyter Notebook, then you will need to install
#  matplotlib on your machine, and include the library in your IDE.
# Why this format for an import? matplotlib has a ton of classes/functions in it. For 90% of what you need to do,
#  you only need the plot function. So, just like we indicate all numpy methods with np., we'll label all plotting
#  methods with plt.
import numpy as np
import matplotlib.pyplot as plt

# ------------- Making a plot - use case 1 -----------------------------
# We'll use made-up data to practice plotting with
#  This is a first example of setting parameters to functions by name. Note the num= and the degree=. If you
#   go to here: https://numpy.org/doc/stable/reference/generated/numpy.linspace.html and look at the parameters,
#   you'll see that it requires two of them, start and stop, (they don't have default values) but there are a lot
#   of other parameters that have default values. We've set one of them, number of elements, to be 200 instead of the
#   default 50
#
#  matplotlib makes heavy use of this feature of python (specifying one of a bunch of function parameters by name).
t_values = np.linspace(-np.pi, np.pi, num=200)
y1_values = np.sin(t_values)
y2_values = np.cos(t_values)

print(f"Num elems in array: {len(t_values)}, First sin value: {y1_values[0]}")

# This command is THE most basic plot command. This creates a window/figure, makes 1 subplot, and plots t versus y
#  This does NOT give you access to the figure or the axes
plt.plot(t_values, y1_values)

# If you want to plot TWO things in the same plot, just do another plot. It will put the second on top of the first
plt.plot(t_values, y2_values)

# And now you can label the plot
plt.xlabel('t-values')
plt.title('My Cos Sin plot')

# This resulting plot is less than ideal - what is it with orange and yellow? Let's try again, this controlling the
#  color/line style.

# Before that, though, let's clean up a bit so we don't have a lot of windows floating around
# Note that, in general, if you've set up your code properly, you don't need to do this in practice. But it's sometimes
#   handy if you're re-plotting things in the same window, so let's see what the available commands are.

# First, see what happens when you call cla (clear axes). What does the plot look like? This clears JUST the axes/plot
plt.cla()

# Ok, what happens with clf (clear figure?) This is a bit more extreme - it removes ALL of the plots in the window
plt.clf()

# And, finally, make the window go away altogether. Note that, depending on your operating system,
#  and how you're running the code, this may not take effect immediately
# Note that plt.close('all') will close all figures, plt.close(fig) will close just that figure.
plt.close()

# ------------- Making a plot - use case 1, try 2 -----------------------------

# There are three ways to set things like colors and labels. The first is to do so in the plot command itself, the
#   second is to use other commands in plot, and the third is to use variables that "hold" the plotting data - more
#   on this below with subplot and figure.
#
# For line colors, styles, markers, etc by far the easiest is to set the colors when you plot them.
# Labels and other ways to decorate plots with Useful Information are best done after you've finished plotting the
# data
#
# Here, we've set the line to be a line (-) and blue (b), used x as markers for the points, and
# labeled this data as "sin" so when we do a legend, it will have a name.
# Note the label= syntax - there are many, many parameters plot understand (see kwds).
#
# The '-b' is called the format (fmt) string. You can use this to set the line's color and marker style in one go
#  (see the cheatsheet above). It's a bit cryptic, but fairly simple once you get the hang of it
# "Markers" are what matplotlib calls the symbols that are plotted at each data point. The default assumption is that
#   you want to plot lines; if you want to draw markers only, you have to tell it to NOT draw lines and to set the
#   marker style
plt.plot(t_values, y1_values, '-b', label='sin', marker='x')

# We can keep plotting more... in this example, we'll use double dashes and one of matplotlib's default colors
plt.plot(t_values, y2_values, label='cos', color='seagreen', linestyle='dashed', linewidth=2)

# These commands add these elements to the current plot
plt.xlabel("t value")
plt.ylabel("y value")
plt.title('Sin and Cos example')

# Always save this one for last, since all of the plots need to be done by this time
#   You can give legend the list of names for each of the things you plotted, but it's a lot easier to use the
#   label='' when plotting the data instead.
# loc is where the legend appears in the figure.
plt.legend(loc='upper right')


# ----------- Use-case 2: More than one plot in a window -------------------
# If one plot is good, two must be better!
#  Sometimes you want to show more than one plot at the same time.

# I like to do this so I don't have to change all of the subplots later if I decide to add another row...
nrows = 1
ncols = 2

# Things to notice: 1) it made a new window. That's because subplots makes a new window. 2) The size of the window -
#   short and wide. You can re-size the window in the usual way
fig, axs = plt.subplots(nrows, ncols, figsize=(3, 6))

# Add a title over all the subplots
fig.suptitle("Trigonometry")

axs[0].plot(t_values, y1_values, '-b', label="Sin")
axs[0].plot(t_values, y2_values, '-g', label="Cos")
axs[0].set_title('Sin and cos')
axs[0].set_xlabel('t values')
axs[0].set_ylabel('y values')
# Notice that THIS one doesn't have a set.
axs[0].legend()   # Without explicit instructions it will put it wherever it deems best

# Now do a SECOND plot that is a circle. Notice axs[1] instead of axs[0]
axs[1].plot(y1_values, y2_values, '--b', label='circle')
axs[1].set_title('Circle')

# Notice that the circle does not look like a circle - this fixes it, by making the axes equal size.
axs[1].axis('equal')

# ------------------ Plotting gotchas ----------------------------

# This closes ALL the windows. Do this first, so we start with a clean slate below.
plt.close('all')


# One weirdness that is (usually) easy to spot, but not always obvious, is that if you DON'T give plot two arrays,
#  then it will just assume the t-values are 0, 1, etc. This is not a problem, unless it makes the first plot "disappear"
#  because the ranges of the values are so different.
plt.clf()
# Very small x range
plt.plot(np.linspace(-0.01, 0.01, 100), np.cos(np.linspace(-0.01, 0.01, 100)), '-r', label='Small cos')
# The cosine plot seems to "disappear" because it is really, really skinny wrt this plot
plt.plot(y1_values, '--b', label='Big x value')

plt.legend() # Just to prove that both plots DO exist

# matplotlib expects the x and y arrays to be the same size. If they aren't, then it raises an error
plt.clf()

# There are a couple ways this happens. One is you just created the arrays the wrong size
# eg ValueError: x and y must have same first dimension, but have shapes (10,) and (50,)
# plt.plot(np.linspace(0, 1, 10), np.linspace(0, 10), '-b')

# Sometimes you're trying to pull out data from a matrix and you drop a colon, or get the rows and columns messed up
matrix_data = np.random.random([20, 30])
# plt.plot(matrix_data[:, 0], matrix_data[0, :], '-x')

# ---------------------------- Commonly raised errors -----------------------------
# Common gotcha: When calling xlabel etc from plot, the command name is xlabel. When calling using the axes variable,
#   the command name is set_label(). If you call xlabel, you'll get the rather cryptic error:
#    TypeError: 'Text' object is not callable
# This is because axs is actually a text object...
plt.xlabel('x label')
# axs[0].xlabel('xlabel')  # Generates type error
axs[0].set_xlabel('xlabel')  # The correct command

# Just to be annoying, legend is just legend - this will cause a
#  AttributeError: 'AxesSubplot' object has no attribute 'set_legend'
# axs[0].set_legend()

# If you mess up the parameters to plot by giving it something it doesn't understand, you'll get the rather cryptic
#  error: AttributeError: 'Line2D' object has no property 'fmt'
# This is because plt.plot will pass on the parameters to a Line2D object, which doesn't know what "fmt" means
# plt.plot(t_values, y1_values, fmt='foo')

# If you get the name of the parameter right, but set it to something matplotlib doesn't understand, the error message
#   is usually a big more helpful
# ValueError: 'dash' is not a valid value for ls; supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
# plt.plot(t_values, y1_values, linestyle='dash')

