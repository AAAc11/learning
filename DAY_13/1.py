"""
Polecenie:
Utwórz klasę bazową Animal oraz klasy Dog i Cat dziedziczące po niej.
Stwórz metodę make_sound. Zbuduj listę zwierząt i wywołaj tę samą metodę dla każdego (polimorfizm).
Zmień klasę Animal, tak aby wymuszała implementację metody make_sound w każdej klasie pochodnej.
"""
from abc import abstractmethod


class Animal:
    """Klasa bazowa"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass #wymusza implementację w klasach potomnych


class Dog(Animal):
    def __init__(self,name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        return f"{self.name} szczeka."

class Cat(Animal):
    def __init__(self,name,age,fur_color):
        super().__init__(name,age)
        self.fur_color = fur_color

    def make_sound(self):
        return f"{self.name} miauczy."

def main():
    pies = Dog("Reksio", 3, "cocker spaniel")
    kot = Cat("Lola", 4, "black")

    print(pies.make_sound())
    print(kot.make_sound())

if __name__ == '__main__':
    main()