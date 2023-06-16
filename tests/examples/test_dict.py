# - dict
#   - creation
#   - get value
#   - get key and value
#   - loop over key
#   - loop over value


def test_create():
    d = {}
    d["damage"] = 10
    d["power"] = 20.0
    assert d == {"damage": 10, "power": 20.0}


def test_comp():
    d = {i: i * 2 for i in [3, 4]}
    assert d == {3: 6, 4: 8}


def test_get_val():
    d = {"damage": 10, "power": 20.0}
    assert d["damage"] == 10


def test_get_key_and_val():
    d = {"damage": 10, "power": 20.0}
    for k, v in d.items():
        if k == "damage":
            assert v == 10
        if k == "power":
            assert v == 20


def test_loop_key():
    d = {"damage": 10, "power": 20.0}
    for k in d:
        if k == "damage":
            assert d[k] == 10
        if k == "power":
            assert d[k] == 20


def test_loop_value():
    d = {"damage": 10, "power": 20.0}
    count = 0
    for v in d.values():
        if count == 0:
            assert v == 10
        if count == 1:
            assert v == 20
        count += 1
