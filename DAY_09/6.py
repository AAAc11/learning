"""
Polecenie:
Posortuj listę krotek na podstawie drugiego
elementu (liczby) w każdej krotce, używając
funkcji lambda jako argumenty key w funkcji sorted.
"""

tup = [('jabłko', 10), ('banan', 3), ('pomarańcza', 7)]

sort = sorted(tup, key = lambda x: x[1])

print(sort)