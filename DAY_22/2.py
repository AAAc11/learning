"""
Masz słownik: kody = {'PL': 'Polska', 'DE': 'Niemcy', 'FR': 'Francja'}. Stwórz nowy
słownik, używając Dictionary Comprehension, który zamieni klucze z wartościami.
Oczekiwany wynik: Słownik, gdzie kluczami są nazwy krajów, a wartościami kody.
Wymagana technika: Tylko Dictionary Comprehension.
"""

def main():
    kody = {'PL': 'Polska', 'DE': 'Niemcy', 'FR': 'Francja'}

    rever = {y: x for x,y in kody.items()}

    print(rever)

if __name__ == '__main__':
    main()