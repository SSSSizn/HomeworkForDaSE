import random
import math


def f(x):
    return x**2 + 4*x*math.sin(x)


def monte_carlo_integration(times):
    start = 2
    end = 3
    sum = 0

    for _ in range(times):
        x = random.uniform(start, end)
        y = f(x)
        sum += y

    average = sum / times
    result = (end - start) * average
    return result


times = 100000
result = monte_carlo_integration(times)
print(result)
