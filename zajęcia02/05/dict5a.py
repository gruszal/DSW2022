osoba = {'imie': 'Guido',
         'nazwisko': 'van Rossum',
         'rok_urodzenia': 1906}

# inaczej niż gdy iterujemy po liście, iterując po słowniku dostajemy klucze a nie wartości
for k in osoba:
    print('klucz ->', k)
