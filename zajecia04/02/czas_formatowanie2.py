from datetime import datetime

teraz = datetime.now()
print(teraz)
print(type(teraz))

print()

# Uwaga! poniższe może wyglądać inaczej na różnych systemach
data_tekst_inaczej = teraz.strftime('%d %B \'%y')
print(data_tekst_inaczej)
print(type(data_tekst_inaczej))

# Więcej tu: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
