# - functions
#   - input variables
#     - named
#     - typed
#     - default values
#   - output
#     - one
#     - many
#     - typed


def test_func():
    def shot_power():
        return 5

    assert shot_power() == 5


def test_input_variable():
    def shots_total_power(shots):
        return shots

    assert shots_total_power(1) == 1


def test_named_input():
    def shot_power(shots):
        return 1.5 * shots

    assert shot_power(shots=10) == 15


# python don't care about types have to use mypy to get an error
def test_typed_input():
    def shot_power(shots: int):
        return 1.5 * shots

    s = shot_power(2.5)
    assert s == 3.75


def test_default_values():
    def shots_total_power(shots=1):
        return shots

    assert shots_total_power() == 1


def test_no_output():
    def fire():
        return

    assert fire() is None


def test_one_output():
    def fire():
        return 1

    assert fire() == 1


def test_mult_output():
    def fire():
        return 1, 2, "Cannon"

    big, small, name = fire()
    assert big == 1
    assert small == 2
    assert name == "Cannon"


# python don't care about types have to use mypy to get an error
def test_typed_output():
    def fire() -> int:
        return "a"

    out = fire()
    assert out == "a"
