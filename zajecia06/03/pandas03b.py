import pandas as pd


a = pd.read_csv('oceny.txt')
b = a.transpose()
b = b.reset_index()

print(b)

imiona = b.iloc[0]

b = b.rename(columns=imiona)

print(b)
