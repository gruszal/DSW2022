odpowiedz = input("Tak czy nie? [t/n]: ")

if odpowiedz == 'T' or odpowiedz == 't':  # każda strona "or" jest sprawdzana oddzielnie
    print('TAK!')
elif odpowiedz == 'N' or odpowiedz == 'n':
    print('NIE')
else:
    print('Nie rozumiem')
