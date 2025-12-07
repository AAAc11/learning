"""
Utwórz słownik o nazwie access_levels, w którym kluczami będą obiekty
frozenset, a wartościami będą opisy. Kluczami niech będą np.:
• frozenset({'Admin', 'Dev'}) z wartością "Pełny dostęp techniczny"
• frozenset({'User'}) z wartością "Ograniczony dostęp"
Następnie:
• Spróbuj odwołać się do opisu, używając klucza frozenset({'User'}).
• Spróbuj dodać nowy klucz do zwykłego zbioru (set) – np. set({'Admin', 'Dev'}) – i zaobserwuj,
dlaczego to się nie uda. (Pamiętaj: standardowy set nie może być kluczem w słowniku).
"""

def main():
    access_levels = {frozenset({'Admin', 'Dev'}): "Full access", frozenset({'User'}): "Limited access"}

    print(access_levels.get(frozenset({'User'})))
    access_levels.pop(set({'Admin', 'Dev'}))

    #kluczem musi byc typ niezmienny, ponieważ musi być możliwe poprawne haszowanie


if __name__ == '__main__':
    main()

