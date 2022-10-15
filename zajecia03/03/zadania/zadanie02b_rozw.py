auta = ['Lancia', 'Peugeot', 'Audi', 'Fiat', 'Ford', 'Renault', 'Mitsubishi', 'Subaru', 'Ford', 'Austin']

odpowiedz = input("Podaj indeks producenta aut rajdowych: ")

try:
    indeks = int(odpowiedz)
    producent = auta[indeks]
    print(f"Wybrany producent to: {producent}")
except ValueError:
    print(f"Podana wartość {odpowiedz} nie jest liczbą naturalną!")
except IndexError:
    print(f"Nie ma producenta o indeksie {odpowiedz}!")
