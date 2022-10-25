class Prostokat:
    def __init__(self, a, b):  # "inicjalizator" obiektu
        self.bok_a = a  # atrybut obiektu
        self.bok_b = b


p1 = Prostokat(5, 6)
print(p1.bok_a, p1.bok_b)

p1.bok_a = 11

print(p1.bok_a, p1.bok_b)

print(p1)
