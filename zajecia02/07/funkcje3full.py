# Unikaj przypisywania argumentom domyślnym wartości mutowalnych i wyliczanych w momencie definiowania
def dodaj_do_listy_wartosc(a, lista=[]):
    lista.append(a)
    return lista


wynik = dodaj_do_listy_wartosc(1)
print(wynik)

wynik = dodaj_do_listy_wartosc(2)
print(wynik)  # CO?!
