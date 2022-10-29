from urllib.request import urlopen
import json

import ssl  # https://clay-atlas.com/us/blog/2021/09/26/python-en-urllib-error-ssl-certificate/
ssl._create_default_https_context = ssl._create_unverified_context

with urlopen('https://yesno.wtf/api') as response:
    odpowiedz_json = response.read()

    odpowiedz = json.loads(odpowiedz_json)

    slownik = {'yes': 'tak', 'no': 'nie'}

    slowo = odpowiedz['answer']

    print(f'Odpowiedź na Twoje pytanie to: {slownik[slowo]}.')
