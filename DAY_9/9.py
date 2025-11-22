"""
Iloczyn z reduce: Użyj reduce (z functools), aby obliczyć iloczyn
wszystkich elementów listy.
"""
from functools import reduce

list_of_numbers = [1, 2, 3, 4, 5]

result = reduce(lambda r,x: r*x,list_of_numbers)

print(result)