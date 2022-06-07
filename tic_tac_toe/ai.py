from copy import deepcopy
from game import Game
from position import Position


def check_all_pos(g: Game, player, check):
    for row in range(g.board_size):
        for col in range(g.board_size):
            pos = Position(row, col)
            if not g.position_used(pos):
                g_copy = deepcopy(g)
                g_copy.play(position=pos, player=player)
                if check(g_copy, player):
                    return pos
    return None


def check_all_pos_win(g: Game, player):
    return check_all_pos(g, player, check_position_wins)


def check_position_wins(g: Game, player):
    if g.won(player):
        return True
    return False


def empty_corner(g: Game):
    empty_corners = []
    for pos in [
        Position(0, 0),
        Position(0, g.board_size - 1),
        Position(g.board_size - 1, 0),
        Position(g.board_size - 1, g.board_size - 1),
    ]:
        if not g.position_used(pos):
            return pos
    return None


def empty_centre(g: Game):
    mid = int((g.board_size - 1) / 2)
    pos = Position(mid, mid)
    if not g.position_used(pos):
        return pos
    return None

class TTTai:
    def play(g: Game):
        pos = check_all_pos_win(g, g.current_player)
        if pos != None:
            g.play(position=pos)
            return

        if g.current_player == g.player_one:
            other_player = g.player_two
        else:
            other_player = g.player_one

        pos = check_all_pos_win(g, other_player)
        if pos != None:
            g.play(position=pos)
            return

        pos = empty_centre(g)
        if pos != None:
            g.play(position=pos)
            return

        pos = empty_corner(g)
        if pos != None:
            g.play(position=pos)
            return