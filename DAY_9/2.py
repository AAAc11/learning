"""
Polecenie:
Użyj filter, aby wybrać liczby parzyste
"""

list_of_numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, list_of_numbers))

print(even_numbers)