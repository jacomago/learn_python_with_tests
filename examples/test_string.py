import pytest

def test_string():
    x = "Cannon"
    assert type(x) is str


def test_add():
    x = "Cannon"
    y = "Sniper"
    assert x + y == "CannonSniper"


def test_join():
    x = "Cannon"
    y = "Sniper"
    z = "Freeze"
    assert " ".join((x, y, z)) == "Cannon Sniper Freeze"


def test_format():
    s = "Tower types are: {} {} {}."
    x = "Cannon"
    y = "Sniper"
    z = "Freeze"
    assert s.format(x, y, z) == "Tower types are: Cannon Sniper Freeze."


def test_format_advanced():
    s = "Cannon details, cost:{:.2e} power factor:{:.2f} health:{:.2%}"
    x = 10000
    y = 12.7777777
    z = 0.5
    assert (
        s.format(x, y, z)
        == "Cannon details, cost:1.00e+04 power factor:12.78 health:50.00%"
    )


# This shows that we get the error we expect when we try to just insert a new character in the string.
def test_immutability_again():
    s = "Cannon"
    with pytest.raises(TypeError) as e:
        s[1] = "o"
    assert str(e.value) == "'str' object does not support item assignment"


# This gets around string immutability by making a new one using characters from the old.
def test_immutability_workaround():
    s = "Cannon"
    assert s[0] + "o" + s[2:] == "Connon"
