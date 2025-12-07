"""
Utwórz dwa obiekty frozenset: wzorce_a z elementami (1, 2, 3, 4)
i wzorce_b z elementami (3, 4, 5, 6). Następnie:
• Znajdź i wydrukuj część wspólną (ang. intersection) obu zbiorów.
• Sprawdź i wydrukuj, czy wzorce_a jest nadzbiorem (ang. superset) zbioru (1, 2).
"""

def main():
    pattern_a = {1, 2, 3, 4}
    frozenset(pattern_a)
    pattern_b = {3, 4, 5, 6}
    frozenset(pattern_b)


    common_part = pattern_a & pattern_b
    print(f"Common part: {common_part}")

    is_superset = pattern_a.issuperset({1, 2})
    print(f"Is superset? {is_superset}")

if __name__ == '__main__':
    main()
