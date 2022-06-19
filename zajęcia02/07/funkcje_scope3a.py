lista = ['a', 'b']

print(lista)


def funkcja():
    lista.append('c')
    print('wewnątrz funkcji:', lista)


funkcja()
print(lista)
