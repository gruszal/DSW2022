plik = open('dane.txt', mode='rb')

zawartosc = plik.read()
print(zawartosc)

print('---')

odkodowana = zawartosc.decode(encoding='cp1250')  # cp1250 standardowe na Windowsie
print(odkodowana)

print('---')

odkodowana = zawartosc.decode(encoding='utf-8')
print(odkodowana)
