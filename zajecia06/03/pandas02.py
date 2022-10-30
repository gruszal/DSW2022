import pandas as pd
import matplotlib.pyplot as plt

dane = {
    'Franek': [4, 1, 5, 3.5, 5, 4],
    'Zbyszek': [5, 3, 2.5, 2, 3, 3.5],
    'Izabela': [4, 4, 5, 2, 4.5, 5.5]
}

a = pd.DataFrame(dane)

# a.plot()
a.plot.bar()  # https://www.shanelynn.ie/bar-plots-in-python-using-pandas-dataframes/

plt.show()
