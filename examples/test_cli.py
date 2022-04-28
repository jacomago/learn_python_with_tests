def print_tower_level(level):
    print("Level", level)


def test_print_tower_level(capsys):
    print_tower_level(10)
    captured = capsys.readouterr()
    assert captured.out == "Level 10\n"


def get_tower_choice():
    choice = input("What tower do you want to build?")
    return choice


def test_tower_choice(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Cannon")
    choice = get_tower_choice()
    assert choice == "Cannon"
