import numpy as np
import matplotlib.pyplot as plt


def gain_equation_1(omega):
    return (
        (((-omega**2+10**9)*(-omega**2*(1+270*10**(-3))+10**9+270*10**6))/((-omega**2*(1+270*10**(-3))+10**9+270*10**6)**2
                                                                         +(270*10**3*omega)**2))**2
            +((270*10**3*omega)/((-omega**2*(1+270*10**(-3))+10**9+270*10**6)**2+(270*10**3*omega)**2))**2)**(1/2)

def phase_equation_1(omega):
    return np.arctan(
        (((-omega**2+10**9)*(-omega**2*(1+270*10**(-3))+10**9+270*10**6))/((-omega**2*(1+270*10**(-3))+10**9+270*10**6)**2
                                                                         +(270*10**3*omega)**2))**2
            +((270*10**3*omega)/((-omega**2*(1+270*10**(-3))+10**9+270*10**6)**2+(270*10**3*omega)**2))**2)
    return np.arctan(
        ((270*10**3*omega)/((-omega**2*(1+270*10**(-3))+10**9+270*10**6)**2+(270*10**3*omega)**2)) / 
        (((-omega**2+10**9)*(-omega**2*(1+270*10**(-3))+10**9+270*10**6))/((-omega**2*(1+270*10**(-3))+10**9+270*10**6)**2
                                                                         +(270*10**3*omega)**2))
    )

omega_space = np.logspace(1, 7, 20000, base=10)
plt.plot(omega_space, gain_equation_1(omega_space), "mo", markersize=2)
plt.xscale("log")
plt.show()

plt.plot(omega_space, phase_equation_1(omega_space), "mo", markersize=2)
plt.xscale("log")
plt.show()
