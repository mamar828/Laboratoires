"""
This files allows the creation of a histogram from a .lvm file.

Date created : 19/09/2023
    by : Félix Desroches
Date last modified : 19/09/2023
    by : Félix Desroches & Mathieu Marquis
"""
import os
from typing import Optional

import lvm_read
import matplotlib.pyplot as plt
import numpy as np


def terminate_figure(
        fig: Optional[plt.Figure] = None,
        show: bool = True,
        path_to_save: Optional[str] = None,
        **kwargs
) -> None:
    """
    Terminates current figure.

    Parameters
    ----------

    fig : plt.Figure
        Current figure. If no figure is given, will close the opened figure.
    show : bool
        Whether to show figure. Defaults to True
    path_to_save : Optional[str]
        Path to save the figure.
    """
    if fig is not None:
        fig.tight_layout()

    if path_to_save is not None:
        plt.savefig(path_to_save, dpi=kwargs.get('dpi', 300), bbox_inches='tight')
    if show:
        plt.show()

    if fig is not None:
        plt.close(fig)
    else:
        plt.close()


def create_histogram_from_lvm(
        file_path: str,
        histogram: bool = True,
        point_cloud: bool = False,
        show: bool = True,
        path_to_save_folder: Optional[str] = None,
        **kwargs
) -> None:
    """
    Creates and shows a histogram based on the data points from a .lvm file.

    Parameters
    ----------
    file_path : str
        The path to the .lvm file to use.
    histogram : bool
        Whether to compute a histogram of the voltage as a function of time. Defaults to True.
    point_cloud : bool
        Whether to compute a point cloud of the voltage as a function of time. Defaults to False.
    show : bool
        Whether to show the graphs. Defaults to True.
    path_to_save_folder : Optional[str]
        The path to the folder within which the graph should be saved. Does not save the graph by default.
    """
    lvm_file = lvm_read.read(file_path)
    if len(lvm_file[0]["data"][0]) == 2:
        y_data = np.transpose(lvm_file[0]["data"][:, 0]).squeeze()
        # tension_1 = np.transpose(lvm_file[0]["data"][:, 0]).squeeze()
        # tension_2 = np.transpose(lvm_file[0]["data"][:, 1]).squeeze()
        # intensity = tension_2 / 12
        # resistance = tension_1/intensity
        # print(resistance)
        # print(np.average(resistance), np.std(resistance), np.median(resistance))
        # fig, arr = plt.subplots(1, 1, figsize=(8, 6))
        # arr.hist(resistance, bins=25)
        plt.show()
    else:
        y_data = np.transpose(lvm_file[0]["data"]).squeeze()
    delta_x = lvm_file[0]["Delta_X"][0]
    x_data = np.linspace(0, delta_x * (len(y_data) - 1), len(y_data))

    if point_cloud and histogram:
        fig, arr = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))
        arr[0].hist(y_data, bins=25)
        # arr[1].plot(x_data, y_data, linestyle='-')
        arr[1].scatter(x_data, y_data)
    elif point_cloud:
        fig, arr = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))
        # arr.plot(x_data, y_data, linestyle='-')
        arr.scatter(x_data, y_data)
        arr.set_ylabel('Voltage [V]')
        arr.set_xlabel('Time [s]')
    elif histogram:
        fig, arr = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))
        arr.hist(y_data, bins=25)
        arr.set_xlabel('Voltage [V]')
        arr.set_ylabel('Number of values [-]')
    else:
        return

    if histogram and point_cloud :
        file_name = "histogram_point_cloud_from_lvm.pdf"
    elif histogram:
        file_name = "histogram_from_lvm.pdf"
    elif point_cloud:
        file_name = "point_cloud_from_lvm.pdf"
    else:
        file_name = ""

    if path_to_save_folder is not None:
        path = os.path.join(
            path_to_save_folder,
            f"{kwargs.get('filename', file_name)}"
        )
    else:
        path = None
    terminate_figure(fig=fig, path_to_save=path, show=show)


# create_histogram_from_lvm(
#     "data/20230919_mesures_resistances_3.lvm",
#     histogram=True,
#     point_cloud=True,
#     show=False,
#     path_to_save_folder=None,
# )
# create_histogram_from_lvm(
#     "data/20230919_mesures_0.05_nothing.lvm",
#     histogram=True,
#     point_cloud=False,
#     show=False,
#     path_to_save_folder="save_fig",
#     filename='histogram_nothing.pdf'
# )
create_histogram_from_lvm(
    "data/20230919_mesures_smol_patate_inox_alu.lvm",
    histogram=False,
    point_cloud=True,
    show=False,
    path_to_save_folder="save_fig",
    filename='point_cloud_inox_alu.pdf'
)
# create_histogram_from_lvm(
#     "data/20230919_mesures_smol_patate_zinc_inox.lvm",
#     histogram=True,
#     point_cloud=True,
#     show=False,
#     path_to_save_folder="save_fig",
#     filename='25_bins_smol_zinc_inox.pdf'
# )
# create_histogram_from_lvm(
#     "data/20230919_mesures_smol_patate_zinc_alu.lvm",
#     histogram=True,
#     point_cloud=True,
#     show=False,
#     path_to_save_folder="save_fig",
#     filename='25_bins_smol_zinc_alu.pdf'
# )
# create_histogram_from_lvm(
#     "data/20230919_mesures_smol_patate_acier_alu.lvm",
#     histogram=True,
#     point_cloud=True,
#     show=False,
#     path_to_save_folder="save_fig",
#     filename='25_bins_smol_acier_alu.pdf'
# )
# create_histogram_from_lvm(
#     "data/20230919_mesures_patate_inox_alu.lvm",
#     histogram=True,
#     point_cloud=True,
#     show=False,
#     path_to_save_folder="save_fig",
#     filename='25_bins_not_smol_inox_alu.pdf'
# )
# create_histogram_from_lvm(
#     "data/20230919_mesures_patate_inox_alu_1.lvm",
#     histogram=True,
#     point_cloud=True,
#     show=False,
#     path_to_save_folder="save_fig",
#     filename='25_bins_not_smol_inox_alu_1.pdf'
# )
# create_histogram_from_lvm(
#     "data/20230919_mesures_patate_inox_alu_2.lvm",
#     histogram=True,
#     point_cloud=True,
#     show=False,
#     path_to_save_folder="save_fig",
#     filename='25_bins_not_smol_inox_alu_2.pdf'
# )
# create_histogram_from_lvm(
#     "data/20230919_mesures_resistances.lvm",
#     histogram=True,
#     point_cloud=True,
#     show=False,
#     path_to_save_folder="save_fig",
#     filename='25_bins_res_0_col_2.pdf'
# )
# create_histogram_from_lvm(
#     "data/20230919_mesures_resistances_1.lvm",
#     histogram=True,
#     point_cloud=True,
#     show=False,
#     path_to_save_folder="save_fig",
#     filename='25_bins_res_1_col_2.pdf'
# )
# create_histogram_from_lvm(
#     "data/20230919_mesures_resistances_2.lvm",
#     histogram=True,
#     point_cloud=True,
#     show=False,
#     path_to_save_folder="save_fig",
#     filename='25_bins_res_2_col_2.pdf'
# )
# create_histogram_from_lvm(
#     "data/20230919_mesures_resistances_3.lvm",
#     histogram=True,
#     point_cloud=True,
#     show=False,
#     path_to_save_folder="save_fig",
#     filename='25_bins_res_3_col_2.pdf'
# )
