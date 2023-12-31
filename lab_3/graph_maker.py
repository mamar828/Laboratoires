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


def make_figures_for_parts_abce():
    plot_files = [
        ["lab_3/data/part_3_a.lvm", "lab_3/graphs/part_3_a.png", {
            "title": "Courant en fonction de la différence de potentiel aux bornes \nd'une résistance de 1.2 kΩ",
            "xlabel": "Différence de potentiel $∆V$ [V]",
            "ylabel": "Courant $I$ [A]"
        }],
        ["lab_3/data/part_3_b.lvm", "lab_3/graphs/part_3_b.png", {
            "title": "Courant en fonction de la différence de potentiel aux bornes \nd'un condensateur de 1 μF",
            "xlabel": "Différence de potentiel $∆V$ [V]",
            "ylabel": "Courant $I$ [A]"
        }],
        ["lab_3/data/part_3_c.lvm", "lab_3/graphs/part_3_c.png", {
            "title": "Courant en fonction de la différence de potentiel aux bornes \nd'une bobine de 1 mH",
            "xlabel": "Différence de potentiel $∆V$ [V]",
            "ylabel": "Courant $I$ [A]"
        }],
        ["lab_3/data/part_3_e.lvm", "lab_3/graphs/part_3_e.png", {
            "title": ("Courant en fonction de la différence de potentiel aux bornes \n" + 
                      "d'une diode Zener branchée en sens inverse"),
            "xlabel": "Différence de potentiel $∆V$ [V]",
            "ylabel": "Courant $I$ [A]"
        }]
    ]
    for data, save_path, params in plot_files:
        plot_graph(read_lvm(data), params=params)
        save_figure(save_path, show=True)

# make_figures_for_parts_abce()

def make_figure_for_part_d():
    zero_to_six = read_lvm("lab_3/data/part_3_d_0to6.lvm")
    zero_to_one = read_lvm("lab_3/data/part_3_d_0to1.lvm")
    global_array = np.concatenate(((zero_to_six * (-1))[::-1], zero_to_one[1:,:]))
    np.save("lab_3/data/concatenated_part_4.npy", global_array)
    params = {
        "title": "Courant en fonction de la différence de\npotentiel aux bornes d'une diode standard",
        "xlabel": "Différence de potentiel $∆V$ [V]", 
        "ylabel": "Courant $I$ [A]"
    }
    plot_graph(global_array, params)
    save_figure("lab_3/graphs/part_3_d.png", show=True)

# make_figure_for_part_d()

def make_figures_for_part_4():
    arrays = read_lvm("lab_3/data/part_4_ok_17.lvm")
    params = {
        "title": r"Courant $i_{ce}$ en fonction de la tension $v_{ce}$ pour différentes tensions $v_{be}$",
        "xlabel": r"Différence de potentiel $v_{ce}$ [V]", 
        "ylabel": r"Courant $i_{ce}$ [A]"
    }
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.errorbar(arrays[0][:,0], arrays[0][:,1], fmt="go",
                markersize=2, label=r"Tension $v_{be}=0.0$ V",
                xerr=0.0015/100*arrays[0][:,0]+0.0004/100*10, yerr=0.005/100*arrays[0][:,1]+0.010/100*0.01)
    ax.errorbar(arrays[1][:,0], arrays[1][:,1], fmt="ro",
                markersize=2, label=r"Tension $v_{be}=0.2$ V",
                xerr=0.0015/100*arrays[0][:,0]+0.0004/100*10, yerr=0.005/100*arrays[1][:,1]+0.010/100*0.01)
    ax.errorbar(arrays[2][:,0], arrays[2][:,1], fmt="bo",
                markersize=2, label=r"Tension $v_{be}=0.4$ V",
                xerr=0.0015/100*arrays[0][:,0]+0.0004/100*10, yerr=0.005/100*arrays[2][:,1]+0.010/100*0.01)
    ax.errorbar(arrays[3][:,0], arrays[3][:,1], fmt="yo",
                markersize=2, label=r"Tension $v_{be}=0.6$ V",
                xerr=0.0015/100*arrays[0][:,0]+0.0004/100*10, yerr=0.005/100*arrays[3][:,1]+0.010/100*0.01)
    ax.errorbar(arrays[4][:,0], arrays[4][:,1], fmt="mo",
                markersize=2, label=r"Tension $v_{be}=0.8$ V",
                xerr=0.0015/100*arrays[0][:,0]+0.0004/100*10, yerr=0.01/100*arrays[4][:,1]+0.004/100*0.1)
    ax.errorbar(arrays[5][:,0], arrays[5][:,1], fmt="ko",
                markersize=2, label=r"Tension $v_{be}=1.0$ V",
                xerr=0.0015/100*arrays[0][:,0]+0.0004/100*10, yerr=0.05/100*arrays[5][:,1]+0.006/100*1)
    ax.errorbar(arrays[6][:,0], arrays[6][:,1], fmt="co",
                markersize=2, label=r"Tension $v_{be}=1.2$ V",
                xerr=0.0015/100*arrays[0][:,0]+0.0004/100*10, yerr=0.05/100*arrays[6][:,1]+0.006/100*1)
    ax.set_title(params["title"])
    ax.set_xlabel(params["xlabel"])
    ax.set_ylabel(params["ylabel"])
    fig.legend(loc=(0.15,0.63), fontsize=7)

    # Get the values of i_{sat}
    i_sat_600mV  = np.mean(arrays[3][1:,1]), np.std(arrays[3][1:,1])
    i_sat_800mV  = np.mean(arrays[4][4:,1]), np.std(arrays[4][4:,1])
    i_sat_1000mV = np.mean(arrays[5][6:,1]), np.std(arrays[5][6:,1])
    i_sat_1200mV = np.mean(arrays[6][8:,1]), np.std(arrays[6][8:,1])*3
    ax.text(2, 0.003, c="y", 
            s=(r"$i_{sat}=$"+f"({round(i_sat_600mV[0]*10**6, 1)} ± {round(i_sat_600mV[1]*10**6, 1)}) μA"))
    ax.text(2, 0.044, c="m", 
            s=(r"$i_{sat}=$"+f"({int(round(i_sat_800mV[0]*10**3, 0))} ± {int(round(i_sat_800mV[1]*10**3, 0))}) mA"))
    ax.text(2, 0.12, c="k", 
            s=(r"$i_{sat}=$"+f"({int(round(i_sat_1000mV[0]*10**3, 0))} ± {int(round(i_sat_1000mV[1]*10**3, 0))}) mA"))
    ax.text(2, 0.195, c="c", 
            s=(r"$i_{sat}=$"+f"({round(i_sat_1200mV[0], 2)} ± {round(i_sat_1200mV[1], 2)}) A"))
    print(f"  0mV std: {np.std(arrays[0][:,1])}")
    print(f"200mV std: {np.std(arrays[1][:,1])}")
    print(f"400mV std: {np.std(arrays[2][1:,1])}")
    save_figure("lab_3/graphs/part_4.png", show=True)

