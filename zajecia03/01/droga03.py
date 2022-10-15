dystans = float(input('Podaj dystans do pokonania: '))

spalanie_na_100km = 8.5
cena_za_litr = 7.97
koszt = dystans * spalanie_na_100km / 100 * cena_za_litr

# f-string do wygodnego umieszczania wartości w stringu
print(f'Koszt przejechania {dystans}km to: {round(koszt, 2)}zł')
#                                           ^
#                    w klamerkach można umieścić PROSTE funkcje
