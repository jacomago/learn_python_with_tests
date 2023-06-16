from tic_tac_toe.position import input_position


def win_message(player):
    return "Player " + player + " won!"


class Game:
    def __init__(
        self, board_size=3, empty_board_str="_", player_one="o", player_two="x"
    ):
        self.empty_board_str = empty_board_str
        self.board_size = board_size
        self.board = [
            [empty_board_str for column_index in range(board_size)]
            for row_index in range(board_size)
        ]
        self.player_one = player_one
        self.player_two = player_two
        self.current_player = player_one

    def board_state(self):
        return "\n".join("|".join(row) for row in self.board)

    def update_board(self, player, position):
        self.board[position.y][position.x] = player

    def position_used(self, position):
        if self.board[position.y][position.x] != self.empty_board_str:
            return True
        return False

    def reset_player(self, last_player=None):
        if not last_player:
            last_player = self.current_player
        if last_player == self.player_one:
            self.current_player = self.player_two
        else:
            self.current_player = self.player_one

    def get_position(self):
        while True:
            position = input_position()
            if not self.position_used(position):
                break
            else:
                print("Position used.")
        return position

    def play(self, player=None, position=None):
        if position is None:
            position = self.get_position()
        if player is None:
            player = self.current_player

        self.update_board(player, position)
        self.reset_player(last_player=player)

    def won(self, player):
        winning_list = [player for i in range(self.board_size)]

        # row check
        for row in self.board:
            if row == winning_list:
                return True

        # column check
        for column_index in range(self.board_size):
            if [
                self.board[row_index][column_index]
                for row_index in range(self.board_size)
            ] == winning_list:
                return True

        # diagonal check
        first_diagonal = [self.board[i][i] for i in range(self.board_size)]
        if first_diagonal == winning_list:
            return True

        second_diagonal = [
            self.board[i][self.board_size - 1 - i] for i in range(self.board_size)
        ]
        if second_diagonal == winning_list:
            return True

        return False

    def complete_board(self):
        for row in self.board:
            for col in row:
                if col == self.empty_board_str:
                    return False
        return True

    def finished(self):
        if (
            self.won(self.player_one)
            or self.won(self.player_two)
            or self.complete_board()
        ):
            return True
        return False

    def __str__(self):
        board_state = self.board_state()
        if self.finished():
            if self.won(self.player_one):
                return board_state + "\n" + win_message(self.player_one)
            elif self.won(self.player_two):
                return board_state + "\n" + win_message(self.player_two)
            else:
                return board_state + "\n" + "No winners!"
        return board_state


def main_method():
    print("Start game")
    game = Game()
    while not game.finished():
        game.play()
        print(game)


if __name__ == "__main__":
    main_method()
