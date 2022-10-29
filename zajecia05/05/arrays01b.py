import numpy as np

lista = [1, 2, 3, 4, 5, 'sześć']

print(lista, type(lista))

tablica = np.array([1, 2, 3, 4, 5, 'sześć'])
# tablice muszą przechowywać dane jednego typu, w tym przypadku dostaliśmy tablicę STRINGÓW

print(tablica, type(tablica), tablica.dtype)
