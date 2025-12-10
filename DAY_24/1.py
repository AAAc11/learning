"""
Masz listę tupli, gdzie każda tupla reprezentuje osobę: (imię, wiek). Użyj funkcji lambda
jako klucza (key) w funkcji sorted(), aby posortować listę według wieku.
"""

osoby = [("Anna", 30), ("Krzysztof", 25), ("Ewa", 35), ("Tomasz", 20)]

sorted_by_age = sorted(osoby, key=lambda osoba: osoba[1])
print(sorted_by_age)
