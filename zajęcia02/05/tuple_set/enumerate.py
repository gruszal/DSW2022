imiona = ['Artur', 'Barbara', 'Czesław', 'Danuta']

print(imiona)

print(enumerate(imiona))  # to co tu otrzymujemy to obiekt iteratora

# Iterator zwraca nowe elementy, gdy zostanie "odpytany", np. przez
# pętle for, albo przez funkcję list(), która tworzy nową listę.

print(list(enumerate(imiona)))  # Stworzyliśmy listę, która ma cztery elementy.
