def srednia_arytm(*liczby):
    print(f'liczę średnią dla {liczby}')
    return sum(liczby) / len(liczby)


oceny = (5, 3.5, 4, 2.5, 5)

wynik = srednia_arytm(*oceny)
print(wynik)
