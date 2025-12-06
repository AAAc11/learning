"""
Utwórz listę zawierającą kwadraty wszystkich liczb parzystych z zakresu od 1 do 30 (włącznie).
Oczekiwany wynik: Lista int.
Wymagana technika: Tylko List Comprehension z warunkiem (if).
"""

def main():
    squares = [x**2 for x in range(1,31) if x % 2 == 0]
    print(squares)

if __name__ == '__main__':
    main()