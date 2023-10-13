import numpy as np
import lvm_read
import matplotlib.pyplot as plt
import os


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


def make_figures_for_parts_abce():
    plot_files = [
        ["lab_3/data/part_3_a.lvm", "lab_3/graphs/part_3_a.png", {
            "title": "Courant en fonction de la différence de potentiel aux bornes \nd'une résistance de 1.2 kΩ",
            "xlabel": "Différence de potentiel $∆V$ (V)",
            "ylabel": "Courant $I$ (A)"
        }],
        ["lab_3/data/part_3_b.lvm", "lab_3/graphs/part_3_b.png", {
            "title": "Courant en fonction de la différence de potentiel aux bornes \nd'un condensateur de 1 μF",
            "xlabel": "Différence de potentiel $∆V$ (V)",
            "ylabel": "Courant $I$ (A)"
        }],
        ["lab_3/data/part_3_c.lvm", "lab_3/graphs/part_3_c.png", {
            "title": "Courant en fonction de la différence de potentiel aux bornes \nd'une bobine de 1 mH",
            "xlabel": "Différence de potentiel $∆V$ (V)",
            "ylabel": "Courant $I$ (A)"
        }],
        ["lab_3/data/part_3_e.lvm", "lab_3/graphs/part_3_e.png", {
            "title": ("Courant en fonction de la différence de potentiel aux bornes \n" + 
                      "d'une diode Zener branchée en sens inverse"),
            "xlabel": "Différence de potentiel $∆V$ (V)",
            "ylabel": "Courant $I$ (A)"
        }]
    ]
    for data, save_path, params in plot_files:
        plot_graph(read_lvm(data), params=params)
        save_figure(save_path, show=True)

# make_figures_for_parts_abce()

def make_figure_for_part_d():
    zero_to_six = read_lvm("lab_3/data/part_3_d_0to6.lvm")
    zero_to_one = read_lvm("lab_3/data/part_3_d_0to1.lvm")
    global_array = np.concatenate(((zero_to_six * (-1))[::-1], zero_to_one))
    np.save("lab_3/data/concatenated_part_4.npy", global_array)
    params = {
        "title": "Courant en fonction de la différence de potentiel aux bornes \nd'une diode standard",
        "xlabel": "Différence de potentiel $∆V$ (V)", 
        "ylabel": "Courant $I$ (A)"
    }
    plot_graph(global_array, params)
    save_figure("lab_3/graphs/part_3_d.png", show=True)

# make_figure_for_part_d()

def make_figures_for_part_4():
    voltage_be = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
    arrays = read_lvm("lab_3/data/part_4.lvm")
    params = {
        "xlabel": "Différence de potentiel $∆V$ (V)", 
        "ylabel": "Courant $I$ (A)"
    }
    for voltage, array in zip(voltage_be, arrays):
        params["title"] = (r"Courant $i_{ce}$ en fonction de la tension $v_{ce}$ pour une tension $v_{be}$ de " + 
                           f"{voltage}V")
        plot_graph(array, params=params)
        save_figure(f"lab_3/graphs/part_4_{voltage}V.png", show=True)

# make_figures_for_part_4()

def make_figure_for_dvdi():
    array = np.load("lab_3/data/concatenated_part_4.npy")
    diff_array = np.diff(array, n=1, axis=0)
    plotted_array = np.stack((array[:-1,0], diff_array[:,1]/diff_array[:,0]), axis=1)
    params = {
        "title": ("Résistance dynamique $R_D$ en fonction de la différence\n" + 
                  "de potentiel aux bornes d'une diode standard"),
        "xlabel": "Différence de potentiel $∆V$ (V)", 
        "ylabel": "Résistance dynamique $R_D$ (Ω)"
    }
    plot_graph(plotted_array, params)
    save_figure("lab_3/graphs/dynamic_resistance.png", show=True)

# make_figure_for_dvdi()



