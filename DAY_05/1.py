try:
    liczb1=int(input("Podaj pierwszą liczbę: "))
    znak=input("Podaj znak: ")
    liczb2 = int(input("Podaj drugą liczbę: "))
    match znak:
        case '+':
            print(liczb1+liczb2)
        case '-':
            print(liczb1-liczb2)
        case '*':
            print(liczb1*liczb2)
        case '/':
            print(liczb1/liczb2)



except ValueError:
    print("To nie jest liczba!")
except ZeroDivisionError:
    print("Nie wolno dzielic przez zero!")