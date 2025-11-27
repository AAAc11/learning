"""
Polecenie:
Stwórz klasę Employee z prywatnymi polami __salary.
Dodaj getter i setter.
Zaimplementuj walidację wynagrodzenia.
"""

class Employee:
    def __init__(self, name, __salary):
        self.name = name
        self.setSalary(__salary)

    def getSalary(self):
        return self.__salary

    def setSalary(self,s):
        self.__salary = s

    def __str__(self):
        return f"{self.name} earns {self.__salary}"

def main():
    emp1 =Employee("Andrzej", 5000)
    print(emp1)
    emp1.setSalary(6000)
    print(emp1)

if __name__ == '__main__':
    main()