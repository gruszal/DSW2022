# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 20, 3, 40]

plt.figure(figsize=(3, 6))

plt.suptitle('Dwa wykresy')

plt.subplot(2, 1, 1)  # można też podawać wartości jako osobne parametry
plt.plot(x, y)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.subplot(2, 1, 2)
plt.bar(x, y)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.show()
