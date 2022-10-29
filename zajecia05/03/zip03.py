a = [12, 13, 14, 15]
b = [2, 3, 4, 5]

c = zip(a, b)

print(c)  # to jest obiekt iteratora

print(next(c))  # 'next' pobiera jeden element z iteratora

print(list(c))
