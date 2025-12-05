"""
Napisz funkcję przetwarzaj_dane(lista).
W bloku try spróbuj uzyskać dostęp do elementu o indeksie 10 (np. lista[10]).
W bloku except IndexError:
Wydrukuj: "Wewnętrzny błąd: indeks poza zakresem. Logowanie zdarzenia...".
Użyj samej instrukcji raise (bez argumentów) w celu ponownego zgłoszenia (re-raise) złapanego
wyjątku do wyższej warstwy. Wywołaj funkcję dla listy np. [1, 2, 3] i otocz to wywołanie
zewnętrznym blokiem try...except, aby złapać ponownie zgłoszony IndexError i wydrukować "Błąd
krytyczny: aplikacja zakończona."
"""

def process_data(lis):
    try:
        element = lis[10]
    except IndexError:
        print("Internal error. Index out of bounds.")
        raise 

def main():
    try:
        process_data([1,2,3,4,5,6,7,8])
    except IndexError:
        print("Fatal error")

if __name__ == '__main__':
    main()