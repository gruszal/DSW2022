numbers = [13, 17, 19]

#       obliczenie nowej wartości
#                   vvvvvvvvvvvvv
numbers_with_tax = [number * 1.23 for number in numbers]
#                                     ^^^^^^    ^^^^^^^
#                    bieżący element z listy    ^^^^^^^
#                                          lista bazowa

print(numbers_with_tax)
