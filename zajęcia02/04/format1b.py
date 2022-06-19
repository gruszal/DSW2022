liczba = 12
tekst = 'coś jest napisane'

szablon = 'Zmienna "liczba" ma wartość: {} a tu jest tekst: {}'

print(szablon)

print(szablon.format(liczba, tekst))

print(szablon.format(1234, 'zupełnie inny tekst'))
