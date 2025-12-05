"""
Napisz funkcję wykonaj_dzielenie(a, b), która używa bloku try...except...else...finally.
W bloku try wykonaj operację a / b.
Obsłuż w oddzielnych blokach except dwa wbudowane wyjątki:
ZeroDivisionError: wydrukuj "Błąd: Nie można dzielić przez zero!".
TypeError: wydrukuj "Błąd: Argumenty muszą być liczbami!".
W bloku else wydrukuj "Dzielenie przebiegło pomyślnie."
W bloku finally wydrukuj "Sprawdzenie zasobów zakończone."
Przetestuj funkcję dla par argumentów: (10, 2), (10, 0), (10, 'x').
"""

def division(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Error. Cannot divide by 0!")
    except TypeError:
        print("Error. Arguments must be digits!")
    else:
        print("Division completed successfully")
        return a / b
    finally:
        print("Operation completed\n")

def main():
    division(10, 2)
    division(10, 0)
    division(10, 'x')

if __name__ == '__main__':
    main()