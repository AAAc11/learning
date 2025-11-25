"""
Polecenie:
Utwórz klasę User z atrybutami name i age oraz metodą is_adult.
"""

class User:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def is_adult(self):
        return True if self.age >= 18 else False


def main():
    u1 = User("Andrzej", 20)
    print(f"Is {u1.name} an adult? {u1.is_adult()}")

if __name__ == '__main__':
    main()