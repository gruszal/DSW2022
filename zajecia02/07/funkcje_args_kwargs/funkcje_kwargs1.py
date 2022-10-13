def podaj_nowa_cene(przedmiot, cena, procent_obnizki):
    nowa_cena = cena * (100 - procent_obnizki) / 100
    print(f'Po obniżce o {procent_obnizki}% {przedmiot} kosztuje {nowa_cena:.2f}zł.')


podaj_nowa_cene('Plecak', 120, 15)

artykul = {'przedmiot': 'Torba',
           'cena': 250}

podaj_nowa_cene(**artykul, procent_obnizki=25)
podaj_nowa_cene(przedmiot='Torba', cena=250, procent_obnizki=25)  # to samo co linijka wyżej

# można i tak:

artykul_do_przeceny = {'przedmiot': 'Torba',
                       'cena': 250,
                       'procent_obnizki': 25}

podaj_nowa_cene(**artykul_do_przeceny)
