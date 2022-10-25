class Plecak:
    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc
        self.kolor = 'zielony'

    def __str__(self):
        return f'Plecak koloru {self.kolor} o pojemności {self.pojemnosc}l.'


if __name__ == '__main__':
    p1 = Plecak(30)
    print(p1)

    p2 = Plecak(45)
    p2.kolor = 'kamuflaż'
    print(p2)
