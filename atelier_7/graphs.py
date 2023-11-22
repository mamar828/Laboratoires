import numpy as np
import matplotlib.pyplot as plt
import lvm_read
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
    number_of_data_arrays = len(file) - 12      # Get the number of arrays in the same .lvm file
    arrays = []
    for i in range(number_of_data_arrays):      # Iterate to group all the arrays
        arrays.append(file[i]["data"])
    
    print(file["Description"])

    if len(arrays) == 1:                        # Crop if the list contains a single element
        return arrays[0]
    else:
        return arrays

def get_frequencies(array):
    return 2**array[:,0]

def get_gain(array):
    v_out, v_g = array[:,2], array[:,1]
    return 20*np.log10(v_out/v_g)

def get_heaviside_linspaces(f_cut, lower_bound, upper_bound):
    return np.array([
        [np.logspace(0, np.log10(f_cut), 100, base=10),       np.logspace(0, np.log10(f_cut), 100, base=10)*0+lower_bound],
        [np.logspace(np.log10(f_cut), np.log10(2**(24)), 100, base=10), np.logspace(np.log10(f_cut), np.log10(2**(24)), 100, base=10)*0+upper_bound]
    ])

def circuit_1():
    array = read_lvm("atelier_7/1_C.lvm")[:13,:]
    print(array)
    plt.plot(2**array[:,0], array[:,3], "yo")
    plt.xlabel("Fréquence [Hz]")
    plt.ylabel("Déphasage [°]")
    # plt.title("Déphasage en fonction de la fréquence aux bornes du condensateur dans le circuit de la Figure 1")
    plt.show()

    array = read_lvm("atelier_7/1_R.lvm")[:,:]
    print(array)
    plt.plot(2**array[:,0], array[:,3], "yo")
    plt.xlabel("Fréquence [Hz]")
    plt.ylabel("Déphasage [°]")
    # plt.title("Déphasage en fonction de la fréquence aux bornes de la résistance dans le circuit de la Figure 1")
    plt.show()

circuit_1()

def circuit_4a():
    array = read_lvm("atelier_7/4a)test_6.lvm")
    print(array)
    plt.plot(get_frequencies(array), get_gain(array), "yo")
    heaviside = get_heaviside_linspaces(1/(2*np.pi*270*10**(-6)), lower_bound=0, upper_bound=-32.63)
    plt.plot(heaviside[0,0], heaviside[0,1], "g-", markersize=2)
    plt.plot(heaviside[1,0], heaviside[1,1], "g-", markersize=2)
    plt.xlabel("Fréquence [Hz]")
    plt.ylabel("Gain [dB]")
    # plt.title("Gain en fonction de la fréquence dans le circuit de la Figure 4a")
    plt.text(800, 0, r"$f_c=589.46$ Hz")
    plt.xscale("log")
    plt.show()

circuit_4a()

def circuit_4c():
    array = read_lvm("atelier_7/4c)_in_out_1.lvm")
    print(array)
    plt.plot(get_frequencies(array), get_gain(array), "yo")
    heaviside = get_heaviside_linspaces(260000, lower_bound=0, upper_bound=-2.469)
    plt.plot(heaviside[0,0], heaviside[0,1], "g-", markersize=2)
    plt.plot(heaviside[1,0], heaviside[1,1], "g-", markersize=2)
    plt.xlabel("Fréquence [Hz]")
    plt.ylabel("Gain [dB]")
    # plt.title("Gain en fonction de la fréquence dans le circuit de la Figure 4c")
    plt.text(270000, 0, r"$f_c≈260000$ Hz")
    plt.xscale("log")
    plt.show()

circuit_4c()
