print('Początek programu')

try:
    wynik_dzielenia_przez_zero = 13 / 0
except ZeroDivisionError:
    pass  # można też wyciszyć wyjątek, ale nie jest to dobra praktyka

print('Program działa dalej')
