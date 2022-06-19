koszykarze = {'Alojzy', 'Benedykt', 'Czesław', 'Dobromił'}
siatkarze = {'Czesław', 'Dobromił', 'Eligiusz'}

siatkarze.add('Franciszek')

print(siatkarze)

sportowcy = koszykarze.union(siatkarze)
print(sportowcy)

dwa_sporty = koszykarze.intersection(siatkarze)
print(dwa_sporty)

tylko_kosz = koszykarze.difference(siatkarze)
print(tylko_kosz)

# Czy Czesław gra w siatkówkę?
print('Czesław' in siatkarze)
