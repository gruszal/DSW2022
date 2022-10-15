auta = ['Lancia', 'Peugeot', 'Audi', 'Fiat', 'Ford', 'Renault', 'Mitsubishi', 'Subaru', 'Ford', 'Austin']

while True:
    odpowiedz = input("Podaj indeks producenta aut rajdowych: ")

    try:
        indeks = int(odpowiedz)
        producent = auta[indeks]
        break
    except ValueError:
        print(f"Podana wartość {odpowiedz} nie jest liczbą naturalną!")
    except IndexError:
        print(f"Nie ma producenta o indeksie {odpowiedz}!")

print(f"Wybrany producent to: {producent}")
