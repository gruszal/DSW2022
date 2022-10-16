# https://docs.python.org/3/library/csv.html
import csv

plik = open('slodycze.csv', 'r')

reader = csv.reader(plik)  # zwykły "czytnik" csv, każdy wiersz interpretuje jako listę

slodycze = list(reader)

print(slodycze)
