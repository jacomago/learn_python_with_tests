import copy

class Cool:
    def __init__(self, x: int, y: list) -> None:
        self.x = x
        self.y = y

def test_no_copy():
    c = Cool(3, [4])

    assert c.x == 3
    c.x = 7
    assert c.x == 7

    assert c.y == [4]
    c.y.append(5)
    assert c.y == [4, 5]

def test_copy():
    c = Cool(3, [4])

    assert c.x == 3
    c2 = copy.copy(c)
    c2.x = 7
    assert c.x == 3
    assert c2.x == 7

    assert c.y == [4]
    c3 = copy.copy(c)
    c3.y.append(5)
    assert c3.y == [4, 5]
    assert c.y == [4, 5]

def test_deepcopy():
    c = Cool(3, [4])

    assert c.x == 3
    c2 = copy.deepcopy(c)
    c2.x = 7
    assert c.x == 3
    assert c2.x == 7

    assert c.y == [4]
    c3 = copy.deepcopy(c)
    c3.y.append(5)
    assert c3.y == [4, 5]
    assert c.y == [4]

