from pytest import raises

from plates import is_valid

def test_min2_max6():
    assert is_valid("HELLO") == True
    assert is_valid("CS50") == True
    assert is_valid("HI") == True
    assert is_valid("ABCDEF") == True

    assert is_valid("HELLO, WORLD") == False
    assert is_valid("GOODBYE") == False
    assert is_valid("H") == False
    # assert is_valid() == False


def test_start_2_letters():
    assert is_valid("HI") == True
    assert is_valid("HEY") == True

    assert is_valid("012345") == False
    assert is_valid("H1") == False


def test_fail_non_alphanumeric():
    assert is_valid("PI3.14") == False


def test_num_not_middle():
    assert is_valid("CSP50") == True

    assert is_valid("CS50P") == False

def test_num_start_not_0():
    assert is_valid("CS05") == False