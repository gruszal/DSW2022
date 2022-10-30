# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
import matplotlib.pyplot as plt
import numpy as np

x = [[1, 2, 3, 4], [1, 20, 3, 40]]

table = np.array(x)

plt.plot(table)  # plot przyjmuje także obiekty ndarray z numpy

plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.show()
