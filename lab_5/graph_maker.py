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


def resistance_power_equation(R_charge, R_source):
    global V_source
    return V_source**2 / (R_charge + R_source)**2 * R_charge


def capacitor_power_equation(R_charge, R_source):
    o = 2 * np.pi * 1000        # Omega value
    global capacity
    global V_source
    return (V_source**2 / ((R_charge / (R_charge**2 * (o*capacity)**2 + 1) + R_source)**2 
                           + (o * capacity / ((o*capacity)**2 + 1 / (R_charge**2)))**2) 
                           * (R_charge / (R_charge**2 * (o*capacity)**2 + 1)))


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
    resistance_potent = []
    resistance_powers = []
    for part_no in range(2,24):
        resistance, potential, power = get_dissipated_power(f"lab_5/data_new/resistance_ordered/part_1_{part_no}.lvm")
        resistance_values.append(resistance)
        resistance_potent.append(potential)
        resistance_powers.append(power)

    # Resistance curve
    capacitor_values = []
    capacitor_potent = []
    capacitor_powers = []
    for part_no in range(1,23):
        resistance, potential, power = get_dissipated_power(f"lab_5/data_new/capacitor_ordered/part_4_{part_no}.lvm")
        capacitor_values.append(resistance)
        capacitor_potent.append(potential)
        capacitor_powers.append(power)

    r_v_array = np.array(resistance_values)
    r_p_array = np.array(resistance_powers)
    c_v_array = np.array(capacitor_values)
    c_p_array = np.array(capacitor_powers)

    if False:
        # Write to a file all the data used for plotting
        # This part is used for making the global table
        with open("lab_5/part_1_tables.txt", "a") as f:
            print(f"CIRCUIT 1\nResistance")
            np.savetxt('lab_5/part_1_tables.txt', r_v_array, fmt = '%.8f')
            input("")
            print(f"Potential")
            np.savetxt('lab_5/part_1_tables.txt', np.array(resistance_potent), fmt = '%.8f')
            input("")
            print(f"Power")
            np.savetxt('lab_5/part_1_tables.txt', r_p_array, fmt = '%.8f')
            input("")
            
            print(f"CIRCUIT 2\nResistance")
            np.savetxt('lab_5/part_1_tables.txt', c_v_array, fmt = '%.8f')
            input("")
            print(f"Potential")
            np.savetxt('lab_5/part_1_tables.txt', np.array(capacitor_potent), fmt = '%.8f')
            input("")
            print(f"Power")
            np.savetxt('lab_5/part_1_tables.txt', c_p_array, fmt = '%.8f')
            input("")

    plt.errorbar(r_v_array[:,0], r_p_array[:,0], xerr=r_v_array[:,1], yerr=r_p_array[:,1], markersize=2, fmt="go",
                 label="Circuit de la Figure 1")
    plt.errorbar(c_v_array[:,0], c_p_array[:,0], xerr=c_v_array[:,1], yerr=c_p_array[:,1], markersize=2, fmt="mo",
                 label="Circuit de la Figure 2")

    R_source_1, R_source_cov_1 = scipy.optimize.curve_fit(resistance_power_equation, r_v_array[:,0], r_p_array[:,0])
    R_source_1_u = np.sqrt(R_source_cov_1[0])
    R_source_2, R_source_cov_2 = scipy.optimize.curve_fit(capacitor_power_equation, c_v_array[:,0], c_p_array[:,0],
                                                          p0=51)
    R_source_2_u = np.sqrt(R_source_cov_2[0])
    print(f"R_source_1 : {R_source_1} ± {R_source_1_u}\nR_source_2 : {R_source_2} ± {R_source_2_u}")
    
    x_space = np.linspace(14, 200, 50000)
    print(f"Resistance - Standard R : {x_space[np.argmax(resistance_power_equation(x_space, R_source_1))]}")
    
    # plt.plot(x_space, resistance_power_equation(x_space, R_source_1), "g-", linewidth=1)
    # plt.plot(x_space, capacitor_power_equation(x_space, R_source_2), "m-", linewidth=1)
    print(f"Capacitor - Standard R : {x_space[np.argmax(capacitor_power_equation(x_space, R_source_2))]}")
    
    # Min max curves for capacitor
    global capacity
    capacity *= 0.8
    R_source_2_min = scipy.optimize.curve_fit(capacitor_power_equation, c_v_array[:,0], c_p_array[:,0],
                                                          p0=51)[0]
    # plt.plot(x_space, capacitor_power_equation(x_space, R_source_2_min), "r--", linewidth=0.5)
    print(f"Capacitor - Max R : {x_space[np.argmax(capacitor_power_equation(x_space, R_source_2_min))]}")

    capacity /= 0.8
    capacity *= 1.2
    R_source_2_max = scipy.optimize.curve_fit(capacitor_power_equation, c_v_array[:,0], c_p_array[:,0],
                                                          p0=51)[0]
    # plt.plot(x_space, capacitor_power_equation(x_space, R_source_2_max), "r--", linewidth=0.5)
    print(f"Capacitor - Min R : {x_space[np.argmax(capacitor_power_equation(x_space, R_source_2_max))]}")
    print(f"R_sources from capacitor :\n\t{R_source_2_min}\n\t{R_source_2}\n\t{R_source_2_max}")
    
    # plt.title("Puissance moyenne dissipée par la charge en fonction de sa résistance")
    plt.xlabel("Résistance de la charge mesurée en courant continu [$\Omega$]")
    plt.ylabel("Puissance moyenne dissipée par la charge [W]")
    plt.xscale("log")
    plt.xticks(list(range(20,110,10)), list(range(20,110,10)))
    plt.legend(loc="upper right")
    plt.show()


V_source = 1 / np.sqrt(2)
capacity = 4*10**(-6)
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

# make_filix_figure()
