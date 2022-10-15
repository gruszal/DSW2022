# https://docs.python.org/3/library/fractions.html
from fractions import Fraction

u1 = Fraction(3, 7)
u2 = Fraction(5, 13)

print(u1)
print(type(u1))

suma = u1 + u2

print(f'{u1} + {u2} = {suma}')
