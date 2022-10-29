import json
from urllib.request import urlopen

url = 'http://api.nbp.pl/api/cenyzlota/last/30/?format=json'

with urlopen(url) as response:
    odpowiedz = response.read()

odpowiedz_json = json.loads(odpowiedz)

ceny_zlota = []
for notowanie in odpowiedz_json:
    cena = notowanie['cena']
    ceny_zlota.append(cena)

print(ceny_zlota)
