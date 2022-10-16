from datetime import datetime

# pierwsze połączenie telefoniczne między komputerami
# https://en.wikipedia.org/wiki/History_of_the_Internet#ARPANET

polaczenie = datetime(1969, 10, 29, 22, 30)
print(polaczenie)

teraz = datetime.now()
print(teraz)
print(type(teraz))

roznica = teraz - polaczenie
print(roznica)
print(type(roznica))

print(f'Wydarzyło się to {roznica.days / 365} lat temu')
