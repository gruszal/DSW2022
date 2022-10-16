# https://docs.python.org/3/library/csv.html
import csv

plik = open('slodycze.csv', 'r')

reader = csv.DictReader(plik)  # czytnik przygotowany specjalnie dla list słowników z nagłówkiem

slodycze = list(reader)

print(slodycze)

nazwa_pierwszego_art = slodycze[1]['nazwa']

print(nazwa_pierwszego_art)

# UWAGA: Wszystkie wartości stały się stringami!
