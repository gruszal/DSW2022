# Skrypt generujący plik 'slodycze.csv'
import csv
from sklep import slodycze

plik = open('slodycze.csv', 'w')
klucze = slodycze[0].keys()  # wyciągamy wszystkie klucze z pierwszego słownika na liście

writer = csv.DictWriter(plik, fieldnames=klucze)
writer.writeheader()
writer.writerows(slodycze)
