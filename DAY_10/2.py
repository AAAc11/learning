"""
Polecenie:
Generator czytający plik linia po linii.
"""

def function(file):
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            yield line

for l in function("teoria.txt"):
    print(l)