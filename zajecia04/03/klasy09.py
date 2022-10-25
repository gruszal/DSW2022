class Prostokat:
    def __init__(self, a, b):
        self.bok_a = a
        self.bok_b = b

    def __repr__(self):
        return f'Prostokat({self.bok_a}, {self.bok_b})'

    def pole(self):
        return self.bok_a * self.bok_b


if __name__ == '__main__':
    maly = Prostokat(1, 2)
    sredni = Prostokat(7, 11)
    duzy = Prostokat(32, 54)

    print(maly.pole())
    print(sredni.pole())
    print(duzy.pole())
