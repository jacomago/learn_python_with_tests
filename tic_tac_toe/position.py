class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get():
        pos = input("Which position, x, y?")
        pos = pos.split(",")
        return Position(int(pos[0]) - 1, int(pos[1]) - 1)

