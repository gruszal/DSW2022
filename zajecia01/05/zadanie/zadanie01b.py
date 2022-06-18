imiona = ['Artur', 'Barbara', 'Czesław']

print(imiona)

nowe_imie = input('Proszę podać nowe imię: ')

imiona.append(nowe_imie)

print(imiona)

imiona[0] = 'Guido'

print(imiona)

indeks = int(input('Proszę podać indeks imienia do skasowania: '))

skasowane_imie = imiona.pop(indeks)
print("Skasowano imię: ", skasowane_imie)
print(imiona)
