# - list
#   - loop over index
#   - loop over value
#   - comprehension
#   - in
#   - append


def test_loop_index():
    tower_types = ["Cannon", "Sniper", "Arrow", "Freeze"]
    for ind in range(len(tower_types)):
        assert tower_types[ind] in ("Cannon", "Sniper", "Arrow", "Freeze")


def test_loop_value():
    tower_types = ["Cannon", "Sniper", "Arrow", "Freeze"]
    for value in tower_types:
        assert value in ("Cannon", "Sniper", "Arrow", "Freeze")


def test_loop_comprehension():
    tower_levels = [i * 2 for i in range(3)]
    assert tower_levels == [0, 2, 4]


def test_in():
    assert 3 in [1, 2, 3]


def test_append():
    tower_levels = []
    tower_levels.append(1)
    assert tower_levels == [1]
