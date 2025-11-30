"""
Polecenie:
Napisz funkcję 'combine_lists', która przyjmuje dwie listy łańcuchów znaków i zwraca jedną nową listę
będącą ich połączeniem. Użyj typing.List
"""
from typing import List

def combine_lists(l1: List[str], l2: List[str]) -> List[str]:
    return l1+l2

def main():
    s1 = ["Green"]
    s2 = ["Grass"]
    print(combine_lists(s1 , s2))

if __name__ == '__main__':
    main()

