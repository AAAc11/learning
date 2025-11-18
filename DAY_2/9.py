def sprawdz_ustawienia(dozwolone_klucze,**ustawienia_uzytkownika):
    for klucz in ustawienia_uzytkownika.values():
        if klucz not in dozwolone_klucze:
            return False
    return True

print(sprawdz_ustawienia(dozwolone_klucze=["zegar","zmiana strefy","zmiana hasla"],zmiana="zegar",zmiana2="zmiana hasla",zmiana3="usuniecie konta"))