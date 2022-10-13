samochod = {'marka': 'Fiat',
            'model': '126p',
            'rocznik': 1973}

print(samochod)

if 2022 - samochod['rocznik'] >= 25:
    print('Twój {} może być zarejestrowany jako zabytek.'.format(samochod['marka']))
else:
    print('Twój {} jest jeszcze zbyt młody :)'.format(samochod['marka']))
