import matplotlib.pyplot as plt


def linear_function(x):
    a = -2
    b = 1
    return a * x + b


def quadratic_function(x):
    a = -1
    b = 2
    c = -10
    return a * x ** 2 + b * x + c


x = list(range(-10, 10))

y = [quadratic_function(x) for x in x]
plt.plot(x, y, 'r--')

y = [linear_function(x) for x in x]
plt.plot(x, y, 'b')

plt.xlabel('x')
plt.ylabel('y')

plt.show()
