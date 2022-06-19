def wypisz_cztery(a, b, c, d):
    print(f'Przekazano cztery argumenty: {a}, {b}, {c}, {d}')


wypisz_cztery('arbuz', 'banan', 'cytryna', 'daktyl')

# można także podać argumenty po nazwie
wypisz_cztery(a='arbuz', b='banan', c='cytryna', d='daktyl')

# podając argumenty po nazwie, kolejność jest nieważna
wypisz_cztery(d='daktyl', c='cytryna', b='banan', a='arbuz')

# można też używać metody mieszanej
# argumenty pozycyjne muszą być przed podawanymi po nazwie
wypisz_cztery('arbuz', 'banan', d='daktyl', c='cytryna')
