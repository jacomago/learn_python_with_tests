
# - tuples

#   - creation
import pytest


def test_create():
    t = (1, "french")
    assert t[0] == 1
    assert t[1] == "french"

#   - indexing
def test_index():
    t = (1,2,3,4,5,6,7,8,9)
    for i in range(9):
        assert t[i] == i + 1 
        assert t.__getitem__(i) == i + 1

# adding
def test_add():
    assert (3,) + (4,) == (3,4)
    assert (2,3 ).__add__((1,2)) == (2,3,1,2)

#   - immutability

def test_immutability():
    s = (1,2,3)
    with pytest.raises(TypeError) as e:
        s[1] = "hello"
    assert str(e.value) == "'tuple' object does not support item assignment"

def test_data():
    car_data = ("ferrari", 1997, "Red", "Italian", "Electric")
    many_cars = [("bmw"), car_data]
    assert many_cars[0] == ("bmw")
    assert many_cars[1] == car_data

def test_convert():
    t = (4,5,6)
    l = list(t)
    assert l == [4,5,6]
    assert type(l) is list

#   - named tuple
from collections import namedtuple

def test_named_tuple():
    CarTuple = namedtuple('Car', ['make', 'year', 'color', 'country', 'type'])
    c = CarTuple("ferrari", 1997, "Red", "Italy", "Electric")
    assert c[0] == "ferrari"
    assert c.make == "ferrari"
    assert CarTuple.__doc__ == "Car(make, year, color, country, type)"


#   - comprehension
def test_comprehension():
    t = tuple((i*2 for i in range(3)))
    assert t == (0,2,4)

    t = tuple((j for j in range(2, 13, 2)))
    assert t == (2, 4, 6, 8, 10, 12)