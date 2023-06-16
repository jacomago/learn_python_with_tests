def test_while():
    int_sum = 0
    count = 10
    while count > 0:
        int_sum += 5
        count -= 5
    assert count == 0
    assert int_sum == 10


def test_for():
    int_sum = 0
    for i in range(0, 10, 5):
        int_sum += i
    assert int_sum == 5
