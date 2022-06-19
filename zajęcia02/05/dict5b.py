osoba = {'imie': 'Guido',
         'nazwisko': 'van Rossum',
         'rok_urodzenia': 1906}

for k in osoba.keys():
    print(k)

print()

print(osoba.keys())  # to jest specjalny obiekt "dict_keys", ułatwiający iterację
print(list(osoba.keys()))  # można zrobić zwykłą listę z "dict_keys"

print()

for wartosc in osoba.values():
    print(wartosc)

print()

print(osoba.values())  # to jest specjalny obiekt "dict_values", ułatwiający iterację
print(list(osoba.values()))  # można zrobić zwykłą listę z "dict_values"
