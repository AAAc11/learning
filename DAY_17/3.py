"""
Polecenie:
Napisz funkcję 'check_price', która przyjmuje opcjonalną cenę (float lub None). Jeśli
cena jest podana, zwraca True, jeśli jest wyższa niż 100.0, w przeciwnym razie
zwraca False. Dodaj odpowiednie podpowiedzi typów (Optional).
"""
from typing import Optional

def check_price(price: Optional[float]) -> bool:
    if price is None:
        return False
    return price > 100.0

def main():
    print(check_price(140.4))
    print(check_price(None))
    print(check_price(60.7))

if __name__ == '__main__':
    main()
