"""
Masz listę liczb całkowitych. Użyj filter i funkcji lambda, aby wybrać tylko liczby parzyste.
"""

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, liczby))
print(even_numbers)

