import pytest


# - tuples
#   - creation
def test_create():
    tower = (100, "Projectile", 1)
    assert tower[0] == 100
    assert tower[1] == "Projectile"


#   - indexing
def test_index():
    towers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    for i in range(9):
        assert towers[i] == i + 1
        assert towers.__getitem__(i) == i + 1


# adding
def test_add():
    assert (3, 4) == (3, 4)
    assert (2, 3).__add__((1, 2)) == (2, 3, 1, 2)


#   - immutability
def test_immutability():
    s = (100, "Sniper", 3)
    with pytest.raises(TypeError) as e:
        s[1] = "Cannon"
    assert str(e.value) == "'tuple' object does not support item assignment"


def test_data():
    tower_data = ("Normal", 100, 1, 300, "Electric")
    towers_data = [("Cannon", 400, 3, 300, "Explosive"), tower_data]
    assert towers_data[0] == ("Cannon", 400, 3, 300, "Explosive")
    assert towers_data[1] == tower_data


def test_convert():
    tower = ("Normal", 100, 1, 300, "Electric")
    l = list(tower)
    assert l == ["Normal", 100, 1, 300, "Electric"]
    assert type(l) is list


#   - named tuple
from collections import namedtuple


def test_named_tuple():
    TowerTuple = namedtuple("Tower", ["type", "health", "level", "cost", "bonus_type"])
    tower = TowerTuple("Normal", 100, 1, 300, "Electric")
    assert tower[0] == "Normal"
    assert tower.type == "Normal"
    assert TowerTuple.__doc__ == "Tower(type, health, level, cost, bonus_type)"


#   - comprehension
def test_comprehension():
    tower_levels = tuple(i * 2 for i in range(3))
    assert tower_levels == (0, 2, 4)

    enemy_types = tuple(j for j in range(2, 13, 2))
    assert enemy_types == (2, 4, 6, 8, 10, 12)
