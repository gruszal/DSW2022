# zaczynamy z listą imiona
imiona = ['Artur', 'Barbara', 'Czesław']

# wchodząc do pętli, program:
# 1. pobiera pierwszy element z listy `imiona` i wpisuje go do zmiennej `imie`.
#    jeśli nie uda się pobrać elementu, "wychodzi" z pętli, czyli idzie do linii `print('Koniec programu')`
# 2. wykonuje blok pętli (czyli `print(imię)`)
# 3. gdy blok pętli się skończy (skończą się "wcięte" linijki), wracamy do punktu pierwszego

for imie in imiona:
    print(imie)

print('Koniec programu')
