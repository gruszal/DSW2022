dystans = int(input('Wpisz dystans w km: '))

spalanie_na_100km = 8.5
cena_litra = 7.97
koszt = dystans * spalanie_na_100km / 100 * cena_litra

print('Koszt wyprawy to:', koszt)