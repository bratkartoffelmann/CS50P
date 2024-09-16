from pytest import raises
from fuel import convert, gauge


def test_valid_fractions():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0


def test_invalid_fractions():
    with raises(ValueError):
        convert("/")
    with raises(ValueError):
        convert("1")
    with raises(ValueError):
        convert("1/")
    with raises(ValueError):
        convert("/4")
    with raises(ValueError):
        convert("cat/dog")
    with raises(ValueError):
        convert("1.5/3")

    with raises(ZeroDivisionError):
        convert("4/0")
    with raises(ValueError):
        convert("5/4")

def test_guage():
    # Full guage
    assert gauge(percentage=100) == "F"
    assert gauge(percentage=99) == "F"
    assert gauge(percentage=98.99) != "F"

    # Empty guage
    assert gauge(percentage=0) == "E"
    assert gauge(percentage=1) == "E"
    assert gauge(percentage=1.01) != "E"

    # Others
    assert gauge(percentage=25) == "25%"
    assert gauge(percentage=50) == "50%"
    assert gauge(percentage=75) == "75%"
