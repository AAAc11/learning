"""
Polecenie:
Zdefiniuj funkcję lambda, która przyjmuje imię
i nazwisko jako osobne argumenty, a zwraca
je połączone w jeden string.
"""

name = input("Enter your name: ")
surname = input("Enter your surname: ")\

combined = lambda n, s: f"{n} {s}"

print(combined(name,surname))