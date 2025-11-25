produkty = [
    {"id": 1, "nazwa": "Laptop", "kategoria": "elektronika", "cena": 3500},
    {"id": 2, "nazwa": "Myszka", "kategoria": "akcesoria", "cena": 150},
    {"id": 3, "nazwa": "Książka OOP", "kategoria": "książki", "cena": 80},
    {"id": 4, "nazwa": "Klawiatura", "kategoria": "akcesoria", "cena": 250}
]

names={x["nazwa"] for x in produkty if x["kategoria"]=="akcesoria"}

print(names)