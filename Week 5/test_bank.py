from bank import value


def test_string_value():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO how are you") == 0
    assert value("TWITTER") == 100
    assert value("CS50") == 100


def test_punctuation_value():
    assert value(".,?!") == 100

def test_numbers_value():
    assert value("50") == 100

