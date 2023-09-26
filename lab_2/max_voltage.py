import numpy as np


resistances = np.array([
    12, 270, 560, 100e3, 1e6
])

max_wattage = 1/40

max_voltage = np.sqrt(max_wattage*resistances)

np.set_printoptions(suppress=True)
print("Max voltage:")
print(np.stack((resistances, max_voltage), axis=1))
