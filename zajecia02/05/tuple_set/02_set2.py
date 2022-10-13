tekst = 'Simple is better than complex.\nComplex is better than complicated.'
print(tekst)

wyrazy = tekst.split()
print(wyrazy)

wyrazy_bez_powtorzen = set(wyrazy)

print(wyrazy_bez_powtorzen)

print("Ilość unialnych wyrazów:", len(wyrazy_bez_powtorzen))
