from datetime import datetime

poczatek = datetime.now()

input('Naciśnij ENTER')

stop = datetime.now()
roznica = stop - poczatek

sekundy = roznica.seconds
mikrosekundy = roznica.microseconds

print(f'Naciśnięto ENTER po {sekundy + mikrosekundy/1000000} sekundach.')
