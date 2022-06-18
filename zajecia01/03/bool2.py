# Wyrażenia <, >, <=, >=, ==, != służą do porównana wartości dwóch obiektów.
# Porównywanie wartości obiektów różnych typów może skutkować niespodziewanymi wynikami.

# wyrażenie 3 < 10 oraz bool(3 < 10) działają tak samo: zwracają wartość True albo False
print(3 < 10)
print(bool(3 < 10))  # nie ma potrzeby rzutowania takiego wyrażenia na wartość logiczną

print(5 > 25)  # False

print(3 <= 100)  # True

print(3 >= 101)  # False

print(3 == 101)  # False
print(3 == 3)  # True

print(15 != 4)  # True
