import datetime
import time
from typing import NoReturn


def log_action(message: str) -> NoReturn:
    try:
        with open("logs.txt","a",encoding='utf-8') as f:
            now = datetime.datetime.now()
            f.write(f"[{now}] {message}\n")
    except IOError:
        print("Cannot save in logs.txt")