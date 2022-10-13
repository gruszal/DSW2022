osoba = {'imie': 'Guido',
         'nazwisko': 'van Rossum',
         'rok_urodzenia': 1906}

print(osoba)

osoba['rok_urodzenia'] = 1956  # modyfikujemy istniejący klucz. Guido nie jest taki stary :)
print(osoba)

osoba['programista'] = True  # dodajemy nowy klucz
print(osoba)

osoba.pop('rok_urodzenia')  # usuwamy ten klucz ze słownika
print(osoba)
