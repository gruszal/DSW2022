from datetime import date

wydanie_pythona3 = date(2008, 12, 3)

print(wydanie_pythona3)

print('Rok wydania:', wydanie_pythona3.year)

print(type(wydanie_pythona3.year))

# możemy też dostać się do miesiąca i dnia:
print('Miesiąc:', wydanie_pythona3.month)
print('Dzień:', wydanie_pythona3.day)
