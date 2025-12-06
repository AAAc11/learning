"""
Utwórz plik settings.json z kluczem "max_workers" o wartości 5.
Napisz program, który wczyta ten plik za pomocą json.load().
Zmień wartość klucza "max_workers" na 10.
Zapisz zmodyfikowany słownik z powrotem do pliku.
Wymagana technika: Tylko moduł json (load i dump).
"""
import json

def main():
    with open('settings.json', 'r+', encoding='utf-8') as reading_file:
        context = json.load(reading_file)
    context["max_workers"] = 10
    with open('settings.json', 'r+', encoding='utf-8') as saving_file:
        json.dump(context, saving_file, indent=4,ensure_ascii=False)
    print(context)

if __name__ == '__main__':
    main()