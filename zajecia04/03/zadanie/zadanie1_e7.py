class Plecak:
    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc
        self.kolor = 'zielony'
        self.zawartosc = []

    def __str__(self):
        return f'Plecak koloru {self.kolor} o pojemności {self.pojemnosc}l.'

    def dodaj_przedmiot(self, przedmiot):
        self.zawartosc.append(przedmiot)

    def ile_przedmiotow(self):
        return len(self.zawartosc)


class NiebieskiPlecak34(Plecak):
    def __init__(self):
        super().__init__(34)
        self.kolor = 'niebieski'


if __name__ == '__main__':
    np = NiebieskiPlecak34()
    print(np)

    np.dodaj_przedmiot('latarka')
    print(np.zawartosc)
