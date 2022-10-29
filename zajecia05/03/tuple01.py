lista = ['a', 'b', 'c']

print(lista[0])
lista.append('d')
print(lista)
del lista[0]
print(lista)

print()

krotka = ('a', 'b', 'c')
print(krotka)
print(krotka[0])

# tuple(krotki) są niemutowalne. Po stworzeniu nie można zmienić ich zawartości
# del krotka[0]
