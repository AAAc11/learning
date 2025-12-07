"""
Utwórz funkcję tworz_konfiguracje(**kwargs),
która przyjmuje dowolną liczbę argumentów słownikowych (**kwargs).
• Wewnątrz funkcji: zbierz wszystkie wartości z **kwargs w list.
• Następnie, utwórz frozenset z tej listy, aby uzyskać unikalne, niezmienne wartości konfiguracyjne.
• Dodatkowo, utwórz drugą funkcję przypisz_tagi(*args, **kwargs), która przyjmie *args jako tagi
i zwróci nowy słownik, łączący tagi z *args (jako frozenset dla unikalności) z kluczami z **kwargs.
"""

def make_configuration(**kwargs):
    values = list(kwargs.values())
    values = frozenset(values)
    return values

def assign_tags(*args, **kwargs):
    tags = frozenset(args)
    dict_tag = {}
    dict_tag['tags'] = tags
    dict_tag.update(kwargs)
    return dict_tag

def main():
    print(make_configuration(imie = 'Anna', nazwisko = 'Cygan', imie2 = "Anna"))

    print(assign_tags(
        "backend", "python", "serwer", "python", "django",
        nazwa_projektu="API_Gateway",
        wersja="1.5",
        status="W_PRODUKCJI"
    ))

if __name__ == '__main__':
    main()