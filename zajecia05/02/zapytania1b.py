from urllib.request import urlopen
import json

with urlopen('https://yesno.wtf/api') as response:
    odpowiedz_json = response.read()

    odpowiedz = json.loads(odpowiedz_json)

    slownik = {'yes': 'tak', 'no': 'nie'}

    slowo = odpowiedz['answer']

    print(f'Odpowiedź na Twoje pytanie to: {slownik[slowo]}.')
