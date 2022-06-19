osoba = {'imie': 'Guido',
         'nazwisko': 'van Rossum',
         'rok_urodzenia': 1956}

for k in osoba:
    klucz = k
    wartosc = osoba[k]

    print('Klucz: {}, wartość: {}'.format(klucz, wartosc))
