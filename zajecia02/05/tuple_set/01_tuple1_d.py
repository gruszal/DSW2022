adres = ('Fundacja CODE:ME',
         'aleja Wojska Polskiego 41',
         '80-268 Gdańsk')

# Jeśli nie planujemy użyć którejś z wartości z tupli, możemy użyć w jej miejscu znaku "_"
nazwa, ulica, _ = adres

print(nazwa)
print(ulica)
