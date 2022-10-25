class Prostokat:
    def __init__(self, a, b):
        self.bok_a = a
        self.bok_b = b

    def __repr__(self):
        return f'Prostokat({self.bok_a}, {self.bok_b})'

    def pole(self):
        return self.bok_a * self.bok_b


if __name__ == '__main__':
    prostokaty = [Prostokat(1, 2),
                  Prostokat(7, 11),
                  Prostokat(32, 54)]

    print(prostokaty[0].pole())
