# wpisywanie specjalnych znaków bezpośrednio:

tekst_pl = 'piękny tekst'

zakodowany = tekst_pl.encode()
print(zakodowany)
print(type(zakodowany))

print(b'\xc4\x99'.decode())

# litera 'ę' : https://unicode-table.com/pl/0119/
