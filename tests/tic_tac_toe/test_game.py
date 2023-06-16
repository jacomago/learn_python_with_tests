from tic_tac_toe.game import Game, win_message
from tic_tac_toe.position import Position


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


def test_not_won():
    g = Game()
    assert not g.won(g.player_one)
    assert not g.won(g.player_two)


def play_winning_row(g: Game, game_player):
    g.play(player=game_player, position=Position(0, 0))
    g.play(player=game_player, position=Position(0, 1))
    g.play(player=game_player, position=Position(0, 2))


def test_won_row():
    g = Game()
    game_player = g.player_one
    play_winning_row(g, game_player)
    assert g.won(game_player)


def test_won_column():
    g = Game()
    game_player = g.player_one
    g.play(player=game_player, position=Position(0, 0))
    g.play(player=game_player, position=Position(1, 0))
    g.play(player=game_player, position=Position(2, 0))
    assert g.won(game_player)


def test_won_first_diag():
    g = Game()
    game_player = g.player_one
    g.play(player=game_player, position=Position(0, 0))
    g.play(player=game_player, position=Position(1, 1))
    g.play(player=game_player, position=Position(2, 2))
    assert g.won(game_player)


def test_won_second_diag():
    g = Game()
    game_player = g.player_one
    g.play(player=game_player, position=Position(0, 2))
    g.play(player=game_player, position=Position(1, 1))
    g.play(player=game_player, position=Position(2, 0))
    assert g.won(game_player)


def play_complete_board_without_win(g: Game):
    """
    o x x
    x o o
    x o x
    """
    g.play(player=g.player_one, position=Position(0, 0))
    g.play(player=g.player_two, position=Position(0, 1))
    g.play(player=g.player_two, position=Position(0, 2))
    g.play(player=g.player_two, position=Position(1, 0))
    g.play(player=g.player_one, position=Position(1, 1))
    g.play(player=g.player_one, position=Position(1, 2))
    g.play(player=g.player_two, position=Position(2, 0))
    g.play(player=g.player_one, position=Position(2, 1))
    g.play(player=g.player_two, position=Position(2, 2))


def test_complete_board():
    g = Game()
    assert not g.complete_board()
    play_complete_board_without_win(g)
    assert g.complete_board()


def test_game_finished_init():
    g = Game()
    assert not g.finished()


def test_game_finished_won():
    g = Game()
    game_player = g.player_one
    play_winning_row(g, game_player)
    assert g.finished()


def test_game_finished_complete_board():
    g = Game()
    play_complete_board_without_win(g)
    assert not g.won(g.player_one)
    assert not g.won(g.player_two)
    assert g.finished()


def test_str_init():
    g = Game()
    assert str(g) == g.board_state()


def test_str_win():
    g = Game()
    game_player = g.player_one
    play_winning_row(g, game_player)
    assert str(g) == g.board_state() + "\n" + win_message(game_player)


def test_str_stalemate():
    g = Game()
    play_complete_board_without_win(g)
    assert str(g) == g.board_state() + "\n" + "No winners!"
