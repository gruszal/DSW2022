import numpy as np
import matplotlib.pyplot as plt

dane = np.loadtxt('oceny.txt', delimiter=',', dtype=str)
oceny = np.array(dane[:, 1:], dtype=np.float64)
uczniowie = np.array(dane[:, :1]).flatten()  # Uwaga!

wagi_ocen = (0.5, 1, 0.5, 0.5, 1, 1)

# https://numpy.org/doc/stable/reference/generated/numpy.average.html
srednie = np.average(oceny, axis=1, weights=wagi_ocen).round(2)


plt.figure(figsize=(9, 3))

for i, dane in enumerate(zip(oceny, srednie), start=1):
    plt.subplot(1, len(oceny), i)  # ile wierszy, ile kolumn, index
    plt.plot(dane[0])
    plt.axhline(y=dane[1], color='red')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.show()
