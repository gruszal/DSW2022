nazwa_pliku = 'dane3.txt'

plik = open(nazwa_pliku, mode='w', encoding='utf-8')

for i in range(10):
    tekst_do_zapisania = f'Linia numer {i}.\n'
    plik.write(tekst_do_zapisania)
