lista = ['a', 'b']

print(lista)


def funkcja():
    lista = ['x', 'y']
    lista.append('c')
    print('wewnątrz funkcji:', lista)


funkcja()
print(lista)
