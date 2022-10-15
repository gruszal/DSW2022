lista_trzyelementowa = ['a', 'b', 'c']

try:
    trzynasty_element = lista_trzyelementowa[13]  # pokomentuj te dwie linie, zamień je kolejnością, poeksperymentuj
    wynik_dzielenia_przez_zero = 13 / 0
except ZeroDivisionError:
    print('Ktoś próbował dzielić przez zero!')
except IndexError:
    print('Ktoś próbował sprawdzić wartość pod indeksem, którego nie ma!')

print('Program działa dalej')
