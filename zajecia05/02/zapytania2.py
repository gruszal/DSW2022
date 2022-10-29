from urllib.request import urlopen
import json

import ssl  # https://clay-atlas.com/us/blog/2021/09/26/python-en-urllib-error-ssl-certificate/
ssl._create_default_https_context = ssl._create_unverified_context

ile_kosci = 2
ile_scianek = 6

url = f'http://roll.diceapi.com/json/{ile_kosci}d{ile_scianek}'

with urlopen(url) as response:
    odpowiedz_json = response.read()

    wynik = json.loads(odpowiedz_json)

    print(wynik)
