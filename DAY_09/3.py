"""
Polecenie:
Użyj reduce, aby obliczyć sumę listy
"""
from functools import reduce

list_of_numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, s: s + x, list_of_numbers)

print(sum)