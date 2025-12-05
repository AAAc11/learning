"""
Napisz funkcję konwertuj_i_czytaj(wartosc), która:
W bloku try próbuje skonwertować wartosc na liczbę całkowitą i wypisuje: "Konwersja
udana.". Jeśli konwersja się nie powiedzie, blok except ValueError powinien
wydrukować: "Błąd konwersji: nieprawidłowy format liczby.".
Blok else (wykonywany tylko, jeśli nie było błędu) powinien wydrukować: "Logika po konwersji.".
Blok finally (wykonywany zawsze) powinien wydrukować: "Zakończono operację.".
Przetestuj funkcję, wywołując ją dla dwóch wartości: '123' i 'abc'.
"""

def convert_and_read(value):
    try:
        value = int(value)
        print("Conversion successful")
    except ValueError:
        print("Invalid number format")
    else:
        print("Logic after conversion")
    finally:
        print("Operation completed\n")

def main():
    convert_and_read(123)
    convert_and_read("abc")

if __name__ == '__main__':
    main()
