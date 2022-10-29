import numpy as np

a = np.random.randint(1, 9, size=(4, 3))

print(a)

a2 = a.reshape(2, 6)  # trzeba użyć wszystkich wartości
print(a2)
print(f'size: {a2.size}, ndim: {a2.ndim}, shape: {a2.shape}')

a3 = a.flatten()
print(a3)
print(f'size: {a3.size}, ndim: {a3.ndim}, shape: {a3.shape}')
