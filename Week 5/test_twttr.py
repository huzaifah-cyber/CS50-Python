from twttr import shorten
import pytest

def test_string_shorten():
    assert shorten("hello") == "hll"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("CS50") == "CS50"


def test_punctuation_shorten():
    assert shorten(".,?!") == ".,?!"

def test_numbers_shorten():
    assert shorten("50") == "50"

def test_type_shorten():
    with pytest.raises(TypeError):
        shorten(123)
