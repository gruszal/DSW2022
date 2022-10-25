class Plecak:
    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc
        self.kolor = 'zielony'
        self.zawartosc = []

    def __str__(self):
        return f'Plecak koloru {self.kolor} o pojemności {self.pojemnosc}l.'

    def dodaj_przedmiot(self, przedmiot):
        self.zawartosc.append(przedmiot)


if __name__ == '__main__':
    p1 = Plecak(30)
    print(p1.zawartosc)
    p1.dodaj_przedmiot('konserwa')

    print(p1.zawartosc)
