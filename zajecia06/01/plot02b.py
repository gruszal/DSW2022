# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
import matplotlib.pyplot as plt

x = [[1, 2, 3, 4], [1, 20, 3, 40]]

plt.plot(*x)  # UWAGA! rozpakowanie

plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.show()
