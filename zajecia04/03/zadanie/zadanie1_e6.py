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

    p2 = Plecak(24)
    p2.dodaj_przedmiot('saperka')
    p2.dodaj_przedmiot('paprykarz szczeciński')

    p3 = Plecak(60)
    p3.dodaj_przedmiot('książka o survivalu')
    p3.dodaj_przedmiot('baton')
    p3.dodaj_przedmiot('mapa')

    plecaki = [p1, p2, p3]

    for plecak in plecaki:
        plecak.podsumowanie()
        print()
