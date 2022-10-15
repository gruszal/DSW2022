# https://docs.python.org/3/library/string.html
import string

print(string.ascii_letters)
print(string.ascii_letters[13])

print(string.punctuation)

print(string.whitespace)  # białe znaki, takie jak spacja, tab, enter

print(string.whitespace.encode())  # jeśli NAPRAWDĘ chcemy je zobaczyć, oto jest sposób
