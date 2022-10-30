import numpy as np

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

a = np.array(lista)
print(a)

print(a[0, 2], '\n')  # znak '\n' dodaje dodatkową linię dla czytelności
print(a[0][2], '\n')  # znak '\n' dodaje dodatkową linię dla czytelności

print(a[1:], '\n')

print(a[:-1], '\n')
