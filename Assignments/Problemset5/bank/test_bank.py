from bank import value
import pytest

def test_value_str():
    assert value("hello") == "$0"
    assert value("hi") == "$20"
    assert value("baby") == "$100"
    assert value("dolls") == "$100"

def test_value_num():
    with pytest.raises(AttributeError):
        value(50)
        value(0)