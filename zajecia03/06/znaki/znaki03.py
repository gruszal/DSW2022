# wpisywanie specjalnych znaków bezpośrednio:

# https://unicode-table.com/pl/00A3/

litera_duze_z = 'Z'
print(litera_duze_z)
print('\x5a')
print('\u005a')

funt = '£'
print(funt)
print('\xa3')  # hex number
print('\u00a3')  # unicode number

suma = '∑'
print(suma)
print('\u2211')
