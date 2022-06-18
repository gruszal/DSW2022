# przetestuj rzutowanie na typ 'bool' dla różnych typów danych i różnych ich wartości

print(bool(13))  # True
print(bool(0))  # False
print(bool('tekkst'))  # True
print(bool(''))  # False
print(bool(' '))  # True, gdyż ten string zawiera jeden znak (spację)
print(bool(10.23))  # True
print(bool(0.0))  # False
print(bool(0.00000001))  # True

print(bool(None))  # False
