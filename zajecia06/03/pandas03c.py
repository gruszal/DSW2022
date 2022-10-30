import pandas as pd

a = pd.read_csv('oceny.txt')
b = a.transpose()
b = b.reset_index()
b = b.rename(columns=b.iloc[0])

print(b)

b = b.drop(0)
b.reset_index(inplace=True, drop=True)
print(b)
