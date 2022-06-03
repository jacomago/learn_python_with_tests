from tic_tac_toe.ai import TTTai
from tic_tac_toe.game import Game
from tic_tac_toe.position import Position


def test_ai_plays():
    g = Game(board_size=1)
    assert not g.position_used(Position(0, 0))
    TTTai.play(g)
    assert g.position_used(Position(0, 0))


def test_ai_plays_win_row():
    g = Game()
    game_player = g.current_player
    g.play(player=game_player, position=Position(0, 0))
    g.play(player=game_player, position=Position(0, 1))
    g.current_player = game_player
    TTTai.play(g)
    assert g.won(game_player)


def test_ai_plays_win_col():
    g = Game()
    game_player = g.current_player
    g.play(player=game_player, position=Position(0, 0))
    g.play(player=game_player, position=Position(1, 0))
    g.current_player = game_player
    TTTai.play(g)
    assert g.won(game_player)


def test_ai_plays_win_diag():
    g = Game()
    game_player = g.current_player
    g.play(player=game_player, position=Position(0, 0))
    g.play(player=game_player, position=Position(1, 1))
    g.current_player = game_player
    TTTai.play(g)
    assert g.won(game_player)


def test_ai_blocks_play_row():
    g = Game()
    game_player = g.player_one
    g.play(player=game_player, position=Position(0, 0))
    g.play(player=game_player, position=Position(0, 1))
    g.current_player = g.player_two
    TTTai.play(g)
    assert g.position_used(Position(0, 2))


def test_ai_blocks_play_col():
    g = Game()
    game_player = g.player_one
    g.play(player=game_player, position=Position(0, 0))
    g.play(player=game_player, position=Position(1, 0))
    g.current_player = g.player_two
    TTTai.play(g)
    assert g.position_used(Position(2, 0))


def test_ai_blocks_play_diag():
    g = Game()
    game_player = g.player_one
    g.play(player=game_player, position=Position(0, 0))
    g.play(player=game_player, position=Position(1, 1))
    g.current_player = g.player_two
    TTTai.play(g)
    assert g.position_used(Position(2, 2))


def test_ai_looks_ahead_by_one_diag():
    g = Game()
    g.play(player=g.player_one, position=Position(1, 1))
    g.play(player=g.player_two, position=Position(0, 0))
    g.play(player=g.player_two, position=Position(2, 2))
    g.current_player = g.player_two
    TTTai.play(g)
    assert g.position_used(Position(0, 2)) or g.position_used((Position(2, 0)))


def test_ai_looks_ahead_by_one_cross():
    g = Game()
    g.play(player=g.player_two, position=Position(0, 1))
    g.play(player=g.player_two, position=Position(1, 0))
    g.current_player = g.player_two
    TTTai.play(g)
    assert g.position_used(Position(1, 1))


def test_ai_takes_centre():
    g = Game()
    TTTai.play(g)
    assert g.position_used(Position(1, 1))

def test_ai_takes_corner():
    g = Game()
    g.play(player=g.player_one, position=Position(1, 1))
    TTTai.play(g)
    assert (
        g.position_used(Position(0, 0))
        or g.position_used(Position(2, 2))
        or g.position_used(Position(0, 2))
        or g.position_used(Position(2, 0))
    )
