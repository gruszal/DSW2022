dane = input('Wpisz dowolną ilość wyrazów oddzielonych przecinkiem: ')

lista = dane.split(',')

print(lista)

for wyraz in lista:
    wyraz = wyraz.strip()

    if wyraz:
        print(f"Wyraz \"{wyraz}\" ma długość {len(wyraz)}")