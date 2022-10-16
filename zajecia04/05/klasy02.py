class Prostokat:
    pass


p = Prostokat()
print(p)

# możemy tworzyć nowe atrybuty "w biegu"
p.bok_a = 7
p.bok_b = 13

pole = p.bok_a * p.bok_b

print(pole)
