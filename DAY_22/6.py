"""
Wczytaj plik stock.json. Używając Dictionary Comprehension, stwórz nowy słownik, który będzie zawierał tylko
te klucze (symbole akcji), których wartość (cena) jest niższa niż 150.
Wymagana technika: JSON Load, Dictionary Comprehension z warunkiem.
"""
import json

with open('stock.json', 'r', encoding='utf-8') as f:
    context = json.load(f)

    lower_than_150 = {x for x, y in context.items() if y < 150}

    print(lower_than_150)