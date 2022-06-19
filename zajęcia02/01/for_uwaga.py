el = 'Ważny tekst'
print('zawartość el:', el)

print()

# używając w pętli wcześniej zadeklarowanej zmiennej NADPISUJEMY JĄ!
for el in ['jeden', 'dwa', 'trzy']:
    print('element:', el)

print()

print('zawartość el:', el)  # straciliśmy string 'Ważny tekst'
