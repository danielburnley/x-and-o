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

    def has_won(self):
        return self._row_won() or self._col_won() or self._diagonals_won()

    def has_draw(self):
        return " " not in self._flattened_grid() and not self.has_won()

    def possible_moves(self):
        moves = []
        for index, row in enumerate(self.grid):
            for cell_index, cell in enumerate(row):
                if cell == " ":
                    moves.append((index, cell_index))
        return moves

    # Private

    def _row_won(self):
        for row in self.grid:
            if self._all_elements_equal_and_not_empty(row):
                return True
        return False

    def _col_won(self):
        for i in range(self.size):
            col = [row[i] for row in self.grid]
            if self._all_elements_equal_and_not_empty(col):
                return True
        return False

    def _diagonals_won(self):
        diagonal_left = [self.grid[i][i] for i in range(self.size)]
        if self._all_elements_equal_and_not_empty(diagonal_left):
            return True

        diagonal_right = [self.grid[i][self.size - 1 - i] for i in range(self.size)]
        if self._all_elements_equal_and_not_empty(diagonal_right):
            return True

        return False

    def _all_elements_equal_and_not_empty(self, arr):
        return " " not in arr and len(set(arr)) == 1

    def _flattened_grid(self):
        return [y for x in self.grid for y in x]
