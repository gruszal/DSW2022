class Prostokat:
    def __init__(self, a, b):
        self.bok_a = a
        self.bok_b = b

    def __repr__(self):
        return f'Prostokat({self.bok_a}, {self.bok_b})'

    def pole(self):
        return self.bok_a * self.bok_b

    def powieksz_boki(self, a=0, b=0):
        nowy_a = self.bok_a + a
        nowy_b = self.bok_b + b
        if nowy_a > 0 and nowy_b > 0:
            self.bok_a = nowy_a
            self.bok_b = nowy_b
        else:
            raise ValueError('Prostokat nie może mieć ujemnych boków!')


if __name__ == '__main__':
    p = Prostokat(5, 6)
    print(p)

    p.powieksz_boki(a=10, b=1)
    print(p)

    p.powieksz_boki(a=-10, b=-10)  # zakomentuj, aby przejść dalej
    print(p)

    # ale można zrobić tak:

    p.bok_a = -10
    print(p)