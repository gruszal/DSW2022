import json
from sklep import warzywa_i_owoce

print(warzywa_i_owoce)
print(type(warzywa_i_owoce))

dane_json = json.dumps(warzywa_i_owoce)  # dumps = dump + s(tring)

print()

print(dane_json)

plik = open('warzywa_i_owoce.json', 'w')
plik.write(dane_json)
