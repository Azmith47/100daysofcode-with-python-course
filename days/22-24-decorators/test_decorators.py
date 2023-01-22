from decorators import make_html
import pytest


@pytest.mark.parametrize(
    "arg, elem1, elem2, ret",
    [
        (
            "Hello Christian",
            "h1",
            "strong",
            "<h1><strong>Hello Christian</strong></h1>",
        ),
        ("how do you do?", "li", "p", "<li><p>how do you do?</p></li>"),
        (
            "whats happening Harry",
            "p",
            "strong",
            "<p><strong>whats happening Harry</strong></p>",
        ),
        (None, "p", "strong", "<p><strong>I code with PyBites</strong></p>"),
    ],
)
def test_make_html(arg, elem1, elem2, ret):
    @make_html(elem1)
    @make_html(elem2)
    def get_text(text="I code with PyBites"):
        """Returns text"""
        return text

    if arg != None:
        assert get_text(arg) == ret
    else:
        assert get_text() == ret
