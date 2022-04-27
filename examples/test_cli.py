def print_hello(name):
    print('hello', name)


def test_spam(capsys):
    print_hello("World")
    captured = capsys.readouterr()
    assert captured.out == 'hello World\n'

def get_input():
    name = input("What is your name?")
    return name

def test_in(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "World")
    name = get_input()
    assert name == "World"
    
