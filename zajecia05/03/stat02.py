# https://docs.python.org/3/library/statistics.html
from statistics import NormalDist, stdev, median

a = [10, 5, 9, 7, 1, 1]

odchylenie_std = stdev(a)
mediana = median(a)

n = NormalDist(mediana, odchylenie_std)  # rozkład normalny

print(n.samples(10))

print(n.quantiles())
