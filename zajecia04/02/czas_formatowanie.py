from datetime import datetime

teraz = datetime.now()
print(teraz)
print(type(teraz))

print()

data_tekst = teraz.strftime('%d-%m-%Y')  # "str-Format-time"
print(data_tekst)
print(type(data_tekst))

# Więcej tu: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
