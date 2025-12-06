"""
Wczytaj cały plik persons.csv za pomocą csv.reader i wydrukuj każdy wiersz w formacie: [Imię] ma [Wiek] lat..
Wymagana technika: Tylko moduł csv i prosta pętla for. Pomiń nagłówek.
"""
import csv

with open("persons.csv", 'r', encoding='utf-8') as f:
    context = csv.reader(f)
    next(context)
    for person in context:
        print(f"{person[0]} is {person[1]} years old and lives in {person[2]}")

