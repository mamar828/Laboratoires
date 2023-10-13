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
    print(file)
    print(len(file))
    return file[0]["data"]

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


plot_files = [
    ["lab_3/data/part_3_a.lvm", "lab_3/graphs/part_3_a.png", {
        "title": "Différence de potentiel aux bornes \nd'une résistance de 1.2 kΩ en fonction du courant",
        "xlabel": "Différence de potentiel $∆V$ (V)", "ylabel": "Courant $I$ (A)"}],
    ["lab_3/data/part_3_b.lvm", "lab_3/graphs/part_3_b.png", {
        "title": "Différence de potentiel aux bornes \nd'un condensateur de 1 μF en fonction du courant",
        "xlabel": "Différence de potentiel $∆V$ (V)", "ylabel": "Courant $I$ (A)"}],
    ["lab_3/data/part_3_c.lvm", "lab_3/graphs/part_3_c.png", {
        "title": "Différence de potentiel aux bornes \nd'une bobine de 1 mH en fonction du courant",
        "xlabel": "Différence de potentiel $∆V$ (V)", "ylabel": "Courant $I$ (A)"}],
    ["lab_3/data/part_3_e.lvm", "lab_3/graphs/part_3_e.png", {
     "title": "Différence de potentiel aux bornes \nd'une diode Zener branchée en sens inverse en fonction du courant",
        "xlabel": "Différence de potentiel $∆V$ (V)", "ylabel": "Courant $I$ (A)"}]
]

def make_figures_for_parts_abce():
    for data, save_path, params in plot_files:
        plot_graph(read_lvm(data), params=params)
        save_figure(save_path, show=True)

# make_figures_for_parts_abce()

def make_figure_for_part_d():
    zero_to_six = read_lvm("lab_3/data/part_3_d_0to6.lvm")
    zero_to_one = read_lvm("lab_3/data/part_3_d_0to1.lvm")
    global_array = np.concatenate(((zero_to_six * (-1))[::-1], zero_to_one))
    params = {
        "title": "Différence de potentiel aux bornes \nd'une diode standard en fonction du courant",
        "xlabel": "Différence de potentiel $∆V$ (V)", 
        "ylabel": "Courant $I$ (A)"
    }
    plot_graph(global_array, params)
    save_figure("lab_3/graphs/part_3_d.png", show=True)

# make_figure_for_part_d()

# read_lvm("lab_3/data/part_4.lvm")




