def test_if():
    x = True
    if x:
        assert True
        return
    raise AssertionError()


def test_else():
    x = True
    if not x:
        raise AssertionError()
    else:
        assert True


def test_elif():
    x = 1
    if x == 0:
        raise AssertionError()
    elif x == 1:
        assert True
    else:
        raise AssertionError()


def test_not():
    assert False is not True  # noqa: PLR0133
    assert True is not False  # noqa: PLR0133


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
    assert x and y is False
    assert z and y is False
    assert (y and y) is False
    assert z and x is True
