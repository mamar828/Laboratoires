import numpy as np


resistances = np.array([
    12, 270, 560, 100e3, 1e6
])
max_wattage = 1/40
max_voltage = np.sqrt(max_wattage*resistances)
np.set_printoptions(suppress=True)
print("Max voltage:")
print(np.stack((resistances, max_voltage), axis=1))

max_potentiometer_wattage = 0.5
max_potentiometer_resistance = 1000
print("\nMax intensity for all the potentiometer's length")
max_intensity = np.sqrt(max_potentiometer_wattage/max_potentiometer_resistance)
print(f"{max_intensity*1000:.4f} mA")

source_tension = 8.032
print("\nMinimum protective resistance")
print(f"{source_tension/max_intensity:.4f} ohms")
