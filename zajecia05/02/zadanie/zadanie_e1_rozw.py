from urllib.request import urlopen

url = 'http://api.nbp.pl/api/cenyzlota/last/30/?format=json'

with urlopen(url) as response:
    odpowiedz_json = response.read()

print(odpowiedz_json)
