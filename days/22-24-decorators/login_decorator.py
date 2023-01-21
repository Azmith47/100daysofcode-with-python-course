from functools import wraps

known_users = ["bob", "julian", "mike", "carmen", "sue"]
loggedin_users = ["mike", "sue"]


def login_required():
    @wraps(func)
    def wrapper(*args, **kwargs):
        pass


@login_required
def welcome(user):
    """Return a welcome message if logged in"""
    return f"welcome back {user}"
