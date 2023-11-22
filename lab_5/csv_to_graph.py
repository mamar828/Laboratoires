import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ref = [
    844.2210964859*10**(-3),
    844.2210964859*10**(-3),
    844.2210964859*10**(-3),
    844.2210964859*10**(-3),
    844.2210964859*10**(-3),
    844.2210964859*10**(-3),
    844.2210964859*10**(-3),
    844.2210964859*10**(-3),
    844.2210964859*10**(-3),
    844.2210964859*10**(-3),
    864.3215987831*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    884.4221010804*10**(-3),
    881.9095382933*10**(-3),
    # -40.2010045946*10**(-3),
    # -40.2010045946*10**(-3),
    # -40.2010045946*10**(-3),
    # -40.2010045946*10**(-3),
]
# ref_640 = []
# for i in range(20):
#     ref_640 += ref
if False:
    for i in range(1,13):
        k = 1
        # if i != k :
        #     continue
        # print(ref_640)
        filename = f"shlubabuba{i}.csv"
        df = pd.read_csv(filename, sep=',', header=None)
        df = df.iloc[2:, :]
        arr = df.to_numpy()
        arr = arr.astype(float)
        fig, axes = plt.subplots(2, 2)
        axes[0, 0].plot(arr[:, 0], arr[:, 1], "r+")
        axes[0, 1].plot(arr[:, 0], arr[:, 1]/max(np.abs(arr[:, 1])), "r+")
        if len(arr[0]) == 3:
            axes[1, 0].plot(arr[:, 0], arr[:, 2], "b+")
            axes[1, 1].plot(arr[:, 0], arr[:, 2]/max(np.abs(arr[:, 2])), "b+")
        print(i)
        # axes.axis('off')
        # axes[0].set_yticklabels([-1, 0, 1])
        # axes[0].set_xticklabels([])
        # axes[1].set_yticklabels([-1, 0, 1])
        # axes[1].set_xticklabels([])
        # axes[0].set_yticks([-1, 0, 1])
        # axes[0].set_xticks([])
        # axes[1].set_yticks([-1, 0, 1])
        # axes[1].set_xticks([])
        plt.show()


def get_csv_data(filename: str) -> np.ndarray:
    df = pd.read_csv(filename, sep=',', header=None)
    df = df.iloc[2:, :]
    arr = df.to_numpy()
    return arr.astype(float)


def make_graphs():
    arrays = [get_csv_data(f"lab_5/data_new/small_pulse/lol_{i}.csv") for i in range(102,107)]
    fig, axes = plt.subplots(2, 2, sharey="row", sharex="col")
    fig.set_size_inches(12,6)

    axes[0,0].plot(arrays[0][:,0], arrays[0][:,1], "r-", label="Signal détecté à\nl'entrée en circuit ouvert")
    axes[0,0].legend(loc="lower right", handlelength=0)
    axes[0,0].title.set_text("A")
    axes[0,1].plot(arrays[1][:,0], arrays[1][:,1], "r-", label="Signal détecté à\nl'entrée avec court-circuit")
    axes[0,1].legend(loc="lower left", handlelength=0)
    axes[0,1].title.set_text("B")
    axes[1,0].plot(arrays[2][:,0], arrays[2][:,2], "b-", label="Signal détecté à la\nsortie en circuit ouvert")
    axes[1,0].legend(loc="upper right", handlelength=0)
    axes[1,0].title.set_text("C")
    axes[1,1].plot(arrays[3][:,0], arrays[3][:,2], "b-", label="Signal détecté à la\nsortie avec court-circuit")
    axes[1,1].legend(loc="upper left", handlelength=0)
    axes[1,1].title.set_text("D")

    fig.text(0.5, 0.01, "Temps [s]", ha="center", size=12)
    fig.text(0.05, 0.5, "Amplitude [V]", va="center", rotation="vertical", size=12)
    # manager = plt.get_current_fig_manager()
    # manager.full_screen_toggle()
    plt.show()
    
    arrays = [get_csv_data(f"lab_5/data_new/large_pulse/scope_{i}.csv") for i in [3,4]]
    fig, axes = plt.subplots(2, 2, sharey="all", sharex="col")
    fig.set_size_inches(12,6)

    axes[0,0].plot(arrays[0][:,0], arrays[0][:,1], "r-", label="Signal détecté à\nl'entrée en circuit ouvert")
    axes[0,0].legend(loc="lower right", handlelength=0)
    axes[0,0].title.set_text("A")
    axes[0,1].plot(arrays[1][:,0], arrays[1][:,1], "r-", label="Signal détecté à\nl'entrée avec court-circuit")
    axes[0,1].legend(loc="lower left", handlelength=0)
    axes[0,1].title.set_text("B")
    axes[1,0].plot(arrays[0][:,0], arrays[0][:,2], "b-", label="Signal détecté à la\nsortie en circuit ouvert")
    axes[1,0].legend(loc="upper right", handlelength=0)
    axes[1,0].title.set_text("C")
    axes[1,1].plot(arrays[1][:,0], arrays[1][:,2], "b-", label="Signal détecté à la\nsortie avec court-circuit")
    axes[1,1].legend(loc="upper left", handlelength=0)
    axes[1,1].title.set_text("D")

    fig.text(0.5, 0.01, "Temps [s]", ha="center", size=12)
    fig.text(0.05, 0.5, "Amplitude [V]", va="center", rotation="vertical", size=12)
    # manager = plt.get_current_fig_manager()
    # manager.full_screen_toggle()
    plt.show()


make_graphs()


def test_graphs():
    for i in range(5):
        array = get_csv_data(f"lab_5/data_new/large_pulse/scope_{i}.csv")
        plt.plot(array[:,0], array[:,1], "y-")
        try:
            plt.plot(array[:,0], array[:,2], "m-")
            try:
                plt.plot(array[:,0], array[:,3], "k-")
            except: pass
        except: pass
        plt.show()


# test_graphs()
