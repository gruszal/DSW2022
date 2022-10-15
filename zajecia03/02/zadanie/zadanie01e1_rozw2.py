def rysuj_prostokat(a, b, znak='X'):
    for i in range(a):
        print(znak * b)


rysuj_prostokat(3, 5)

x = 4
y = 6
rysuj_prostokat(x, y)

rysuj_prostokat(5, 7, '#')
