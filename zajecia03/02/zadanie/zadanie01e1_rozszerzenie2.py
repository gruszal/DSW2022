def rysuj_prostokat(a, b, znak='X'):
    for i in range(a):
        for j in range(b):
            if 0 < i < a - 1 and 0 < j < b - 1:
                print(' ', end='')
            else:
                print(znak, end='')
        print()


rysuj_prostokat(1, 1)
print()
rysuj_prostokat(7, 13)
