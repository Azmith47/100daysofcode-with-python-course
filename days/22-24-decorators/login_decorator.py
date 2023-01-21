from functools import wraps

known_users = ["bob", "julian", "mike", "carmen", "sue"]
loggedin_users = ["mike", "sue"]


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg not in known_users:
                return "please create an account"
            elif arg not in loggedin_users:
                return "please login"
            else:
                return func(*args, **kwargs)

    return wrapper


@login_required
def welcome(user):
    """Return a welcome message if logged in"""
    return f"welcome back {user}"


print(welcome("bob"))

print(welcome("mike"))

print(welcome("tory"))
