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


def get_dissipated_power(filename: str) -> tuple:
    data = read_lvm(filename)
    # plt.hist(data[:,0])
    # plt.show()
    resistance = np.mean(data[:,0]), np.std(data[:,0])
    potential  = scipy.stats.mode(data[:,1]).mode[0], 0.0005
    power = (
        potential[0]**2 / resistance[0], 
        (potential[1] / potential[0] * 2 + resistance[1] / resistance[0]) * potential[0]**2 / resistance[0]
    )
    return resistance, potential, power


# print(get_dissipated_power("lab_5/data_new/capacitor/part_4_6.lvm"))



def make_power_figure():
    # Resistance curve
    resistance_values = []
    resistance_powers = []
    for part_no in range(1,24):
        resistance, potential, power = get_dissipated_power(f"lab_5/data_new/resistance/part_1_{part_no}.lvm")
        resistance_values.append(resistance)
        resistance_powers.append(power)

    # Resistance curve
    capacitor_values = []
    capacitor_powers = []
    for part_no in range(1,23):
        resistance, potential, power = get_dissipated_power(f"lab_5/data_new/capacitor/part_4_{part_no}.lvm")
        capacitor_values.append(resistance)
        capacitor_powers.append(power)

    r_v_array = np.array(resistance_values)
    r_p_array = np.array(resistance_powers)
    c_v_array = np.array(capacitor_values)
    c_p_array = np.array(capacitor_powers)

    plt.errorbar(r_v_array[:,0], r_p_array[:,0], xerr=r_v_array[:,1], yerr=r_p_array[:,1], markersize=2, fmt="go",
                 label="Circuit 1")
    plt.errorbar(c_v_array[:,0], c_p_array[:,0], xerr=c_v_array[:,1], yerr=c_p_array[:,1], markersize=2, fmt="mo",
                 label="Circuit 2")

    def power_equation(R_charge, R_source, V_source):
        return V_source**2 / (R_charge + R_source)**2 * R_charge

    R_source_1, V_source_1 = scipy.optimize.curve_fit(power_equation, r_v_array[:,0], r_p_array[:,0])[0]
    R_source_2, V_source_2 = scipy.optimize.curve_fit(power_equation, c_v_array[:,0], c_p_array[:,0])[0]

    x_space = np.linspace(14, 200, 500)
    plt.plot(x_space, power_equation(x_space, R_source_1, V_source_1), "g-", linewidth=1)
    plt.plot(x_space, power_equation(x_space, R_source_2, V_source_2), "m-", linewidth=1)

    plt.title("Puissance moyenne dissipée [W] par la charge en fonction de la résistance [$\Omega$]")
    plt.xlabel("Résistance totale des composantes du circuit [$\Omega$]")
    plt.ylabel("Puissance moyenne dissipée [W]")
    # plt.xscale("log")
    plt.legend(loc="upper right")
    # plt.show()


make_power_figure()




def make_filix_figure():
    for part_no, markertype in zip([5,6,7,8,9], ["g<", "m<", "b<", "k<", "y<"]):
        data = []
        n = 1
        while True:
            try:
                data.append(read_lvm(f"lab_5/data_new/varying_capacity/part_{part_no}_{n}.lvm"))
                n += 1
            except: break

        global_array = np.stack((data), axis=0)
        dissipated_power = global_array[:,:,1]**2 / global_array[:,:,0]
        plotted_array = np.stack((np.mean(global_array[:,:,0], axis=1), np.mean(dissipated_power, axis=1)), axis=1)
        plt.plot(plotted_array[:,0], plotted_array[:,1], markertype, label=f"Circuit {part_no}", markersize=2)
    
    plt.title("Puissance moyenne dissipée [W] par la charge en fonction de la résistance [$\Omega$]")
    plt.xlabel("Résistance totale des composantes du circuit [$\Omega$]")
    plt.ylabel("Puissance moyenne dissipée [W]")
    # plt.xscale("log")
    plt.legend(loc="upper right")
    plt.show()

make_filix_figure()
