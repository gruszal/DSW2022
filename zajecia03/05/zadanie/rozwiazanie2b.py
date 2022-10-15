from math import pi

from geometria import pole_kola

wartosc = input('Podaj promień koła: ')
try:
    promien = float(wartosc)
except ValueError:
    print(f'Wartość {wartosc} nie jest poprawną liczbą.')
else:
    try:
        print('Pole koła wynosi: ', pole_kola(promien, pi))
    except ValueError:
        print('Nie można obliczyć pola dla ujemnego promienia.')
