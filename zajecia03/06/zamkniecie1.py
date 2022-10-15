import time

plik = open('dane.txt', 'r', encoding='utf-8')

print('długie obliczenia...')
time.sleep(30)

print('zamykam plik!')
plik.close()
time.sleep(30)

print('koniec obliczeń!')

# plik jest automatycznie zamykany na koniec działania skryptu
