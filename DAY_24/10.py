"""
Masz listę słów. Twoim celem jest: Mapowanie (map): Zamień każde słowo na jego długość.
Mapowanie (map): Podnieś każdą z tych długości do kwadratu (użyj lambda).
"""

words = ["python", "jest", "super"]

length = list(map(lambda x: len(x), words))

square_of_length = list(map(lambda x: x ** 2, length))

print(length)
print(square_of_length)
