"""
This files computes the maximum voltage through resitances given a condition of maximum power dispersed .

Date created : 26/09/2023
    by : Mathieu Marquis
Date last modified : 26/09/2023
    by : Félix Desroches & Mathieu Marquis
"""
import numpy as np


resistances = np.array([
    12, 270, 560, 100e3, 1e6
])

max_wattage = 1/40

max_voltage = np.sqrt(max_wattage*resistances)

np.set_printoptions(suppress=True)
print("Max voltage:")
print(np.stack((resistances, max_voltage), axis=1))
