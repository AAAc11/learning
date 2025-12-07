"""
Utwórz funkcję format_text(tekst, *args, **kwargs). Funkcja powinna zawsze przyjmować jeden
argument pozycyjny tekst. Następnie:
• Jeśli podano *args, użyj pierwszego elementu jako prefiksu i drugiego jako sufiksu dla tekstu.
• Jeśli podano **kwargs, sprawdź, czy zawiera klucz WIELKIMI o wartości True. Jeśli tak,
przekształć cały tekst na wielkie litery.
"""

def format_text(text, *args, **kwargs):
    if len(args) > 1:
        text = args[0] + text + args[1]

    for key, value in kwargs.items():
        if key == "WIELKIMI" and value == True:
            text = text.upper()

    return text

def main():
    print(format_text("pink pony club", "our ", " exists", MALYMI = False,WIELKIMI =  True))

if __name__ == '__main__':
    main()