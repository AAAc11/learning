def dodawanie(l1):
    return l1+1

def odejmowanie(l1):
    return l1-1

def funkcja(liczby,dzialanie):
    result=[]
    for licza in liczby:
        result.append(dzialanie(licza))
    return result

def main():
    x = [1,2,3,4,5,6,7,8,9]
    print(funkcja(x,dodawanie))
    print(funkcja(x,odejmowanie))
if __name__ == '__main__':
    main()