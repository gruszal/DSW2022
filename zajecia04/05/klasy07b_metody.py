class Prostokat:
    def __init__(self, a, b):
        self._bok_a = a  # podkreślenie oznacza atrybut do wewnętrznego użytku
        self._bok_b = b

    def __repr__(self):
        return f'Prostokat({self._bok_a}, {self._bok_b})'

    def pole(self):
        return self._bok_a * self._bok_b

    def powieksz_boki(self, a=0, b=0):
        nowy_a = self._bok_a + a
        nowy_b = self._bok_b + b
        if nowy_a > 0 and nowy_b > 0:
            self._bok_a = nowy_a
            self._bok_b = nowy_b
        else:
            raise ValueError('Prostokat nie może mieć ujemnych boków!')


if __name__ == '__main__':
    p = Prostokat(5, 6)
    print(p)

    p.powieksz_boki(a=10, b=1)
    print(p)

    p._bok_a = -10  # nadal można tak napisać, ale konwencja podpowiada nam, że to zły pomysł
    print(p)


# https://dbader.org/blog/meaning-of-underscores-in-python
