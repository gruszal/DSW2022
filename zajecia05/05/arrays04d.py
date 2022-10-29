import numpy as np

lista = [2, 4, 1]

a = np.array(lista)
print(a, f'shape:{a.shape}')

a2 = np.expand_dims(a, axis=0)
print(a2, f'shape:{a2.shape}')  # tablica dwuwymiarowa!

a3 = np.expand_dims(a, axis=1)
print(a3, f'shape:{a3.shape}')  # tablica dwuwymiarowa!
