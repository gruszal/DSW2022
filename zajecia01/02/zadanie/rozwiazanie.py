dystans_tekst = input()  # wczytanie danych z klawiatury
dystans = int(dystans_tekst)  # zamiana tekstu na liczbę całkowitą

spalanie_na_100km = 8.5
cena_litra = 7.97
koszt = dystans * spalanie_na_100km / 100 * cena_litra

print('Koszt wyprawy to:', koszt)