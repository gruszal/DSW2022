lista_trzyelementowa = ['a', 'b', 'c']

try:
    trzynasty_element = lista_trzyelementowa[13]  # pokomentuj te dwie linie, zamień je kolejnością, poeksperymentuj
    wynik_dzielenia_przez_zero = 13 / 0
except (ZeroDivisionError, IndexError):
    print('Ktoś próbował dzielić przez zero albo podał nieistniejący indeks!')

print('Program działa dalej')
