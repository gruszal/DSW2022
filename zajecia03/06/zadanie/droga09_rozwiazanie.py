def oblicz_koszt_przejazdu(dystans, cena_za_litr, spalanie_na_100km=8.5):
    return dystans * spalanie_na_100km / 100 * cena_za_litr


def wczytaj_cene_paliwa(domyslna_cena=7.97):
    cena_za_litr = input(f'Podaj bieżącą cenę paliwa (ENTER aby wpisać {domyslna_cena}): ')
    if cena_za_litr == '':
        return domyslna_cena
    else:
        return float(cena_za_litr)


if __name__ == '__main__':  # zwyczajowa linijka oddzielająca skrypt od definicji
    cena_za_litr = wczytaj_cene_paliwa()

    while True:
        dystans = float(input('Podaj dystans do pokonania: '))

        koszt = oblicz_koszt_przejazdu(dystans, cena_za_litr)

        komunikat = f'Koszt przejechania {dystans}km przy cenie paliwa {cena_za_litr}zł/l to: {round(koszt, 2)}zł'

        print(komunikat)
        with open('obliczenia.txt', mode='a') as plik:
            plik.write(komunikat)
            plik.write('\n')

        odpowiedz = input('Wpisz "n" jeśli chcesz zakończyć: ')
        if odpowiedz == 'n':
            break
