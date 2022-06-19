def srednia_arytm(*liczby):
    print(f'liczę średnią dla {liczby}')  # w mamy do dyspozycji tuple o nazwie 'liczby'
    return sum(liczby) / len(liczby)


wynik = srednia_arytm(1, 7, 21, 2)
print(wynik)

wynik = srednia_arytm(1, 7, 21, 2, 7)
print(wynik)

wynik = srednia_arytm(1, 7, 21, 2, 7, 7, 7, 7)
print(wynik)
