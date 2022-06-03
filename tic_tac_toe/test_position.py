from position import *

def test_init():
    p = Position(3, 4)
    assert p.x == 3
    assert p.y == 4
    assert p.__class__ == Position

def test_get(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "4,5")
    p = Position.get()
    assert p.x == 3
    assert p.y == 4
    assert p.__class__ == Position


