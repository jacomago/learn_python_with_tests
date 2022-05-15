def test_if():
    x = True
    if x:
        assert True
        return
    assert False


def test_else():
    x = True
    if not x:
        assert False
    else:
        assert True


def test_elif():
    x = 1
    if x == 0:
        assert False
    elif x == 1:
        assert True
    else:
        assert False


def test_not():
    assert not False == True
    assert not True == False


def test_or():
    x = True
    y = False
    assert x or y
    assert x or True
    assert not (False or y)


def test_and():
    x = True
    y = False
    z = True
    assert x and y == False
    assert z and y == False
    assert (y and y) == False
    assert z and x == True
