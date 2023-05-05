from twttr import shorten
import pytest

def test_shorten_str():
    assert shorten("Hello") == "hll"
    assert shorten("Monil") == "mnl"
    assert shorten("Cs50") == "cs50"

def test_shorten_num():
    with pytest.raises(TypeError):
        shorten(50)
        shorten(10)
