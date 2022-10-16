import json
# https://docs.python.org/3/library/pprint.html
from pprint import pprint

plik = open('warzywa_i_owoce.json', mode='r')

dane = json.load(plik)  # load wczytuje zawartość prosto z pliku

pprint(dane)  # wydrukowane "ładniej"
