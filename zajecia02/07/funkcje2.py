def pole_trojkata(podstawa, wysokosc, wypisz=False):
    pole = podstawa * wysokosc / 2
    if wypisz:
        print(f"{podstawa} * {wysokosc} / 2 = {pole}")
    return pole


wynik = pole_trojkata(7, 10)
print(wynik)

print()

wynik = pole_trojkata(7, 10, wypisz=True)
print(wynik)

wynik = pole_trojkata(7, 10, True)  # straciliśmy na czytelności, nie wiemy od razu co robi True
print(wynik)
