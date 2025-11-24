from functools import wraps


def type_checker(function):
    @wraps(function)
    def inner_wrapper(n):
        if not isinstance(n, int):
            raise TypeError
        return function(n)

    return inner_wrapper


@type_checker
def increase_by_one(number):
    return number+1


print(increase_by_one(10))
print(increase_by_one("A"))