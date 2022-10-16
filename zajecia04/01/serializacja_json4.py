import json

plik = open('warzywa_i_owoce.json', mode='r')

dane = json.load(plik)  # load wczytuje zawartość prosto z pliku

print(dane)
print(type(dane))

print(dane[0]['nazwa'])
