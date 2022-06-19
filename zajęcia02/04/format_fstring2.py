# f-string (od Pythona 3.6)

ilosc_uczniow = 28
budzet = 1000.00

tekst1 = f'każdy z {ilosc_uczniow} może dostać upominek za {budzet / ilosc_uczniow:.2f}zł'

# Nie należy wpisywać zbyt dużo obliczeń w nawiasy klamrowe

# :.2f powoduje, że wartość jest zaokrąglona do dwóch miejsc po przecinku

# https://docs.python.org/3/library/string.html#format-specification-mini-language

print(tekst1)
