import string


def usun_interpunkcje(tekst):
    # uwaga! string.punctuation nie posiada wszystkich (narodowych) znaków interpunkcyjnych
    for znak_interpunkcyjny in string.punctuation:
        tekst = tekst.replace(znak_interpunkcyjny, '')
    return tekst


wierszyk = '''Pan kotek był chory i leżał w łóżeczku,
I przyszedł kot doktór: „Jak się masz koteczku!”
„Źle bardzo...” i łapkę wyciągnął do niego.
Wziął za puls pan doktór poważnie chorego,'''

wierszyk_nowy = usun_interpunkcje(wierszyk)

print(wierszyk_nowy)
