import json

slownik = {1: 'jeden', 2: 'dwa'}  # UWAGA: słownik, który jako klucze ma obiekty typu 'int'

print('slownik:', slownik)
print(type(slownik))

dane_json = json.dumps(slownik)
print('json:', dane_json)
print(type(dane_json))

slownik_z_jsona = json.loads(dane_json)
print('slownik:', slownik_z_jsona)  # klucze w formacie JSON zawsze są stringami
print(type(slownik_z_jsona))
