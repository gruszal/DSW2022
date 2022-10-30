import numpy as np

dane = np.loadtxt('oceny.txt', delimiter=',', dtype=str)

print(dane)

oceny = np.array(dane[:, 1:], dtype=np.float64)
print(oceny)

uczniowie = np.array(dane[:, :1])
print(uczniowie)
