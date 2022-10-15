def rysuj_prostokat(a, b, znak='X'):
    for i in range(a):
        for j in range(b):
            print(znak, end='')
        print()


rysuj_prostokat(3, 5)

x = 4
y = 6
rysuj_prostokat(x, y)

rysuj_prostokat(5, 7, '#')
