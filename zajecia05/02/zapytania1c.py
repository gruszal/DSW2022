from urllib.request import urlopen

import ssl  # https://clay-atlas.com/us/blog/2021/09/26/python-en-urllib-error-ssl-certificate/
ssl._create_default_https_context = ssl._create_unverified_context

with urlopen('https://yesno.wtf') as response:
    odpowiedz = response.read()
    print(odpowiedz)
