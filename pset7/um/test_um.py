from um import count

from pytest import raises

def test_valid_um():
    assert count("hello, um, world") == 1
    assert count("um, hello, um, world") == 2
    assert count("um...") == 1
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_invalid_um():
    assert count("yum") == 0
    assert count("mum") == 0
    assert count("uumm") == 0
    assert count(" umm") == 0