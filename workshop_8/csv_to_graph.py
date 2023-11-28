import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy


def get_csv_data(filename: str) -> np.ndarray:
    df = pd.read_csv(filename, sep=',', header=None)
    df = df.iloc[2:, :]
    arr = df.to_numpy()
    return arr.astype(float)


def make_graphs():
    arrays = [get_csv_data(f"workshop_8/data/circuit_1_{i}.csv") for i in [1,2]+list(range(4,21))]
    def build_plot():
        plt.xlabel("Temps [s]")
        plt.ylabel("Tension [V]")
        plt.legend(loc="upper right")
        plt.show()

    if False:
        plt.plot(arrays[3][:,0], arrays[3][:,1], "r-", label="Capacité de 470 nF", linewidth=1)
        build_plot()
        plt.plot(arrays[3][:,0], arrays[3][:,1], "#8d8c8c4d", label="Capacité de 470 nF", linewidth=1)
        plt.plot(arrays[0][:,0], arrays[0][:,1], "r-", label="Capacité de 1 $\mu$F", linewidth=1)
        build_plot()
        plt.plot(arrays[3][:,0], arrays[3][:,1], "#8d8c8c4d", label="Capacité de 470 nF", linewidth=1)
        plt.plot(arrays[0][:,0], arrays[0][:,1], "#48484879", label="Capacité de 1 $\mu$F", linewidth=1)
        plt.plot(arrays[1][:,0], arrays[1][:,1], "r-", label="Capacité de 2 $\mu$F", linewidth=1)
        build_plot()
        plt.plot(arrays[3][:,0], arrays[3][:,1], "#8d8c8c4d", label="Capacité de 470 nF", linewidth=1)
        plt.plot(arrays[0][:,0], arrays[0][:,1], "#48484879", label="Capacité de 1 $\mu$F", linewidth=1)
        plt.plot(arrays[1][:,0], arrays[1][:,1], "#0c0c0cd8", label="Capacité de 2 $\mu$F", linewidth=1)
        plt.plot(arrays[2][:,0], arrays[2][:,1], "r-", label="Capacité de 6 $\mu$F", linewidth=1)
        build_plot()

    if False:
        plt.plot(arrays[18][:,0], arrays[18][:,1], "r-", label="$R=12 \Omega$", linewidth=1)
        build_plot()
        
        plt.plot(arrays[18][:,0], arrays[18][:,1], "#D4D3D3", label="$R=12 \Omega$", linewidth=1)
        plt.plot(arrays[17][:,0], arrays[17][:,1], "r-", label="$R=33 \Omega$", linewidth=1)
        build_plot()
        
        plt.plot(arrays[18][:,0], arrays[18][:,1], "#D4D3D3", label="$R=12 \Omega$", linewidth=1)
        plt.plot(arrays[17][:,0], arrays[17][:,1], "#B8B7B7", label="$R=33 \Omega$", linewidth=1)
        plt.plot(arrays[16][:,0], arrays[16][:,1], "r-", label="$R=270 \Omega$", linewidth=1)
        build_plot()
        
        plt.plot(arrays[18][:,0], arrays[18][:,1], "#D4D3D3", label="$R=12 \Omega$", linewidth=1)
        plt.plot(arrays[17][:,0], arrays[17][:,1], "#B8B7B7", label="$R=33 \Omega$", linewidth=1)
        plt.plot(arrays[16][:,0], arrays[16][:,1], "#9B9A9A", label="$R=270 \Omega$", linewidth=1)
        plt.plot(arrays[15][:,0], arrays[15][:,1], "r-", label="$R=560 \Omega$", linewidth=1)
        build_plot()
        
        plt.plot(arrays[18][:,0], arrays[18][:,1], "#D4D3D3", label="$R=12 \Omega$", linewidth=1)
        plt.plot(arrays[17][:,0], arrays[17][:,1], "#B8B7B7", label="$R=33 \Omega$", linewidth=1)
        plt.plot(arrays[16][:,0], arrays[16][:,1], "#9B9A9A", label="$R=270 \Omega$", linewidth=1)
        plt.plot(arrays[15][:,0], arrays[15][:,1], "#757574", label="$R=560 \Omega$", linewidth=1)
        plt.plot(arrays[14][:,0], arrays[14][:,1], "r-", label="$R=1 k\Omega$", linewidth=1)
        build_plot()
        
        plt.plot(arrays[18][:,0], arrays[18][:,1], "#D4D3D3", label="$R=12 \Omega$", linewidth=1)
        plt.plot(arrays[17][:,0], arrays[17][:,1], "#B8B7B7", label="$R=33 \Omega$", linewidth=1)
        plt.plot(arrays[16][:,0], arrays[16][:,1], "#9B9A9A", label="$R=270 \Omega$", linewidth=1)
        plt.plot(arrays[15][:,0], arrays[15][:,1], "#757574", label="$R=560 \Omega$", linewidth=1)
        plt.plot(arrays[14][:,0], arrays[14][:,1], "#4C4C4C", label="$R=1 k\Omega$", linewidth=1)
        plt.plot(arrays[13][:,0], arrays[13][:,1], "r-", label="$R=1.2 k\Omega$", linewidth=1)
        build_plot()
        
    if False:
        print(f"{np.mean(np.diff(scipy.signal.find_peaks(arrays[18][:,1])[0]))} 12 ohms")
        print(f"{np.mean(np.diff(scipy.signal.find_peaks(arrays[17][:,1])[0]))} 33 ohms")
        # plt.plot(arrays[18][:,0], arrays[18][:,1], "#D4D3D3", label="$R=12 \Omega$", linewidth=1)
        plt.plot(arrays[18][750:1250,0], arrays[18][750:1250,1]/np.max(arrays[18][:,1]), "r--", label="$R=12 \Omega$", 
                 linewidth=1)
        plt.plot(arrays[17][750:1250,0], arrays[17][750:1250,1]/np.max(arrays[17][:,1]), "b-", label="$R=33 \Omega$", 
                 linewidth=1)
        build_plot()
        
    if False:
        # print(f"{(np.diff(scipy.signal.find_peaks(arrays[0][:,1])[0]))} 1 $\mu$F")
        # print(f"{(np.diff(scipy.signal.find_peaks(arrays[1][:,1])[0]))} 2 $\mu$F")
        # plt.plot(arrays[0][:,0], arrays[0][:,1], "#D4D3D3", label="$R=12 \Omega$", linewidth=1)
        d_1 = 0.00102 - 0.00031
        d_2 = 0.002 - 0.00063
        d_3 = 0.00191750 + 0.00226724
        print(f"Ratio C=2/C=1: {d_2/d_1}")
        print(f"Ratio C=3/C=3: {d_3/d_2}")
        plt.plot(arrays[0][:,0], arrays[0][:,1]/np.max(arrays[0][:,1]), "r--", label="$C=1 \mu$F", 
                 linewidth=1)
        plt.plot(arrays[1][:,0], arrays[1][:,1]/np.max(arrays[1][:,1]), "b-.", label="$C=2 \mu$F", 
                 linewidth=1)
        plt.plot(arrays[2][:,0], arrays[2][:,1]/np.max(arrays[2][:,1]), "g-", label="$C=6 \mu$F", 
                 linewidth=1)
        build_plot()
        
    # for subarray in arrays[-1:-7:-1]:
    #     plt.plot(subarray[:,0], subarray[:,1], "r-", linewidth=1)
    #     plt.show()
    # plt.legend(loc="upper right")
    # plt.show()

    # for i, subarray in enumerate(arrays):
    #     plt.title(i+2)
    #     plt.plot(subarray[:,0], subarray[:,1], "r-")
    #     plt.show()
    # print(arrays)


make_graphs()
