imiona = ['Artur', 'Barbara']
print(imiona)

imiona_nowe = imiona  # "imiona_nowe" wskazuje na ten sam obiekt w pamięci

imiona_nowe[0] = 'Abelard'  # zmieniamy indeks 0 obiektu, na który wskazuje "imiona_nowe"

print(imiona_nowe)
print(imiona)  # zmiana jest również widoczna tu
