# korzystamy ze strony https://yesno.wtf, która swoje api wystawia na https://yesno.wtf/api

from urllib.request import urlopen
import json

with urlopen('http://yesno.wtf/api') as response:
    odpowiedz_json = response.read()
    print(odpowiedz_json)
    print(type(odpowiedz_json))

    print('---')

    odpowiedz = json.loads(odpowiedz_json)

    print(odpowiedz)
    print(type(odpowiedz))

    print(odpowiedz['answer'])
