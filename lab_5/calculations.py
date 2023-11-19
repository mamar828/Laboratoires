import numpy as np
from scipy.constants.constants import c


# Propagation speed
delays = np.array([80, 159]) * 10**(-9)
lengths = np.array([20,40])
u = lengths / delays
u_u = ((lengths + [0.1,0.2])/((delays - 2*10**(-9))) - (lengths - [0.1,0.2])/((delays + 2*10**(-9)))) / 2
print(f"u: {u} m/s, uncertainties: {u_u} m/s")

# Optical density
n = c / u
n_u = (c/(u-u_u)-c/(u+u_u)) / 2
print(f"n: {n}, uncertainties: {n_u}")

# Reflection coefficient
A_i = np.array([673.8, 640])
A_r = np.array([636.3, -630])
A_u = np.array([10, 10])
G = A_r / A_i
G_u = (np.abs(A_u/A_r) + np.abs(A_u/A_i)) * np.abs(A_r/A_i)
print(f"Gamma: {G}, uncertainties {G_u}")
