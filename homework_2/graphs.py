import numpy as np
import matplotlib.pyplot as plt
import scipy


max_G = np.abs(((1j*10)**2+10**9)/((1j*10)**2*(1+270*10**(-3))+270*10**3*(1j*10)+10**9+270*10**6))
mid_G = max_G / np.sqrt(2)


def gain_equation_1(omega, optimizing=True):
    """
    Optimizing parameter : allows the use of scipy.optimize.fmin to find intersections points.
    """
    s = 1j*omega
    if optimizing:
        return np.abs(np.abs(
            (s**2+10**9)/(s**2*(1+270*10**(-3))+270*10**3*s+10**9+270*10**6)
        ) - mid_G)
    else:
        return np.abs(
            (s**2+10**9)/(s**2*(1+270*10**(-3))+270*10**3*s+10**9+270*10**6)
        )


def phase_equation_1(omega):
    s = 1j*omega
    return np.angle(
        (s**2+10**9)/(s**2*(1+270*10**(-3))+270*10**3*s+10**9+270*10**6)
    )


def circuit_1():
    omega_space = np.logspace(1, 7, 20000, base=10)

    intersections = scipy.optimize.fmin(gain_equation_1, 10**4)[0], scipy.optimize.fmin(gain_equation_1, 10**6)[0]
    print(f"Cutoff frequencies : {intersections}")

    plt.plot(omega_space, gain_equation_1(omega_space, False), "mo", markersize=2)
    plt.plot(intersections, [mid_G, mid_G], "go")
    plt.text(intersections[0]/(10**1.7), mid_G, 
             (r"$\omega_{c1}$" + f"={intersections[0]:.2e} " + r"$s^{-1}$"), fontsize=9)
    plt.text(intersections[1]*(10**0.2), mid_G, 
             (r"$\omega_{c2}$" + f"={intersections[1]:.2e} " + r"$s^{-1}$"), fontsize=9)

    plt.xlabel(r"Fréquence angulaire $\omega$ [$s^{-1}$]")
    plt.ylabel(r"Gain $G$ [-]")
    plt.xscale("log")
    plt.show()

    plt.plot(omega_space, phase_equation_1(omega_space), "mo", markersize=2)
    plt.xlabel(r"Fréquence angulaire $\omega$ [$s^{-1}$]")
    plt.ylabel(r"Phase $\varphi(\omega)$ [-]")
    plt.xscale("log")
    plt.show()

circuit_1()
