import json
from sklep import warzywa_i_owoce

print(warzywa_i_owoce)
print(type(warzywa_i_owoce))

dane_json = json.dumps(warzywa_i_owoce)  # dumps = dump + s(tring)

print()

print(dane_json)
print(type(dane_json))


# https://docs.python.org/3/library/json.html#module-json