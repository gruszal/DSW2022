from urllib.request import urlopen
import json

ile_kosci = 2
ile_scianek = 6

url = f'http://roll.diceapi.com/json/{ile_kosci}d{ile_scianek}'

with urlopen(url) as response:
    odpowiedz_json = response.read()

    wynik = json.loads(odpowiedz_json)

    print(wynik)
