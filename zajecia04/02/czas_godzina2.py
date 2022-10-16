from datetime import time

usain_bolt_na_100m = time(0, 0, 9, 580000)  # ostatni argument jest w mikrosekundach

sekundy = usain_bolt_na_100m.second
mikrosekundy = usain_bolt_na_100m.microsecond

print(f'Rekord świata w biegu na 100m: Usain Bolt z czasem {sekundy}.{mikrosekundy}s')
