"""
Polecenie:
Napisz serię funkcji do zarządzania i analizowania listy użytkowników.
"""

from itertools import count
from collections import Counter

users_data = [
    {"name": "Ania", "age": 25, "city": "Kraków"},
    {"name": "Bartek", "age": 32, "city": "Warszawa"},
    {"name": "Celina", "age": 17, "city": "Gdańsk"},
    {"name": "Dawid", "age": 45, "city": "Kraków"},
    {"name": "Ewa", "age": 25, "city": "Warszawa"},
    {"name": "Filip", "age": -5, "city": "Poznań"}, # Błędny wiek
    {"name": "Gosia", "age": 25, "city": "Wrocław"},
]

class InvalidAgeError(Exception):
    pass

def validate_user(user: dict) -> bool:
    if user.get("age",0) < 0:
        raise InvalidAgeError(f"Age {user['age']} is not correct!")
    return True

def analyze_users(users_list: list) -> tuple[list, dict]:
    names = []
    all_cities = []
    for user in users_list:
        try:
            validate_user(user)
            names.append(user["name"])
            all_cities.append(user["city"])


        except InvalidAgeError as e:
            print(f"Error: {e}")
    city_counts = dict(Counter(all_cities))

    return names, city_counts

def main():
    names_list, city_count_dict = analyze_users(users_data)

    print(f"List of names: {names_list}")
    print(f"Dict of cities: {city_count_dict}")

if __name__ == '__main__':
    main()

