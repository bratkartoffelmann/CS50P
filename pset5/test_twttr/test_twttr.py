from twttr import shorten

from pytest import raises

def test_empty():
    assert shorten("") == ""

def test_words():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
    assert shorten("Apple") == "ppl"

def test_incorrect():
    with raises(TypeError):
        shorten(0)

    with raises(TypeError):
        shorten()

    with raises(TypeError):
        shorten(None)