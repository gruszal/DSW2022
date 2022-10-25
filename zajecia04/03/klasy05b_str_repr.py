# https://docs.python.org/3/reference/datamodel.html#object.__repr__
# https://docs.python.org/3/reference/datamodel.html#object.__str__

class Prostokat:
    def __init__(self, a, b):
        self.bok_a = a
        self.bok_b = b

    def __str__(self):
        # czytelny dla użytkownika opis obiektu; jeśli jest, __str__ zastępuje __repr__
        return f'Prostokąt o bokach {self.bok_a} i {self.bok_b}'

    def __repr__(self):
        # powinien przypominać tworzenie opisywanego obiektu
        return f'Prostokat({self.bok_a}, {self.bok_b})'


if __name__ == '__main__':
    p1 = Prostokat(5, 6)
    print(p1)  # print() używa __str__()

    p2 = Prostokat(13, 17)
    print(p2)

    lista_prostokatow = [p1, p2]
    print(lista_prostokatow)  # python drukując listę, używa __repr__()