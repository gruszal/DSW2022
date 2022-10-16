import json
from sklep import warzywa_i_owoce

print(warzywa_i_owoce)

plik = open('warzywa_i_owoce_a.json', 'a')
# UWAGA! tryb "append" wraz z serializacją do JSONa zwykle produkuje błędne efekty!

json.dump(warzywa_i_owoce, plik)
