"""
Masz listę imion. Użyj map i funkcji lambda, aby dodać prefiks "Pan/Pani " do każdego imienia.
"""

imiona = ["Kowalski", "Nowak", "Zielińska"]

adding_prefix = lambda x: ("Pan/Pani " + x)
names_with_prefix = list(map(adding_prefix, imiona))

print(names_with_prefix)