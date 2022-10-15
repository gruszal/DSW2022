plik = open('dane-cp1250.txt', mode='r')
# jeśli nie podamy parametru encoding, ustawiony będzie domyślny dla systemu operacyjnego
# dla Windowsa, jest to `cp1250` a dla Linuxa/MacOS jest to `utf-8`

zawartosc = plik.read(20)

print(zawartosc)

print(f'wczytano {len(zawartosc)} znaków')
