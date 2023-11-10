import numpy as np
import scipy
import matplotlib.pyplot as plt





# x_space = np.linspace(-6,1,36)
# i_0 = 10**(-8)
# v_0 = 0.15

# y_space = i_0*(np.e**((x_space+(np.random.random(len(x_space)))/15)/v_0)-1)

# plt.plot(x_space, y_space, "go", markersize=2)
# # plt.show()


# def shockley_equation(v, i_0, v_0):
#     return i_0*(np.e**(v/v_0)-1)

# i_0, v_0 = scipy.optimize.curve_fit(shockley_equation, x_space, y_space)[0]
# print(i_0, v_0)

# x_shockley = np.linspace(-6,1,1000)
# plt.plot(x_shockley, shockley_equation(x_shockley, i_0, v_0), "b-")
# plt.xlabel(r"tension $v_{be}$")
# plt.ylabel(r"courant $i_{ce}$")
# plt.show()


a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
l = [a,b,a]

c = np.stack(l, axis=0)
print(c)
print(np.stack((c,b), axis=0))
