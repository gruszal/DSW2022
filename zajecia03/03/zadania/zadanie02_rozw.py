auta = ['Lancia', 'Peugeot', 'Audi', 'Fiat', 'Ford', 'Renault', 'Mitsubishi', 'Subaru', 'Ford', 'Austin']

try:
    indeks = int(input("Podaj indeks producenta aut rajdowych: "))
    print(f"Wybrany producent to: {auta[indeks]}")
except ValueError:
    print("Podana wartość nie jest liczbą naturalną!")
except IndexError:
    print("Nie ma producenta o takim indeksie!")
