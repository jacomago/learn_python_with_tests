class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get():
        pos = input("Which position, x, y?")
        pos = pos.split(",")
        return Position(int(pos[0]) - 1, int(pos[1]) - 1)

    def input_str(self):
        return str(self.x + 1) + "," + str(self.y + 1)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Position):
            return self.x == __o.x and self.y == __o.y
        return False
