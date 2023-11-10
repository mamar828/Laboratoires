import numpy as np
import lvm_read
import matplotlib.pyplot as plt
import os
import scipy


def read_lvm(file_path: str) -> np.ndarray:
    """
    Read a lvm file at the specified path and return the data in the form of a numpy array.
    """
    file = lvm_read.read(file_path)
    try:
        os.remove(f"{file_path}.pkl")
    except:
        pass
    number_of_data_arrays = len(file) - 11      # Get the number of arrays in the same .lvm file
    arrays = []
    for i in range(number_of_data_arrays):      # Iterate to group all the arrays
        arrays.append(file[i]["data"])
    
    if len(arrays) == 1:                        # Crop if the list contains a single element
        return arrays[0]
    else:
        return arrays

def plot_graph(array: np.ndarray, params: dict=None):
    """
    Create a plt graph from a two dimensional numpy array.
    """
    plt.plot(array[:,0], array[:,1], "go", markersize=2)
    try:
        plt.title(params["title"])
        plt.xlabel(params["xlabel"])
        plt.ylabel(params["ylabel"])
    except:
        pass
    plt.draw()

def save_figure(file_path: str, show: bool=False):
    """
    Save a pre-rendered plt plot to the specified file_path. Kills the plt after saving if kill=True.
    """
    plt.savefig(file_path, dpi=250)
    if show:
        plt.show(block=True)


def make_power_figure():
    # Only resistance curve
    resistance_data = []
    # resistance_data.append(read_lvm("lab_5/data/lab_5_data.lvm"))
    for i in [4,6,8,10,12,14,16,18,22,24,30,32,36]:
        resistance_data.append(read_lvm(f"lab_5/data/lab_5_data_{i}.lvm"))
    
    r_global_array = np.stack((resistance_data), axis=0)
    r_dissipated_power = r_global_array[:,:,1]**2 / r_global_array[:,:,0]
    r_plotted_array = np.stack((np.mean(r_global_array[:,:,0], axis=1), np.mean(r_dissipated_power, axis=1)), axis=1)

    # Adding resistance + capacitor curve
    capacitor_data = []
    for i in [3,5,7,9,11,13,15,17,23,25,27,29,31,33]:
        capacitor_data.append(read_lvm(f"lab_5/data/lab_5_data_{i}.lvm"))

    c_global_array = np.stack((capacitor_data), axis=0)
    c_dissipated_power = c_global_array[:,:,1]**2 / c_global_array[:,:,0]
    c_plotted_array = np.stack((np.mean(c_global_array[:,:,0], axis=1), np.mean(c_dissipated_power, axis=1)), axis=1)
    
    # Plotting and setting the parameters
    for array, markertype, label in [[r_plotted_array, "go", "Circuit de la Figure 1"],
                                     [c_plotted_array, "yo", "Circuit de la Figure 2"]]:
        plt.plot(array[:,0], array[:,1], markertype, label=label, markersize=2)
    
    plt.title("Puissance moyenne dissipée [W] par la charge en fonction de la résistance [$\Omega$]")
    plt.xlabel("Résistance totale des composantes du circuit [$\Omega$]")
    plt.ylabel("Puissance moyenne dissipée [W]")
    # plt.xscale("log")
    plt.legend(loc="upper right")
    plt.show()

make_power_figure()
