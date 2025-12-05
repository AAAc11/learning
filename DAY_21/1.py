"""
Polecenie:
Zdefiniuj własną klasę wyjątku o nazwie UjemnaWartośćBłąd, która dziedziczy
po wbudowanej klasie Exception.
Napisz funkcję oblicz_pierwiastek(liczba), która:
Przyjmuje jako argument liczbę.
Jeśli liczba jest ujemna, zgłasza (instrukcją raise) wyjątek UjemnaWartośćBłąd z komunikatem
np. "Wartość nie może być ujemna dla tej operacji.".
W przeciwnym razie zwraca pierwiastek kwadratowy z tej liczby.
Użyj bloku try...except do wywołania funkcji dla liczby -9 i obsłuż
tylko wyjątek UjemnaWartośćBłąd, drukując jego komunikat.
"""

class NegativeValueError(Exception):
    pass

def calculate_element(num):
    try:
        if num < 0:
            raise NegativeValueError
        return num ** 0.5
    except NegativeValueError:
        print(f"Number {num} cannot be negative!")

def main():
    print(f"Square root of a number 9 is: {calculate_element(9)}")
    print(f"Square root of a number -5 is: {calculate_element(-5)}")

if __name__ == '__main__':
    main()