from sklep import warzywa_i_owoce

print(warzywa_i_owoce)
print(type(warzywa_i_owoce))

plik = open('warzywa_i_owoce.txt', 'w')

plik.write(warzywa_i_owoce)
# tak się nie da :( Metoda write, umie zapisywać do pliku tylko stringi
