from urllib.request import urlopen

with urlopen('https://yesno.wtf') as response:
    odpowiedz = response.read()
    print(odpowiedz)
