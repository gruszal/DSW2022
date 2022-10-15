dystans = float(input('Podaj dystans do pokonania: '))  # wczytywanie danych od użytkownika

spalanie_na_100km = 8.5
cena_za_litr = 7.97
koszt = dystans * spalanie_na_100km / 100 * cena_za_litr

print('Koszt wyprawy to:', koszt)
