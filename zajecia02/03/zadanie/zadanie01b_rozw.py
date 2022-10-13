wyrazy = []

OCZEKIWANA_ILOSC = 3

while len(wyrazy) < OCZEKIWANA_ILOSC:
    wyraz = input("Proszę podać wyraz: ")
    if wyraz:
        wyrazy.append(wyraz)
        print("Wyrazy na liście:", wyrazy)

    print("Zostało", OCZEKIWANA_ILOSC - len(wyrazy), "wyrazów do wpisania.")
