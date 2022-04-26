
def test_assign():
    x = 5
    assert x == 5

def test_change():
    x = 5
    x = 6
    assert x == 6

def test_type():
    x = 5
    assert type(x) is int

def test_mult_assign():
    x = 5
    y = x
    assert y == x
    assert y == 5
