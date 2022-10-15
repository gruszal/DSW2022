lista_trzyelementowa = ['a', 'b', 'c']

try:
    niezadeklarowana_nazwa
    czwarty_element = lista_trzyelementowa[13]
    wynik_dzielenia_przez_zero = 13 / 0
except:  # proszę tak nie pisać
    print('Zdarzyło się coś, co mogło być istotne. '
          'Uciszając wszystko tracimy bardzo ważną część działania Pythona!')

print('Program działa dalej')
