from pytest import raises

from jar import Jar

def test_init():
    jar = Jar(50)
    assert jar.capacity == 50

    with raises(ValueError):
        Jar("1")
    with raises(ValueError):
        Jar(-10)

def test_deposit():
    jar = Jar()

    # deposit
    jar.deposit(10)
    assert jar.size == 10

    # exceed capacity
    with raises(ValueError):
        jar.deposit(10)

def test_withdraw():
    jar = Jar()
    jar.deposit(10)

    # withdraw
    jar.withdraw(2)
    assert jar.size == 8

    # exceed capacity
    with raises(ValueError):
        jar.withdraw(10)

def test_str():
    jar = Jar()
    assert jar.__str__() == "🍪"*0

    jar.deposit(10)
    assert jar.__str__() == "🍪"*10

    jar.withdraw(5)
    assert jar.__str__() == "🍪"*5