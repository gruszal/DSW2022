import numpy as np

dane = np.loadtxt('liczby.csv', delimiter=',', usecols=(0, 1, -1))  # 'usecols' wskazuje, które kolumny pobrać

print(dane)

# https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes-constructing
dane2 = np.array(dane, dtype=np.int32)
dane3 = dane2 * -2
print(dane3)

np.savetxt('out.csv', dane3, delimiter=',')
