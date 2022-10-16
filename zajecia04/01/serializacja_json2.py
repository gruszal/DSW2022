import json
from sklep import warzywa_i_owoce

print(warzywa_i_owoce)

plik = open('warzywa_i_owoce.json', 'w')

json.dump(warzywa_i_owoce, plik)  # dump pisze bezpośrednio do pliku
