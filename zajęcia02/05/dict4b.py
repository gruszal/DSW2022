osoba = {'imie': 'Guido',
         'nazwisko': 'van Rossum',
         'rok_urodzenia': 1906}

zawod = osoba.get('zawod')  # to zadziała, jeśli nie ma takiego klucza, dostaniemy None
print(zawod)

zawod = osoba.get('zawod', 'programista')  # można też ustawić domyślną wartość
print(zawod)
print(osoba)

zawod = osoba.get('zawod') or 'programista'  # można też tak
print(zawod)
print(osoba)
