liczba = 42

print(liczba)


def funkcja():
    liczba = 13  # to jest lokalna zmienna, dostępna tylko z wnętrzna funkcji
    print('wewnątrz funkcji:', liczba)


funkcja()  # uruchamiamy funkcję 'funkcja'
print(liczba)  # zmienna o tej samej nazwie poza funkcją nie została nadpisana
