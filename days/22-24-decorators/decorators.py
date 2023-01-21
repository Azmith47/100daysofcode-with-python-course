from functools import wraps


def make_html(element):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            response = func(*args, **kwargs)

            return f"<{element}>{response}</{element}>"

        return wrapper

    return inner
