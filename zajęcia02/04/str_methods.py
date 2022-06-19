tekst = 'test'

print(tekst.isalpha())  # składa się z liter
print(tekst.isnumeric())  # składa się z samych cyfr
print(tekst.islower())  # same małe litery

tekst2 = '     dużo spacji   '

tekst_bez_spacji = tekst2.strip()

print(tekst2)
print(tekst_bez_spacji)

# więcej w dokumentacji https://docs.python.org/3/library/stdtypes.html#string-methods
