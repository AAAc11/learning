"""
Polecenie:
Utwórz klasę BankAccount z metodami deposit oraz withdraw.
"""

class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def deposit(self, sum):
        self.amount += sum

    def withdraw(self, sum):
        if self.amount >= sum:
            self.amount -= sum
        else:
            raise ValueError("Not enough money!")

    def __str__(self):
        return f"{self.name} has {self.amount} in the account."

def main():
    u1 = BankAccount("Steve", 200)
    print(u1)
    u1.deposit(40)
    print(u1)
    u1.withdraw(130)
    print(u1)

if __name__ == '__main__':
    main()