import numpy as np

a = np.array([[2, 3], [5, 8]])
print(a)

print(a.sum(), '\n')
print(a.sum(axis=0), '\n')
print(a.sum(axis=1), '\n')

print(a.mean(axis=0), '\n')
print(a.mean(axis=1), '\n')
