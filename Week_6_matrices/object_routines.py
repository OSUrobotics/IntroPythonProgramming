#!/usr/bin/env python3

# Mostly ways to make objects from lists of vertices
#
# Square: make a square and store it in a json file
# Wedge: Make a wedge
# Clicking: Bring up a window and let the user click points to make an object (clicking on the first point closes the
#  object)
#
# An object is just a dictionary with the vertex locations of the geometry stored in an "XYs" array.
# An object can also have a color (for drawing), and a matrix
#
# Optional:
#  You can use the function make_object_by_clicking in object_routines to make a novel object (run object_routines.py)
#  make sure to include that object's file when you hand in

import numpy as np
import matplotlib.pyplot as plt
from json import dump, load


# ----------------- Helper methods -------------------------------
def get_pts_as_numpy_array(obj):
    """ Get the points out as a 3xn array, last row 1'x (i.e., homogenous points)
    @param obj - the object
    @return numpy array of XYs"""
    pts = np.ones((3, len(obj["XYs"])))
    pts[0:2, :] = np.transpose(np.array(obj["XYs"]))

    return pts


# -------------------- Objects - creating, reading, writing ---------------------
# Create a dictionary with the required keys to be an object
def make_blank_object():
    """ XYs - the x,y points of the object as a list
        Matrix - the 3x3 matrix to move the object by
        Color - color of the object (as a matplotlib name)
        Name - name to use if needed
        Pts - the actual 3xn numpy arrame of points"""
    obj = {"XYs": [], "Matrix": None, "Color": "black", "Name": "name", "Pts": None}
    return obj


def read_object(name):
    """Read in the object from Data/name.json and convert the XYs to a numpy array
    @param name - name of the json file
    @return an object as a dictionary"""
    with open("Data/" + name + ".json", "r") as f:
        obj = load(f)
        obj["Pts"] = get_pts_as_numpy_array(obj)
        obj["Matrix"] = np.identity(3)
    return obj


def write_object(obj, name):
    """Strip out the numpy arrays before writing
    @param obj - the object
    @param name - the file name to write to"""
    obj_save_pts = obj["Pts"]
    obj_save_matrix = obj["Matrix"]

    obj["Pts"] = []
    obj["Matrix"] = []
    obj["Name"] = name

    with open("Data/" + name + ".json", 'w') as f:
        dump(obj, f, indent=2)

    obj["Pts"] = obj_save_pts
    obj["Matrix"] = obj_save_matrix


def make_square():
    """Make a square object """
    obj = make_blank_object()
    obj["XYs"] = [[-1, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]]
    obj["Name"] = "Square"
    write_object(obj, "Square")
    return obj


def make_wedge():
    """Make a wedge object """
    obj = make_blank_object()
    obj["XYs"] = [[-1, -1], [1, -0.8], [1, 0.8], [-1, 1], [-1, -1]]
    obj["Name"] = "Wedge"
    write_object(obj, "Wedge")
    return obj


# --------------------------- Plotting ------------------
def plot_object_in_own_coord_system(axs, obj):
    """Plot the object in its own coordinate system (does not apply the object matrix)
    @param axs - the axes of the figure to plot in
    @param obj - the object (as a dictionary)"""
    xs = [p[0] for p in obj["XYs"]]
    ys = [p[1] for p in obj["XYs"]]
    col = 'black'
    if "Color" in obj:
        col = obj["Color"]

    axs.plot(xs, ys, color=col, linestyle='dashed', marker='x', label=obj["Name"])
    axs.axis('equal')


def plot_object_in_world_coord_system(axs, obj, in_world_matrix=None):
    """Plot the object in the world by applying in_world_matrix (if specified) followed by the
      matrix transformation already in the object
    @param axs - the axes of the figure to plot in
    @param obj - the object (as a dictionary)
    @param in_world_matrix - an additional matrix to multiply the geometry by"""

    matrix = in_world_matrix
    if in_world_matrix is None:
        matrix = np.identity(3)

    # This only checks if the numpy array is the same size, not that the values are the same
    try:
        if len(obj["XYs"]) != obj["Pts"].shape[1]:
            obj["Pts"] = get_pts_as_numpy_array(obj)
    except:
        obj["Pts"] = get_pts_as_numpy_array(obj)

    try:
        # This multiplies the matrix by the points
        pts_in_world = matrix @ obj["Matrix"] @ obj["Pts"]
    except:
        # No matrix defined - use identity
        pts_in_world = matrix @ np.identity(3) @ obj["Pts"]

    # User-specified color
    col = 'black'
    if "Color" in obj:
        col = obj["Color"]

    axs.plot(pts_in_world[0, :], pts_in_world[1, :], color=col, linestyle='solid', label=obj["Name"])
    axs.axis('equal')


if __name__ == '__main__':

    sq = make_square()
    wedge = make_wedge()
    obj_read = read_object("Star")
    objs = [sq, wedge, obj_read]
    fig, axs = plt.subplots(1, len(objs))
    for i, o in enumerate(objs):
        axs[i].set_title(o["Name"])
        plot_object_in_own_coord_system(axs[i], o)

    # Depending on if your mac, windows, linux, and if interactive is true, you may need to call this to get the plt
    # windows to show
    plt.show()
    print("Done")
