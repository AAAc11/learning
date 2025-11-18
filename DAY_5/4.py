def pobierz_wartosc(slownik, klucz):
    try:
        return slownik[klucz]

    except KeyError:
        print("klucz nie istnieje!")

slownik={"imie": "jan", "wiek": 30}
print(pobierz_wartosc(slownik,"wiek"))
print(pobierz_wartosc(slownik,"nazwisko"))
