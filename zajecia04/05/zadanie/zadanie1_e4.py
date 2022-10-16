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


if __name__ == '__main__':
    p1 = Plecak(30)
    print(p1.zawartosc)
    p1.dodaj_przedmiot('konserwa')
    p1.dodaj_przedmiot('butelka wody')
    p1.dodaj_przedmiot('scyzoryk')

    print(p1.zawartosc)

    liczba = p1.ile_przedmiotow()
    print(f'W plecaku znajduje się {liczba} przedmiotów.')
