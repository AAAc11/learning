"""
Utwórz funkcję weryfikuj_dane(wymagane_klucze, *args, **kwargs).
• wymagane_klucze to obiekt frozenset zawierający nazwy kluczy, które muszą znaleźć się w **kwargs.
• Funkcja powinna najpierw sprawdzić, czy wszystkie klucze z wymagane_klucze są obecne w **kwargs.
Jeśli nie, niech zwróci odpowiedni komunikat.
• Następnie, jeśli przekazano *args, niech zwróci frozenset będący różnicą (ang. difference) między
zbiorem *args (po przekształceniu na frozenset) a zbiorem wymagane_klucze.
"""

def verify_data(required_keys, *args, **kwargs):
    kwargs_keys = set(kwargs.keys())

    if not kwargs_keys.issuperset(required_keys):
        return f"Missing required key: {required_keys.difference(kwargs_keys)}"

    if args:
        set_args = frozenset(args)
        difference = set_args.difference(required_keys)
        return frozenset(difference)
    return "All required keys are contained"

def main():

    keys = frozenset({'name', 'surname', 'age'})

    print(verify_data(keys, 'Anna', 20, name = 'Anna', age = '20'))
    print()
    print(verify_data(keys, 'Anna', 20, name='Anna', age='20', surname = 'Kowalski'))
    print()
    print(verify_data(keys, name='Anna', age='20', surname = 'Kowalski'))

if __name__ == '__main__':
    main()