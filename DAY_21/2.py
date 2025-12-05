"""
Zdefiniuj niestandardowy wyjątek BłądAutoryzacji, który w konstruktorze
__init__ przyjmuje i przechowuje dodatkowy argument: kod_bledu (liczba całkowita).
Zdefiniuj funkcję sprawdz_uprawnienia(rola), która:
Jeśli rola to 'admin', zwraca True. Jeśli rola to 'użytkownik', zgłasza
BłądAutoryzacji z kodem błędu 403. Jeśli rola to 'gość', zgłasza BłądAutoryzacji
z kodem błędu 401. Użyj bloku try...except do wywołania funkcji dla roli 'użytkownik'.
W bloku except, poza wydrukowaniem komunikatu, wydrukuj również przechwycony kod_bledu wyjątku.
"""

class AuthorizationError(Exception):
    def __init__(self, error_code):
        self.error_code = error_code

def check_permissions(role):
    try:
        if role.lower() == "admin":
            return True
        if role.lower() == "user":
            raise AuthorizationError(403)
        if role.lower() == "guest":
            raise AuthorizationError(401)
    except AuthorizationError as e:
        print(f"Authorization failed. Code {e.error_code}")

def main():
    print(check_permissions("admin"))
    print(check_permissions("user"))
    print(check_permissions("Guest"))

if __name__ == '__main__':
    main()