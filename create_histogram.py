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
    y_data = np.transpose(lvm_file[0]["data"]).squeeze()
    delta_x = lvm_file[0]["Delta_X"][0]
    x_data = np.linspace(0, delta_x * (len(y_data) - 1), len(y_data))
    if point_cloud and histogram:
        fig, arr = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))
        arr[0].hist(y_data)
        # arr[1].plot(x_data, y_data, linestyle='-')
        arr[1].scatter(x_data, y_data)
    elif point_cloud:
        fig, arr = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))
        arr.plot(x_data, y_data, linestyle='-')
        arr.scatter(x_data, y_data)
    elif histogram:
        fig, arr = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))
        arr.hist(y_data)
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


create_histogram_from_lvm(
    "/Users/felixdesroches/Downloads/20230919_mesures_patate_inox_alu_2.lvm",
    histogram=True,
    point_cloud=True,
    show=True,
    path_to_save_folder="/Users/felixdesroches/Desktop/ULaval_labs/PHY_2002_electronique/Laboratoires/save_fig",
)
