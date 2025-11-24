from functools import wraps


def greet(func):
    @wraps(func)
    def wrapper(n):
        print("Starting the operation...")
        return func(n)
    return wrapper

@greet
def greeting(name):
    print(f"Hello {name}!")

greeting("anna")

