# - set
#   - creation
#     - from list
#     - comprehension
#   - in
#   - add


def test_creation():
    s = {1, 1, 2, 3, 3}  # noqa: B033
    assert {1, 2, 3} == s
    assert {1, 2, 3} == s


def test_comprehension():
    s = set(range(2, 30, 5))
    assert {2, 7, 12, 17, 22, 27} == s


def test_in():
    s = {1, 2, 4}
    assert 1 in s
    assert 2 in s
    assert 3 not in s


def test_add():
    s = set()
    assert len(s) == 0
    s.add(1)
    assert s == {1}
