from datetime import datetime

poczatek = datetime.now()

input('Naciśnij ENTER')

stop = datetime.now()
roznica = stop - poczatek

print(f'Naciśnięto ENTER po {roznica} sekundach.')
