from random import choice, choices, sample

elementy = ['arbuz', 'banan', 'cytryna', 'daktyl', 'figa', 'granat']

print(choice(elementy))

print(choices(elementy, k=2))  # uwaga! elementy mogą się powtarzać

print(sample(elementy, 2))  # elementy nie będą się powtarzać
