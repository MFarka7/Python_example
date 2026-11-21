def add (a, b) -> int:
    return a + b

def test_add_two_positive_numbers():
    p=add(2, 3)


    assert p == 5

def test_add_two_negative_numbers():
    p=add(-2, -3)

    
    assert p == -5  