"""
Polecenie:
Stwórz generator, który będzie generował kolejne liczby
z ciągu Fibonacciego (gdzie każda liczba jest sumą dwóch poprzednich:
0, 1, 1, 2, 3, 5, 8...).
"""

def fibo():
    i=0
    j=1
    yield 0
    x=0
    while x in range(0,20):
        f = i + j
        i=j
        j=j+f-j
        yield f
        x+=1


for num in fibo():
    print(num)
