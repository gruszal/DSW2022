# UWAGA! Ten skrypt jest napisany lepiej w `while_true2.py`

czy_powtorzyc = True  # tej zmiennej można się pozbyć

while czy_powtorzyc:
    odpowiedz = input('Wpisz tekst lub "koniec" aby zakończyć wpisywanie: ')

    if odpowiedz == 'koniec':
        czy_powtorzyc = False
    else:
        print('Wpisano:', odpowiedz)
