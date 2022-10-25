class Prostokat:
    def __init__(self, a, b):
        self.bok_a = a
        self.bok_b = b

    def __str__(self):
        obliczone_pole = self.pole()
        return f'Prostokąt a={self.bok_a}, b={self.bok_b}, P={obliczone_pole}'

    def pole(self):
        return self.bok_a * self.bok_b


class Kwadrat(Prostokat):
    def __init__(self, a):
        Prostokat.__init__(self, a, a)


if __name__ == '__main__':
    p = Prostokat(5, 6)
    print(p)
    print(p.pole())

    k = Kwadrat(11)
    print(k)
    print(k.pole())
