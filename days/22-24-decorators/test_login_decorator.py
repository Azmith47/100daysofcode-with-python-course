from login_decorator import login_required

import pytest


@pytest.mark.parametrize(
    "arg, ret",
    [
        ("bob", "please login"),
        ("tory", "please create an account"),
        ("mike", "welcome back mike"),
        ("sue", "welcome back sue"),
    ],
)
def test_login_required(arg, ret):
    @login_required
    def welcome(user):
        """Return a welcome message if logged in"""
        return f"welcome back {user}"

    assert welcome(arg) == ret
