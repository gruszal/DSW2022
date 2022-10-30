# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 20, 3, 40]

plt.plot(x, y)
plt.plot(x, y, 'ro')  # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

ax = plt.gca()  # gca = get current axes

ax.set_xticks(x)
ax.set_yticks(y)

plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.show()
