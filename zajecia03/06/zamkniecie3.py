with open('dane.txt', 'r', encoding='utf-8') as plik:
    wszystkie_linie = plik.readlines()
    print(wszystkie_linie)
    print('zamknięty?', plik.closed)

print('zamknięty?', plik.closed)

plik.read()  # po zamknięciu pliku skrypt zamkniecie3.py nie ma już do niego dostępu
