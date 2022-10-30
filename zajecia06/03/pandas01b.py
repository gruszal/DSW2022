import pandas as pd

dane = {
    'Franek': [4, 1, 5, 3.5, 5, 4],
    'Zbyszek': [5, 3, 2.5, 2, 3, 3.5],
    'Izabela': [4, 4, 5, 2, 4.5, 5.5]
}

a = pd.DataFrame(dane)

seria_nowa = pd.Series([4, 3.5, 3.5, 2, 3.5, 3.5], name='Marta')
print(seria_nowa)

b = a.join(seria_nowa)
print(b)

b['Benek'] = [2, 2.5, 5.5, 2, 4, 4]  # uwaga, edytujemy istniejący data frame
print(b)
