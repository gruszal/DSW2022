import numpy as np

a = np.array([[2, 3], [5, 8]])
print(a)

a2 = np.insert(a, 0, [[10, 11]], axis=0)
print(a2)
