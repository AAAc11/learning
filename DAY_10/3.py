"""
Polecenie:
aNapisz funkcję generatora, która generuje kwadraty kolejnych liczb parzystych.
"""


def squares(limit):
    i=0
    counter = 0

    while counter <= limit:
        yield i*i
        i+=2
        counter+=1

for num in squares(5):
    print(num)
