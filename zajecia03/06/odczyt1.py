# https://docs.python.org/3/library/functions.html#open

plik = open('dane.txt', mode='r', encoding='utf-8')

zawartosc = plik.read()

print(zawartosc)
