import numpy as np

dane = np.loadtxt('oceny.txt', delimiter=',', dtype=str)

oceny = np.array(dane[:, 1:], dtype=np.float64)
uczniowie = np.array(dane[:, :1]).flatten()  # Uwaga!

srednie = oceny.mean(axis=1).round(2)
srednia_klasy = oceny.mean().round(2)

print(f'Średnia klasy {srednia_klasy}')
print(srednie)

# działa, ale brzydko
for i in range(len(uczniowie)):
    print(f'{uczniowie[i]} - średnia: {srednie[i]}')
