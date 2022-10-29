import numpy as np

a = np.array([[2, 2, 8],
              [5, 4, 3],
              [2, 4, 1],
              [6, 7, 8]])

a2 = a.T  # transpozycja
print(a2, '\n')

a3 = np.flip(a)
print(a3, '\n')

a4 = np.flip(a, axis=0)
print(a4, '\n')

a5 = np.flip(a, axis=1)
print(a5, '\n')
