class Position:
    def get(self):
        pos = input("Which position, x, y?")
        pos = pos.split(",")
        self.x = int(pos[0]) - 1
        self.y = int(pos[1]) - 1


class Game:
    def __init__(self):
        self.board = [
            ["_" for column_index in range(3)] for row_index in range(3)
        ]  # [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        self.player = "o"
        self.player_two = "x"

    def position_used(self, position):
        if self.board[position.y][position.x] != "_":
            return True
        return False

    def player_play(self, player):
        position = Position()

        while True:
            print("Player ", player, " your turn.")
            position.get()
            if not self.position_used(position):
                break

        self.board[position.y][position.x] = player


    def play(self):
        self.player_play(self.player)
        print(self)
        if self.won(self.player):
            return 
        self.player_play(self.player_two)
        print(self)


    def won(self, player):
        winning_list = [player, player, player]

        for row in self.board:
            if row == winning_list:
                return True

        # column check
        for column_index in range(3):
            if [
                self.board[row_index][column_index] for row_index in range(3)
            ] == winning_list:
                return True

        # diagonal check
        first_diagonal = [self.board[i][i] for i in range(3)]
        if first_diagonal == winning_list:
            return True

        second_diagonal = [self.board[i][2 - i] for i in range(3)]
        if second_diagonal == winning_list:
            return True

        return False

    def __str__(self):
        return "\n".join("|".join(row) for row in self.board)

    def complete_board(self):
        for row in self.board:
            for col in row:
                if col == "_":
                    return False
        return True

    def finished(self):
        if self.won(self.player) or self.won(self.player_two) or self.complete_board():
            return True
        return False


def main():
    game = Game()
    while not game.finished():
        game.play()


main()
