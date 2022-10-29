import json
from urllib.request import urlopen

url = 'http://api.nbp.pl/api/cenyzlota/last/30/?format=json'

with urlopen(url) as response:
    odpowiedz = response.read()

odpowiedz_json = json.loads(odpowiedz)

print(odpowiedz_json)
print(type(odpowiedz_json))
print(type(odpowiedz_json[0]))
