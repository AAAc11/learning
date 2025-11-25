"""
Polecenie:
Utwórz klasę Product z atrybutami name i price oraz metodą apply_discount.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        self.price = round(self.price * ((100 - percent) / 100),2)

    def __str__(self):
        return f"{self.name} with price {self.price}"

def main():
    p1 = Product("beef", 29.99)
    p1.apply_discount(15)
    print(p1)

if __name__ == '__main__':
    main()