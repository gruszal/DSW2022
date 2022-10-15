import time

with open('dane.txt', 'r', encoding='utf-8') as plik:
    wszystkie_linie = plik.readlines()
    print(wszystkie_linie)

    print('zamknięty?', plik.closed)
    time.sleep(20)

print('zamknięty?', plik.closed)
time.sleep(20)
print('Skrypt zakończył działanie')
