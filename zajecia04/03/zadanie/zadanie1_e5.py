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

    def podsumowanie(self):
        print(f'Plecak w kolorze {self.kolor}, o pojemności {self.kolor}l.')
        print(f'Liczba przedmiotów w plecaku: {self.ile_przedmiotow()}')
        for przedmiot in self.zawartosc:
            print(f'- {przedmiot}')


if __name__ == '__main__':
    p1 = Plecak(30)
    p1.dodaj_przedmiot('konserwa')
    p1.dodaj_przedmiot('butelka wody')
    p1.dodaj_przedmiot('scyzoryk')

    p1.podsumowanie()