# make_figures_for_part_4()

def make_figure_for_dvdi(calc_uncertainty: bool=False):
    array = np.load("lab_3/data/concatenated_part_4.npy")
    diff_array = np.diff(array, n=1, axis=0)
    plotted_array = np.stack((array[:-1,0], diff_array[:,0]/diff_array[:,1]), axis=1)
    params = {
        "title": ("Résistance dynamique $R_D$ en fonction de la différence\n" + 
                  "de potentiel aux bornes d'une diode standard"),
        "xlabel": "Différence de potentiel $∆V$ [V]", 
        "ylabel": "Résistance dynamique $R_D$ [Ω]"
    }

    if calc_uncertainty:
        v_uncertainty = 0.0015/100*np.abs(plotted_array[:,0]) + 0.0004/100*10
        i_uncertainty = np.concatenate((
            0.005/100*np.abs(plotted_array[:-5,1]) + 0.010/100*0.01, 0.01/100*np.abs(plotted_array[-5:,1]) + 0.004/100*0.1
        ))
        r_uncertainty = (
            ((v_uncertainty[1:] + v_uncertainty[:-1]) / np.abs(diff_array[:-1,0]) + 
            (i_uncertainty[1:] + i_uncertainty[:-1]) / np.abs(diff_array[:-1,1])) * np.abs(plotted_array[:-1,1])
        )

        plt.errorbar(plotted_array[:-1,0], plotted_array[:-1,1], xerr=v_uncertainty[:-1], yerr=r_uncertainty,
                    markersize=2, fmt="go")
        plt.title(params["title"])
        plt.xlabel(params["xlabel"])
        plt.ylabel(params["ylabel"])
    else:
        plot_graph(plotted_array, params)

    save_figure("lab_3/graphs/dynamic_resistance.png", show=True)

# make_figure_for_dvdi()

def make_figure_for_fitted_diode():
    array = np.load("lab_3/data/concatenated_part_4.npy")
    params = {
        "title": ("Courant en fonction de la différence de potentiel aux bornes \nd'une diode standard avec un " + 
                  "ajustement de l'équation de Shockley"),
        "xlabel": "Différence de potentiel $∆V$ [V]", 
        "ylabel": "Courant $I$ [A]"
    }

    def shockley_equation(v, i_0, v_0):
        return i_0 * (np.e**(v/v_0) - 1)

    i_0, v_0 = scipy.optimize.curve_fit(shockley_equation, array[:,0], array[:,1])[0]
    plot_graph(array, params)
    print(f"i_0: {i_0}")
    print(f"v_0: {v_0}")

    x_space = np.linspace(-6,1, 350)
    plt.plot(x_space, shockley_equation(x_space, i_0, v_0), "b-", markersize=2)
    save_figure("lab_3/graphs/shockley.png", show=True)

    residue = shockley_equation(array[:,0], i_0, v_0) - array[:,1]
    params["title"] = ("Résidu de l'équation de Shockley appliquée aux mesures de courant en\nfonction de la " + 
                       "différence de potentiel aux bornes d'une diode standard")
    plot_graph(np.stack((array[:,0], residue), axis=1), params)
    print(f"residue stddev: {np.std(residue)}")
    print(f"residue mean  : {np.mean(residue)}")
    save_figure("lab_3/graphs/shockley_residue.png", show=True)
    
# make_figure_for_fitted_diode()

