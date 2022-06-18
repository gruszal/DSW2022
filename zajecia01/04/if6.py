liczba = int(input("Podaj liczbę całkowitą: "))

if liczba > 13:
    print('Wpisana liczba jest większa od 13')

if bool(liczba > 13):  # nie trzeba tak robić, Python robi to za nas
    print('Wpisana liczba jest większa od 13')
