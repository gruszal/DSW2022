# https://numpy.org/doc/stable/user/absolute_beginners.html
import numpy as np

lista = [1, 2, 3, 4, 5, 6]

print(lista, type(lista))

tablica = np.array([1, 2, 3, 4, 5, 6])

print(tablica, type(tablica))

lista2 = tablica.tolist()  # tablica -> lista
print(lista2, type(lista2))
