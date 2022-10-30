import numpy as np

a = np.array([[2, 3], [5, 8]])
b = 10
print(a)

a[:, 0] = a[:, 0] + b  # dodanie skalara do pierwszej kolumny
print(a)
