import numpy as np

dane = np.loadtxt('oceny.txt', delimiter=',', dtype=str)

oceny = np.array(dane[:, 1:], dtype=np.float64)
uczniowie = np.array(dane[:, :1]).flatten()  # Uwaga!

wagi_ocen = (0.5, 1, 0.5, 0.5, 1, 1)

# https://numpy.org/doc/stable/reference/generated/numpy.average.html
srednie = np.average(oceny, axis=1, weights=wagi_ocen).round(2)
srednia_klasy = srednie.mean().round(2)

print(f'Średnia klasy {srednia_klasy}')
print(srednie)
print(list(zip(uczniowie, srednie)))  # tylko do sprawdzenia poprawności

for uczen, srednia in zip(uczniowie, srednie):
    print(f'{uczen} - średnia: {srednia}')
