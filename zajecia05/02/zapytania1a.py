# korzystamy ze strony https://yesno.wtf, która swoje api wystawia na https://yesno.wtf/api

from urllib.request import urlopen
import json

import ssl  # https://clay-atlas.com/us/blog/2021/09/26/python-en-urllib-error-ssl-certificate/
ssl._create_default_https_context = ssl._create_unverified_context

with urlopen('http://yesno.wtf/api') as response:
    odpowiedz_json = response.read()
    print(odpowiedz_json)
    print(type(odpowiedz_json))

    print('---')

    odpowiedz = json.loads(odpowiedz_json)

    print(odpowiedz)
    print(type(odpowiedz))

    print(odpowiedz['answer'])
