from game import win_message
from game import Game
from game import Position


def test_win_message():
    assert win_message("o") == "Player o won!"


def test_create_game():
    g = Game()
    assert g.empty_board_str == "_"


def test_update_board():
    g = Game()
    g.update_board(g.player_one, Position(1, 2))
    assert g.board[2][1] == g.player_one


def test_game_start():
    g = Game()
    assert not g.finished()
