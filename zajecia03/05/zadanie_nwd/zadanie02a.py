from math import gcd


def wczytaj_liczbe_naturalna():
    liczba = int(input('Podaj liczbę naturalną (większą od 0): '))
    if liczba < 1:
        raise ValueError('Podana liczba nie jest większa od 0.')
    return liczba


a = wczytaj_liczbe_naturalna()
b = wczytaj_liczbe_naturalna()

print('Największy wspólny dzielnik liczb {} i {} to {}.'.format(a, b, gcd(a, b)))
