# Uruchom skrypt raz z zakomentowaną linią 3, a raz z 4

samochod = {'nazwa': 'Fiat 126p', 'ilość_kół': 4}
# samochod = {'nazwa': 'Fiat 126p', 'ilość_kół': 4, 'rocznik': 1992}

try:
    samochod['rocznik']
except KeyError:
    print('Samochód nie ma wpisanego rocznika! Wpisuję "None", aby dodać brakujący klucz.')
    samochod['rocznik'] = None

print(samochod)
