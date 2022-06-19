zen = [['The', 'Zen', 'of', 'Python,', 'by', 'Tim', 'Peters'],
       ['Beautiful', 'is', 'better', 'than', 'ugly.'],
       ['Explicit', 'is', 'better', 'than', 'implicit.']]

wyrazy_dwa_znaki = []

for linia in zen:
    print("sprawdzam listę:", linia)
    for wyraz in linia:
        if len(wyraz) == 2:
            wyrazy_dwa_znaki.append(wyraz)

print()
print("Wyrazy z dwoma znakami:", wyrazy_dwa_znaki)
