from tic_tac_toe.position import Position


def test_init():
    p = Position(3, 4)
    assert p.x == 3
    assert p.y == 4
    assert p.__class__ == Position


def test_eq():
    p0 = Position(3, 4)
    p1 = Position(3, 4)
    assert p0 == p1
    p1 = Position(4, 3)
    assert p0 != p1
    assert None is not p0


def test_get(monkeypatch):
    p0 = Position(3, 4)
    monkeypatch.setattr("builtins.input", lambda _: p0.input_str())
    p = Position.get()
    assert p0 == p


def test_input_str():
    p = Position(3, 4)
    assert p.input_str() == "4,5"
