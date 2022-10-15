print("Początek programu")

try:
    wynik_dzielenia_przez_zero = 13 / 0  # to jest linia, która wywołuje wyjątek
    print("Ta linijka się nie wykona")
except ZeroDivisionError:
    print("Ktoś próbował dzielić przez zero, więc zamiast tego wypisuję ten komunikat")

print('Program działa dalej')

# Hierarchia wyjątków:
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
