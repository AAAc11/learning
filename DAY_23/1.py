"""
Utwórz funkcję sum_count(*args), która przyjmuje dowolną liczbę argumentów pozycyjnych (*args),
sumuje je i zwraca tę sumę. Następnie, stwórz funkcję print_report(**kwargs), która przyjmuje dowolną
liczbę argumentów słownikowych (**kwargs) i drukuje każdy z nich w formacie: klucz: wartość.
"""

def sum_count(*args):
    return sum(args)

def print_report(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def main():
    print(sum_count(4, 5, 1, 7))
    print_report(color = "green", emotion = "happy", item = "pencil")


if __name__ == '__main__':
    main()

