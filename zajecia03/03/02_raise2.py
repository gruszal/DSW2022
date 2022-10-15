liczba = int(input("Wprowadź swoją szczęśliwą liczbę: "))

if liczba == 13:
    raise ValueError('Ta liczba nie może być szczęśliwa!')

print(f'Twoja szczęśliwa liczba to {liczba}')
