trojkaty = [
    {'a': 12, 'h': 3.5},
    {'a': 1, 'h': 99},
    {'a': 0.6, 'h': 0.02}
]


def pole_trojkata(a, h):
    pole = a * h / 2
    return pole


for trojkat in trojkaty:
    podstawa = trojkat['a']
    wysokosc = trojkat['h']

    pole = pole_trojkata(podstawa, wysokosc)
    print(f'Pole trójkąta wynosi {pole}')
