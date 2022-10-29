import numpy as np

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

a = np.array(lista)
print(a, '\n')

print(a[1:][1:], '\n')  # tutaj robimy dwa razy operację pobrania wierszy zaczynając od indeksu 1

print(a[1:, 1:], '\n')  # tutaj pobieramy wiersze, zaczynając od indeksu 1 i kolumny, zaczynając od indeksu 1
