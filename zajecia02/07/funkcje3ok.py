# Tak jest dobrze
def dodaj_do_listy_wartosc(a, lista=None):
    if lista is None:
        lista = []
    lista.append(a)
    return lista


wynik = dodaj_do_listy_wartosc(1)
print(wynik)

wynik = dodaj_do_listy_wartosc(2)
print(wynik)

wynik = dodaj_do_listy_wartosc(2, [3, 4])
print(wynik)
