"""
Polecenie:
Stwórz generator, który będzie generował nieskończony
strumień liczb pierwszych. (W tym przykładzie ograniczamy
go do pierwszych kilku liczb dla testów).
"""

def first_numbers(limit):
    numbers = [2, 3, 4, 5, 6, 7, 8, 9]
    first = 1
    counter = 0
    while  counter < limit:
        for num in numbers:
            if first % num == 0 and first != num:
                break
            if num == 9:
                counter += 1
                yield first
        first+=1

for first in first_numbers(5):
    print(first)