wyrazy = []

while len(wyrazy) < 3:
    wyraz = input("Proszę podać wyraz: ")
    if wyraz:
        wyrazy.append(wyraz)
        print("Wyrazy na liście:", wyrazy)
