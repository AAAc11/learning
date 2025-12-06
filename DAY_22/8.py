"""
JSON + Nested List Comprehension (Spłaszczanie i Przekształcanie)
Wczytaj plik categories.json. Każdy element na liście zawiera słownik z kluczem items, który jest
listą. Użyj jednej zagnieżdżonej List Comprehension, aby utworzyć pojedynczą, spłaszczoną listę
zawierającą tylko nazwy wszystkich produktów (name) ze wszystkich kategorii.
Wymagana technika: JSON Load, Zagnieżdżona List Comprehension.
"""
import json


with open('categories.json', 'r', encoding='utf-8') as f:
    context = json.load(f)

    all_names = [item['name'] for d in context for item in d['items']]
    print(all_names)