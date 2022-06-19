osoba = {'imie': 'Guido',
         'nazwisko': 'van Rossum',
         'rok_urodzenia': 1956}

# Rozpakowywanie krotki dla każdej iteracji pętli
for k, w in osoba.items():
    print('Klucz: {}, wartość: {}'.format(k, w))

print()

# Można też tak, ale nie polecam
for krotka in osoba.items():
    print('Klucz: {}, wartość: {}'.format(krotka[0], krotka[1]))
