# https://docs.python.org/3/library/csv.html
import csv
from sklep import warzywa_i_owoce

print(warzywa_i_owoce)

plik = open('warzywa_i_owoce.csv', 'w')
klucze = warzywa_i_owoce[0].keys()  # wyciągamy wszystkie klucze z pierwszego słownika na liście

print(klucze)

writer = csv.DictWriter(plik, fieldnames=klucze)

writer.writeheader()
writer.writerows(warzywa_i_owoce)
