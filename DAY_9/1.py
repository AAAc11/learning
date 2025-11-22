"""
Polecenie:
Użyj map, aby zamienić listę liczb na listę stringów
"""

list_of_numbers = [1, 2, 3, 4, 5]
list_of_str = list(map(lambda x: str(x),list_of_numbers))

print(list_of_str)