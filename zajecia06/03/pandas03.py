import pandas as pd


a = pd.read_csv('oceny.txt')

print(a)

b = a.transpose()

print(b)

b = b.reset_index()

print(b)
