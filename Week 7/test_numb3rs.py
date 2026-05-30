from numb3rs import validate


def test_true_validate():
    assert validate("2.2.2.2") == True
    assert validate("255.44.223.233") == True
    assert validate("0.0.0.0") == True

def test_false_validate():
    assert validate("2.2.2.-32") == False
    assert validate("0.0.0.02") == False
    assert validate("255.44.273.233") == False
