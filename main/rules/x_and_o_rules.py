class XAndORules:
    def has_won(self, grid):
        return self._row_won(grid) or self._col_won(grid) or self._diagonals_won(grid)

    def has_draw(self, grid):
        return " " not in self._flattened_grid(grid) and not self.has_won(grid)

    # Private

    def _row_won(self, grid):
        for row in grid.grid:
            if self._all_elements_equal_and_not_empty(row):
                return True
        return False

    def _col_won(self, grid):
        for i in range(grid.size):
            col = [row[i] for row in grid.grid]
            if self._all_elements_equal_and_not_empty(col):
                return True
        return False

    def _diagonals_won(self, grid):
        diagonal_left = [grid.grid[i][i] for i in range(grid.size)]
        if self._all_elements_equal_and_not_empty(diagonal_left):
            return True

        diagonal_right = [grid.grid[i][grid.size - 1 - i] for i in range(grid.size)]
        if self._all_elements_equal_and_not_empty(diagonal_right):
            return True

        return False

    def _all_elements_equal_and_not_empty(self, arr):
        return " " not in arr and len(set(arr)) == 1

    def _flattened_grid(self, grid):
        return [y for x in grid.grid for y in x]
