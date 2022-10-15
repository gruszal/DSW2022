plik = open('dane-cp1250.txt', 'r', encoding='cp1250')

zawartosc = plik.read(20)
print(zawartosc)

print('---')

zawartosc2 = plik.read(20)
print(zawartosc2)
