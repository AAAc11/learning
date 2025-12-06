"""
Zainicjuj listę nazwisk: workers = ['Kowalski', 'Nowak', 'Zieliński'].
Użyj List Comprehension, aby przekształcić tę listę w listę słowników, gdzie każdy słownik ma
klucze ID i Nazwisko. (ID powinno być numerem porządkowym, np. 1, 2, 3).
Zapisz wynikową listę słowników do nowego pliku CSV pracownicy.csv za pomocą csv.DictWriter.
Wymagana technika: List Comprehension z enumerate, CSV DictWriter.
"""
import csv

workers = ['Kowalski', 'Nowak', 'Zieliński']
list_workers = [
    {"ID": x, "Surname": y} for x,y in enumerate(workers,1)]
print(list_workers)

with open('workers.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["ID", "Surname"])
    writer.writeheader()
    writer.writerows(list_workers)
