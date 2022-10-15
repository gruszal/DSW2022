from math import gcd

a = int(input('Podaj pierwszą liczbę całkowitą: '))
b = int(input('Podaj drugą liczbę całkowitą: '))

print('Największy wspólny dzielnik liczb {} i {} to {}.'.format(a, b, gcd(a, b)))
