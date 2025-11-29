"""
Polecenie:
Napisz prostą funkcję, np. oblicz_sume(a, b), która zwraca sumę a + b.
Wewnątrz tej funkcji dodaj linię logującą (np. logging.info(f"Otrzymano argumenty: {a} i {b}")).
Dodaj linię logującą (np. logging.debug(f"Wynik sumowania: {a+b}")).
Wywołaj funkcję kilka razy i zobacz, jak logi z kontekstem funkcji pojawiają się w pliku.
"""
import logging

file_name = "sum.log"
log_format = ('%(asctime)s - %(levelname)s - %(module)s.%(funcName)s: %(message)s')
logging.basicConfig(
    filename=file_name,
    level=logging.DEBUG,
    format=log_format,
    filemode='w'
)

def cal_sum(a, b):
    logging.info(f"Received: {a} and {b}")
    logging.debug(f"Sum result: {a+b}")
    return a+b

def main():
    print("(7+5): ", end='')
    print(cal_sum(7,5))

    print("(11+4): ", end='')
    print(cal_sum(11, 4))

    print("(90+15): ", end='')
    print(cal_sum(90, 15))



if __name__ == '__main__':
    main()