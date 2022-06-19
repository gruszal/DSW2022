dane = input('Wpisz dowolną ilość wyrazów oddzielonych przecinkiem: ')

wyrazy = dane.split(',')

for wyraz in wyrazy:
    wyraz = wyraz.strip()

    if not wyraz:
        continue

    print(f'Wyraz "{wyraz}" ma {len(wyraz)} znaków')
