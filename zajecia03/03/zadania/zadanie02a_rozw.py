auta = ['Lancia', 'Peugeot', 'Audi', 'Fiat', 'Ford', 'Renault', 'Mitsubishi', 'Subaru', 'Ford', 'Austin']

try:
    indeks = int(input("Podaj indeks producenta aut rajdowych: "))
except ValueError:
    print("Podana wartość nie jest liczbą naturalną!")
    exit()  # kończy działanie skryptu

try:
    producent = auta[indeks]
except IndexError:
    print("Nie ma producenta o takim indeksie!")
    exit()

print(f"Wybrany producent to: {producent}")
