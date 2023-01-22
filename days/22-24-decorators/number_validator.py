from functools import wraps


def valid_positive_numbers(func):
    wraps(func)

    def wrapper(*args, **kwargs):
        for arg in args:
            if type(arg) != type(0):
                return TypeError
            elif arg < 0:
                return ValueError
        return func(*args, **kwargs)

    return wrapper


@valid_positive_numbers
def add(a, b):
    res = a + b
    return res


print(add(5, 5))
