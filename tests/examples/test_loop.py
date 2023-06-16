def test_while():
    sum = 0
    count = 10
    while count > 0:
        sum += 5
        count -= 5
    assert count == 0
    assert sum == 10


def test_for():
    sum = 0
    for i in range(0, 10, 5):
        sum += i
    assert sum == 5
