# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 20, 3, 40]


plt.figure(figsize=(9, 3))  # początkowe ustawienie okna

plt.suptitle('Dwa wykresy')

plt.subplot(131)  # ile wierszy, ile kolumn, indeks
plt.plot(x, y)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# plt.subplot(132)
# plt.plot(x, y, 'r^')
# plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.subplot(133)
plt.bar(x, y)
plt.grid(color='gray', linestyle='--', linewidth=0.5)



plt.show()
