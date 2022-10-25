class Prostokat:
    def __init__(self, a, b):
        self.bok_a = a
        self.bok_b = b

    def __repr__(self):
        return f'Prostokat({self.bok_a}, {self.bok_b})'


if __name__ == '__main__':
    p1 = Prostokat(5, 6)
    print(p1)

    p2 = Prostokat(13, 17)
    print(p2)
