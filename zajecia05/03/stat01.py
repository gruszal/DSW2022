# https://docs.python.org/3/library/statistics.html
from statistics import mean, median, mode

a = [10, 5, 9, 7, 1, 1]

srednia = mean(a)
print(srednia)

mediana = median(a)
print(mediana)

dominanta = mode(a)
print(dominanta)
