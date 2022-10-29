import numpy as np

tablica = np.arange(1, 10, 2)  # jak range()
print(tablica)

tablica2 = np.linspace(1, 10, num=5)  # tablica pięciu równo rozmieszczonych wartości między 1 a 10 (włącznie)
print(tablica2)

tablica3 = np.zeros((2, 3))
print(tablica3)

tablica4 = np.eye(3)
print(tablica4)
