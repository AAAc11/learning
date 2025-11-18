
def oblicz_srednia(*liczby):
    liczby=liczby[0]
    if len(liczby)==0:
        return None
    return sum(liczby)/len(liczby)

def main():
    x = [1,2,3,4,5,6,7,8,9]
    print(oblicz_srednia(x))
main()