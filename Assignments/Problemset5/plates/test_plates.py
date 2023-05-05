import pytest
from plates import is_valid

def test_condition1():
    assert is_valid("AB1234") == True
    assert is_valid("ABC") == True
    assert is_valid("1234AB") == False
    assert is_valid("1234AB") == False


def test_condition2():
    assert is_valid("ABCDEF") == True
    assert is_valid("AB") == True
    assert is_valid("ABCDEFG1234") == False
    assert is_valid("ABCDEF123") == False

def test_condition3a():
    assert is_valid("ABCD123E") == False
    assert is_valid("ABC1234D") == False
    assert is_valid("ABCD123") == False
    assert is_valid("ABCDE1234") == False


def test_condition3b():
    assert is_valid("0AB1234") == False
    assert is_valid("AB12345") == False
    assert is_valid("AB1234C") == False
    assert is_valid("A1234B") == False


def test_condition4():
    assert is_valid("AB1234") == True
    assert is_valid("AB-1234") == False
    assert is_valid("AB_1234") == False
    assert is_valid("AB@1234") == False
