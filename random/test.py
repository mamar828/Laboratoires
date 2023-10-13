import numpy as np


a = np.array([
    [1,2],
    [3,3],
    [6,4],
    [10,6]
])

print(np.diff(a, n=1, axis=0))