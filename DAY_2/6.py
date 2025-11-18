def czy_zawiera(element_szukany, *elementy):
    if element_szukany in elementy:
        return True
    return  False

def main():
    print(czy_zawiera("pomidor","kapusta","ogorek","marchew","pomidor","jablka"))

if __name__ == '__main__':
    main()