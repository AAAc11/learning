"""
Polecenie:
Stwórz klasę Book z dataclass.
Dodaj __str__ i porównywanie dwóch obiektów.
Użyj frozen=True.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Book:
    title: str
    author: str
    year_of_publishing: int

    def __str__(self):
        return f"{self.title} - {self.author}, year of publishing: {self.year_of_publishing}"

def main():
    b1 = Book("Harry Potter and the philosopher's stone", "J.K. Rowling", 1997)
    b2=Book("Harry Potter and the Chamber of Secrets", "J.K. Rowling", 1998)

    print(f"Book 1: {b1}") #__repr__
    print(f"Book 2: {str(b2)}") #__str__

    print(f"\nbook 1 == book 2: {b1 == b2}")

if __name__ == '__main__':
    main()