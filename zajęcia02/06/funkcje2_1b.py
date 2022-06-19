# funkcja, która przyjmująca jeden parametr i zwraca wartość


def dodaj_sto(liczba):
    wynik = liczba + 100
    return wynik  # return kończy wykonywanie funkcji
    print('Ta linia nigdy nie zostanie wykonana')


wartosc = 23

nowa_wartosc = dodaj_sto(wartosc)

print(nowa_wartosc)
