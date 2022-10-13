# funkcja, która przyjmuje jeden parametr i nie zwraca (wprost) żadnej wartości


def wydrukuj_dodanie_sto(liczba):
    wynik = liczba + 100
    print(f'{liczba} + 100 = {wynik}')


wartosc = 23

# funkcja, która nie ma wewnątrz swojego bloku wyrażenia `return` zwraca `None`
nowa_wartosc = wydrukuj_dodanie_sto(wartosc)

print(nowa_wartosc)
