from game import win_message
from game import Game
from position import Position


def test_win_message():
    assert win_message("o") == "Player o won!"


def test_create_game():
    g = Game()
    assert g.empty_board_str == "_"
    assert g.board == [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    assert g.current_player == "o"


def test_start_board_state():
    g = Game()
    assert (
        g.board_state()
        == """_|_|_
_|_|_
_|_|_"""
    )


def test_update_board():
    g = Game()
    g.update_board(g.player_one, Position(1, 2))
    assert g.board[2][1] == g.player_one


def test_board_state():
    g = Game()
    g.update_board(g.player_one, Position(1, 2))
    assert (
        g.board_state()
        == """_|_|_
_|_|_
_|o|_"""
    )


def test_position_used():
    g = Game()
    p = Position(1, 2)
    g.update_board(g.player_one, p)
    assert g.position_used(p)


def test_reset_player():
    g = Game()
    assert g.current_player == g.player_one
    g.reset_player()
    assert g.current_player == g.player_two


def test_get_position(monkeypatch):
    g = Game()
    pn = Position(0, 1)
    monkeypatch.setattr("builtins.input", lambda _: pn.input_str())
    pgn = g.get_position()
    assert pgn == pn

def test_play_default(monkeypatch):
    g = Game()
    pn = Position(0, 1)
    assert not g.position_used(pn)
    assert g.current_player == g.player_one
    monkeypatch.setattr("builtins.input", lambda _: pn.input_str())
    g.play()
    assert g.position_used(pn)
    assert g.current_player == g.player_two

def test_play_player_set(monkeypatch):
    g = Game()
    pn = Position(0, 1)
    assert not g.position_used(pn)
    assert g.current_player == g.player_one
    monkeypatch.setattr("builtins.input", lambda _: pn.input_str())
    g.play(player=g.player_two)
    assert g.position_used(pn)
    assert g.board[pn.y][pn.x] == g.player_two
    assert g.current_player == g.player_one

def test_play_position_set():
    g = Game()
    pn = Position(0, 1)
    assert not g.position_used(pn)
    assert g.current_player == g.player_one
    g.play(position=pn)
    assert g.position_used(pn)
    assert g.current_player == g.player_two

def test_play_position_player_set():
    g = Game()
    pn = Position(0, 1)
    assert not g.position_used(pn)
    assert g.current_player == g.player_one
    g.play(position=pn, player=g.player_two)
    assert g.position_used(pn)
    assert g.board[pn.y][pn.x] == g.player_two
    assert g.current_player == g.player_one

def test_game_finished():
    g = Game()
    assert not g.finished()
