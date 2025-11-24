from functools import wraps


def ending(function):
    @wraps(function)
    def inner(n):
        result = function(n)
        print("Closing the program...")
        return result
    return inner

@ending
def goodbye(name):
    print(f"Goodbye {name}!")

goodbye("anna")