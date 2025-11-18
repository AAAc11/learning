def formatuj_profil(**dane_profilu):
    result=""
    result=result.join((f"\n{x}: {y}") for x,y in dane_profilu.items())

    return result

print(formatuj_profil(imie="Jan", wiek=40, hobby="szachy"))