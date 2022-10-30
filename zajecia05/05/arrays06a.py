import numpy as np

a = np.array([[2, 3], [5, 8]])
print(a, '\n')

a2 = np.append(a, [10, 11])
print(a2, '\n')

a3 = np.append(a, [[10, 11]], axis=0)  # uwaga na wymiary!
print(a3, '\n')

a4 = np.append(a, [[10], [11]], axis=1)
print(a4)
