from random import choice, choices, sample

# losowanie jednej litery z wyrazu
wyraz = "Jabłko"

print(choice(wyraz))

print(choices(wyraz, k=2))

print(sample(wyraz, 2))
