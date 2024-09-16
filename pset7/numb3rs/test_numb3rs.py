from numb3rs import validate

def test_valid_ip():
    assert validate("1.2.3.4") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.0") == True


def test_invalid_ip():
    # Invalid string
    assert validate("1.2") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3.4.") == False
    assert validate("1,2,3,4") == False
    assert validate("cat") == False

    # Invalid byte
    assert validate("260.0.0.0") == False
    assert validate("0.260.0.0") == False
    assert validate("0.0.260.0") == False
    assert validate("0.0.0.260") == False
