# https://numpy.org/doc/stable/user/basics.io.genfromtxt.html
import numpy as np

dane = np.loadtxt('liczby.csv', delimiter=',')

print(dane)
