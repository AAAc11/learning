"""
Polecenie:
Zaimportuj moduł logging.
Użyj logging.basicConfig(level=logging.DEBUG) na samym początku skryptu,
aby skonfigurować logger do wyświetlania wszystkiego.
Zaloguj po jednej wiadomości na każdym poziomie: debug(), info(), warning(), error(), critical().
Zmień poziom konfiguracji na level=logging.INFO i zobacz, które wiadomości znikną.
"""
import logging
import sys

# Ustawienie formatu logów, aby lepiej wizualizować, kiedy następuje zmiana konfiguracji
log_format = '%(levelname)s: %(message)s'

# --- Pierwsza Konfiguracja: Poziom DEBUG ---
print("--- Konfiguracja: logging.DEBUG (Wszystkie wiadomości powinny być widoczne) ---")

# Konfiguracja loggera, aby wyświetlał wiadomości na poziomie DEBUG i wyższych.
# Używamy formatu i ustawiamy, aby logi były kierowane na standardowe wyjście błędów (stderr),
# co jest domyślnym zachowaniem basicConfig.
logging.basicConfig(level=logging.DEBUG, format=log_format, stream=sys.stdout)

# Logowanie wiadomości na każdym poziomie
logging.debug("Wiadomość DEBUG - Ta powinna być widoczna przy level=DEBUG.")
logging.info("Wiadomość INFO - Ta powinna być widoczna przy level=DEBUG.")
logging.warning("Wiadomość WARNING - Ta powinna być widoczna przy level=DEBUG.")
logging.error("Wiadomość ERROR - Ta powinna być widoczna przy level=DEBUG.")
logging.critical("Wiadomość CRITICAL - Ta powinna być widoczna przy level=DEBUG.")

# Resetowanie konfiguracji basicConfig
# Musimy zresetować konfigurację, aby basicConfig mogło zadziałać ponownie.
# W rzeczywistych aplikacjach basicConfig wywołuje się tylko raz.
# Robimy to tutaj wyłącznie w celach demonstracyjnych.
logging.shutdown()
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

print("\n--- Konfiguracja: logging.INFO (Wiadomości DEBUG i INFO powinny być widoczne) ---")
# Zauważ, że standardowo wiadomość na poziomie INFO jest wyświetlana,
# ale wiadomość DEBUG już nie, gdy poziom jest ustawiony na INFO.
# EDIT: Zgodnie z poleceniem, zmieńmy poziom na INFO i zobaczmy co się stanie.
# Używamy nowej konfiguracji, aby pokazać, które wiadomości znikną.

# --- Druga Konfiguracja: Poziom INFO ---
# Konfiguracja loggera, aby wyświetlał wiadomości na poziomie INFO i wyższych.
logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

# Logowanie tych samych wiadomości na każdym poziomie
logging.debug("Wiadomość DEBUG - Ta powinna ZNIKNĄĆ przy level=INFO.")
logging.info("Wiadomość INFO - Ta powinna być WIDOCZNA przy level=INFO.")
logging.warning("Wiadomość WARNING - Ta powinna być WIDOCZNA przy level=INFO.")
logging.error("Wiadomość ERROR - Ta powinna być WIDOCZNA przy level=INFO.")
logging.critical("Wiadomość CRITICAL - Ta powinna być WIDOCZNA przy level=INFO.")