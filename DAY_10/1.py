"""
Polecenie:
Generator liczb od 1 do 100.
"""

def generator(start, stop):
    i=start
    while i<=stop:
        yield i
        i+=1


for num in generator(1,100):
    print(num)
