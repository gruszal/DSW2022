nazwa_pliku = 'dane2.txt'

plik = open(nazwa_pliku, mode='w', encoding='utf-8')

tekst_do_zapisania = 'Jakiś tekst w pierwszej linii.\nDruga linia.'

plik.write(tekst_do_zapisania)
