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


# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
# l = [a,b,a]

# c = np.stack(l, axis=0)
# print(c)
# print(np.stack((c,b), axis=0))



# data = np.array([
#     [70.257799, 0.329000],
#     [70.258024, 0.329000],
#     [70.258248, 0.330000],
#     [70.258136, 0.329000],
#     [70.258136, 0.330000],
#     [70.258074, 0.330000],
#     [70.258124, 0.329000],
#     [70.258111, 0.329000],
#     [70.258049, 0.330000],
#     [70.258061, 0.330000],
#     [70.257712, 0.330000],
#     [70.257974, 0.330000],
#     [70.257986, 0.329000],
#     [70.258124, 0.329000],
#     [70.257962, 0.329000],
#     [70.257824, 0.329000],
#     [70.258360, 0.330000],
#     [70.257762, 0.329000],
#     [70.257787, 0.330000],
#     [70.257937, 0.330000],
#     [70.258149, 0.330000],
#     [70.258124, 0.330000],
#     [70.258373, 0.329000],
#     [70.258485, 0.330000],
#     [70.257974, 0.329000],
#     [70.258485, 0.329000],
#     [70.257874, 0.329000],
#     [70.257849, 0.330000],
#     [70.258336, 0.330000],
#     [70.258423, 0.330000]
# ])

# mean_data = np.mean(data, axis=0)
# print(mean_data[1]**2 / mean_data[0])

# power_d = data[:,1]**2 / data[:,0]
# print(np.mean(power_d))



f = np.array([1,2])
g = np.array([4,5])
h = np.array([7,8])

a = np.append(f,g, axis=1)
print(a)
# print(np.stack((a,h), axis=2))