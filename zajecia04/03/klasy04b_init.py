class Prostokat:
    def __init__(self, a, b):
        if a > 0 and b > 0:
            self.bok_a = a
            self.bok_b = b
        else:
            raise ValueError('Jeden z boków jest mniejszy lub równy zero.')


p1 = Prostokat(5, 6)
print(p1.bok_a, p1.bok_b)

p2 = Prostokat(-2, 3)
print(p2.bok_a, p2.bok_b)
