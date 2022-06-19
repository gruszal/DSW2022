# klucze nie muszą być tylko stringami, kluczem może być każdy obiekt 'immutable'
slownik = {0: 'Alojzy', 1: 'Barnaba', 10: 'Onufry'}

print(slownik)
print(type(slownik))

# taki słownik działa podobnie do listy, ale klucze nie muszą być kolejnymi liczbami naturalnymi
print(slownik[0])
print(slownik[10])
