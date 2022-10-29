a = [12, 13, 14, 15]
b = [2, 3, 4, 5]

c = zip(a, b)

print(c)  # to jest obiekt iteratora

print(list(c))

print(list(c))  # poprzednia linikja wyczerpała iterator
