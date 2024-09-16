from pytest import raises
from datetime import date

from seasons import get_date, get_timedelta_minutes_string

def test_date():
    assert get_date("1999-01-01") == date(1999, 1, 1)
    assert get_date("1999-12-31") == date(1999, 12, 31)

    with raises(ValueError):
        get_date("January 1, 1999")
    with raises(ValueError):
        get_date("1999-02-31")
    with raises(ValueError):
        get_date("1999-13-31")

def test_str_normal1():
    date1 = date(2019, 1, 1)
    date2 = date(2020, 1, 1)

    assert get_timedelta_minutes_string(date1, date2) == "Five hundred twenty-five thousand, six hundred minutes"

def test_str_leap1():
    date1 = date(2020, 1, 1)
    date2 = date(2021, 1, 1)

    assert get_timedelta_minutes_string(date1, date2) == "Five hundred twenty-seven thousand forty minutes"

def test_str_normal2():
    date1 = date(2018, 1, 1)
    date2 = date(2020, 1, 1)

    assert get_timedelta_minutes_string(date1, date2) == "One million, fifty-one thousand, two hundred minutes"

def test_str_leap2():
    date1 = date(2020, 1, 1)
    date2 = date(2022, 1, 1)

    assert get_timedelta_minutes_string(date1, date2) == "One million, fifty-two thousand, six hundred forty minutes"