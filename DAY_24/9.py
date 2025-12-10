"""
Masz listę wyników finansowych (zyski i straty). Twoim celem jest:
Filtrowanie (filter): Wybierz tylko te wyniki, które są dodatnie (zyski).
Redukcja (reduce): Oblicz sumę tych zysków.
Obliczanie: Podziel sumę przez liczbę zysków, aby uzyskać średnią.
"""
from functools import reduce

wyniki = [100, -50, 200, 0, 75, -10]

profit = list(filter(lambda x: x > 0, wyniki))

profit_sum = reduce(lambda a, b: a + b, profit)

average_profit = profit_sum / len(profit)

print(profit)
print(average_profit)
