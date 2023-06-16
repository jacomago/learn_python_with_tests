

from tic_tac_toe import ai
from tic_tac_toe.game import Game
from tic_tac_toe.position import Position


def test_ai_plays():
    g = Game(board_size=1)
    assert not g.position_used(Position(0, 0))
    ai.play(g)
    assert g.position_used(Position(0, 0))


def test_ai_plays_once():
    g = Game()
    player = g.current_player
    ai.play(g)
    count = 0
    for row in g.board:
        for col in row:
            if col == player:
                count += 1
    assert count == 1


def test_ai_plays_win_row():
    g = Game()
    game_player = g.current_player
    g.play(player=game_player, position=Position(0, 0))
    g.play(player=game_player, position=Position(0, 1))
    g.current_player = game_player
    ai.play(g)
    assert g.won(game_player)


def test_ai_plays_win_col():
    g = Game()
    game_player = g.current_player
    g.play(player=game_player, position=Position(0, 0))
    g.play(player=game_player, position=Position(1, 0))
    g.current_player = game_player
    ai.play(g)
    assert g.won(game_player)


def test_ai_plays_win_diag():
    g = Game()
    game_player = g.current_player
    g.play(player=game_player, position=Position(0, 0))
    g.play(player=game_player, position=Position(1, 1))
    g.current_player = game_player
    ai.play(g)
    assert g.won(game_player)


def test_ai_blocks_play_row():
    g = Game()
    game_player = g.player_one
    g.play(player=game_player, position=Position(0, 0))
    g.play(player=game_player, position=Position(0, 1))
    g.current_player = g.player_two
    ai.play(g)
    assert g.position_used(Position(0, 2))


def test_ai_blocks_play_col():
    g = Game()
    game_player = g.player_one
    g.play(player=game_player, position=Position(0, 0))
    g.play(player=game_player, position=Position(1, 0))
    g.current_player = g.player_two
    ai.play(g)
    assert g.position_used(Position(2, 0))


def test_ai_blocks_play_diag():
    g = Game()
    game_player = g.player_one
    g.play(player=game_player, position=Position(0, 0))
    g.play(player=game_player, position=Position(1, 1))
    g.current_player = g.player_two
    ai.play(g)
    assert g.position_used(Position(2, 2))


def test_ai_looks_ahead_by_one():
    """
    _|x|_
    x|o|o
    _|_|_
    """
    g = Game()
    g.play(player=g.player_two, position=Position(0, 1))
    g.play(player=g.player_one, position=Position(1, 1))
    g.play(player=g.player_two, position=Position(1, 0))
    g.play(player=g.player_one, position=Position(1, 2))
    g.current_player = g.player_two
    ai.play(g)
    assert g.position_used(Position(0, 0))


def test_ai_looks_ahead_by_one_switch():
    """
    _|o|_
    x|o|_
    _|x|_
    """
    g = Game()
    g.play(player=g.player_two, position=Position(0, 1))
    g.play(player=g.player_one, position=Position(1, 0))
    g.play(player=g.player_two, position=Position(1, 2))
    g.play(player=g.player_one, position=Position(1, 1))
    g.current_player = g.player_two
    ai.play(g)
    assert g.position_used(Position(0, 2))


def test_ai_takes_centre():
    g = Game()
    ai.play(g)
    assert g.position_used(Position(1, 1))


def test_ai_takes_corner():
    g = Game()
    g.play(player=g.player_one, position=Position(1, 1))
    ai.play(g)
    assert (
        g.position_used(Position(0, 0))
        or g.position_used(Position(2, 2))
        or g.position_used(Position(0, 2))
        or g.position_used(Position(2, 0))
    )
