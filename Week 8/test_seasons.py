import pytest
from seasons import check

def test_correct_check():
    # It should return the string if the format matches
    assert check("1998-01-25") == "1998-01-25"
    assert check("2000-12-31") == "2000-12-31"


def test_incorrect_check():
    # We use pytest.raises(SystemExit) to catch the sys.exit()
    with pytest.raises(SystemExit):
        check("January 1, 1999")

    with pytest.raises(SystemExit):
        check("1999/01/01")

    with pytest.raises(SystemExit):
        check("cat")