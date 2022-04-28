def test_assign():
    health = 5
    assert health == 5


def test_change():
    health = 5
    health = 6
    assert health == 6


def test_type():
    health = 5
    assert type(health) is int


def test_mult_assign():
    health = 5
    new_health = health
    assert new_health == health
    assert new_health == 5
