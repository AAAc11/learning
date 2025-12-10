"""
Masz listę liczb. Użyj reduce i funkcji lambda, aby obliczyć sumę wszystkich elementów na liście.
"""
from functools import reduce

dane = [10, 5, 8, 2]

sum = reduce(lambda a,b: a + b, dane)
print(sum)

