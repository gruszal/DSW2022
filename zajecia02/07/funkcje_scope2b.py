# przykład 01_funkcje_scope2a.py napisany lepiej
sto = 100


def funkcja(drugi_skladnik):  # ta funkcja nie używa zmiennych globalnych
    liczba = 13 + drugi_skladnik
    print(liczba)


funkcja(sto)
