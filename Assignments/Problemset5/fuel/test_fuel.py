from Fuel import convert
from Fuel import gauge
import pytest

def test_convert():
    assert convert("2/4") == "50.00%"
    assert convert("1/8") == "12.50%"
    assert convert("9/9") == "F"
    assert convert("5/7") == "71.43%"

def test_gauge():
    assert gauge(0.5) == "E"
    assert gauge(1) == "1.00%"
    assert gauge(50) == "50.00%"
    assert gauge(100) == "F"
    assert gauge(101) == "F"
