def pole_trojkata(a, h):
    pole = a * h / 2
    return pole


podstawa = float(input('Podaj podstawę: '))
wysokosc = float(input('Podaj wysokość: '))

pole = pole_trojkata(podstawa, wysokosc)

print(f'Pole trójkąta wynosi {pole}')
