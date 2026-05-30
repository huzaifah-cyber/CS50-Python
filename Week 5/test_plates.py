from plates import is_valid

def test_first_2_char_is_valid():
    assert is_valid("12abcd") == False
    assert is_valid("31455") == False
    assert is_valid("22") == False

def test_length_is_valid():
    assert is_valid("ABcs500000") == False
    assert is_valid("") == False
    assert is_valid("1234567") == False
    assert is_valid("123456789") == False


def test_number_before_char_is_valid():
    assert is_valid("ab1de") == False
    assert is_valid("ABC3EF") == False

def test_invalid_ch_is_valid():
    assert is_valid("abcde;") == False
    assert is_valid("ab*&e;") == False

def test_zero_before_number_is_valid():
    assert is_valid("AA0635") == False
    assert is_valid("aa063") == False

def test_valid_inputs_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("abcd12") == True
    assert is_valid("ABCD12") == True
    assert is_valid("AAAA") == True
    assert is_valid("HI") == True
    assert is_valid("AA27") == True
    assert is_valid("AB2") == True
    assert is_valid("GHJI9") == True
    assert is_valid("Harva5") == True