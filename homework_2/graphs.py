import numpy as np
import matplotlib.pyplot as plt


def gain_equation_1(omega):
    s = 1j*omega
    return np.abs(
        (s**2+10**9)/(s**2*(1+270*10**(-3))+270*10**3*s+10**9+270*10**6)
    )
    # EQUATION WITHOUT j
    # return (
    #     (((-omega**2+10**9)*(-omega**2*(1+270*10**(-3))+10**9+270*10**6))/((-omega**2*(1+270*10**(-3))+10**9+270*10**6)**2
    #                                                                      +(270*10**3*omega)**2))**2
    #         +((270*10**3*omega)/((-omega**2*(1+270*10**(-3))+10**9+270*10**6)**2+(270*10**3*omega)**2))**2)**(1/2)

def phase_equation_1(omega):
    s = 1j*omega
    return np.angle(
        (s**2+10**9)/(s**2*(1+270*10**(-3))+270*10**3*s+10**9+270*10**6)
    )
    # OLD EQUATIONS
    # return np.arctan(
    #     (((-omega**2+10**9)*(-omega**2*(1+270*10**(-3))+10**9+270*10**6))/((-omega**2*(1+270*10**(-3))+10**9+270*10**6)**2
    #                                                                      +(270*10**3*omega)**2))**2
    #         +((270*10**3*omega)/((-omega**2*(1+270*10**(-3))+10**9+270*10**6)**2+(270*10**3*omega)**2))**2)
    # return np.arctan(
    #     ((270*10**3*omega)/((-omega**2*(1+270*10**(-3))+10**9+270*10**6)**2+(270*10**3*omega)**2)) / 
    #     (((-omega**2+10**9)*(-omega**2*(1+270*10**(-3))+10**9+270*10**6))/((-omega**2*(1+270*10**(-3))+10**9+270*10**6)**2
    #                                                                      +(270*10**3*omega)**2))
    # )


def circuit_1():
    omega_space = np.logspace(1, 7, 20000, base=10)

    max_P = np.abs(((1j*10)**2+10**9)/((1j*10)**2*(1+270*10**(-3))+270*10**3*(1j*10)+10**9+270*10**6))
    line_y = 10**(-3/10)*max_P
    intersections = omega_space[np.isclose(gain_equation_1(omega_space), np.full(20000,line_y), rtol=0.0001)]
    plt.plot(intersections, [line_y, line_y], "go")
    plt.text(intersections[0]/(10**1.6), line_y+0.04, (rf"$\omega$={intersections[0]:.2e} " + r"$s^{-1}$"), fontsize=9)
    plt.text(intersections[1]*(10**0.2), line_y-0.04, (rf"$\omega$={intersections[1]:.2e} " + r"$s^{-1}$"), fontsize=9)

    plt.plot(omega_space, gain_equation_1(omega_space), "mo", markersize=2)
    plt.plot([10,10**7], [line_y, line_y], "b-")
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
