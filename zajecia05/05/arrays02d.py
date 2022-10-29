import numpy as np

lista = [[2, 7, 6], [9, 5, 1]]

# https://numpy.org/doc/stable/reference/arrays.dtypes.html
tablica_floatow = np.array(lista, dtype=float)
print(tablica_floatow)


tablica_stringow = np.array(lista, dtype=str)
print(tablica_stringow)
