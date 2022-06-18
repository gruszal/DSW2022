imiona = ['Artur', 'Barbara']

# dodawanie do listy
imiona.append('Celina')

print(imiona)

# nadpisywanie elementu
imiona[0] = 'Alojzy'

print(imiona)

# odczytanie i usunięcie elementu
skasowany_element = imiona.pop(1)

print('skasowany element:', skasowany_element)

print(imiona)

imiona.pop(0)
print(imiona)
