try:
    warunek=True
    while warunek:
        liczba=int(input("Podaj liczbe calkowita: "))
        warunek=False
    print(f"towja liczba: {liczba}")
except ValueError:
    print("to nei jest liczba")
