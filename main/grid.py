class IllegalMoveError(Exception):
    pass


class Grid():
    def __init__(self, size=3):
        self.size = size
        self.grid = [[" " for x in range(self.size)] for x in range(self.size)]
        self.turns = 0

    def set_cell(self, val, pos):
        if self.grid[pos[0]][pos[1]] != " ":
            raise IllegalMoveError
        self.grid[pos[0]][pos[1]] = val
        self.turns = self.turns + 1

    def possible_moves(self):
        moves = []
        for index, row in enumerate(self.grid):
            for cell_index, cell in enumerate(row):
                if cell == " ":
                    moves.append((index, cell_index))
        return moves
