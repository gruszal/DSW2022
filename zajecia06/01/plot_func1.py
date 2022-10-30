# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
import matplotlib.pyplot as plt


def quadratic_function(x):
    a = -1
    b = 2
    c = -10
    return a * x ** 2 + b * x + c


range_of_x = list(range(-10, 10))
print(range_of_x)

range_of_y = [quadratic_function(x) for x in range_of_x]
print(range_of_y)

print(list(zip(range_of_x, range_of_y)))
plt.plot(range_of_x, range_of_y)

plt.show()
