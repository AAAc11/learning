def przeczytaj_funkcje(sciezka_do_pliku):
    try:
        plik=None
        plik= open(sciezka_do_pliku, "r", encoding="utf-8")
        zawartosc=plik.read()
    except FileNotFoundError:
        print("nie ma takiego pliky")
    except PermissionError:
        print("nie masz dostepu do tegon pliku")
    except Exception as e:
        print(f"Blad: {e}")
    else:
        print(zawartosc)
    finally:
        print("zakonczono probe odczytu plike!")

with open("test.txt","w",encoding="utf-8") as f:
    f.write("TESCIK")

przeczytaj_funkcje("test.txt")
przeczytaj_funkcje("niesidnr.txt")
