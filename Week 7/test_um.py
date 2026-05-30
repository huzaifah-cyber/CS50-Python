from um import count

def test_true_count():
    assert count("um") == 1
    assert count("um, um.") == 2
    assert count("UM, um.... um ") == 3
    assert count("Yum yum tummy") == 0

def test_false_count():
    assert count("um") != 3
    assert count("um, um.") != 3
    assert count("UM, um.... um ") != 1

def test_spaces_count():
    assert count(" u m ") == 0
    assert count(" um ") == 1
    assert count(" um ... um ") == 2


