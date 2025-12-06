"""
Wczytaj plik prices.csv. Używając modułu csv i List Comprehension, utwórz listę zawierającą same ceny
produktów jako liczby zmiennoprzecinkowe (float). Pamiętaj o pominięciu nagłówka.
Wymagana technika: CSV Reader, List Comprehension, konwersja typu.
"""
import csv

with open('prices.csv', 'r', encoding='utf-8') as f:
    context = csv.reader(f)
    next(context)

    prices = [float(x[1]) for x in context]

    print(prices)