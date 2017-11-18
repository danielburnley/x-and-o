from main.grid import Grid
from main.rules.x_and_o_rules import XAndORules

class TestXAndORules:
    WINNING_TEST_CASES = [
        [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]],
        [[" ", " ", " "], ["X", "X", "X"], [" ", " ", " "]],
        [[" ", " ", " "], [" ", " ", " "], ["X", "X", "X"]],
        [["X", " ", " "], ["X", " ", " "], ["X", " ", " "]],
        [[" ", "X", " "], [" ", "X", " "], [" ", "X", " "]],
        [[" ", " ", "X"], [" ", " ", "X"], [" ", " ", "X"]],
        [["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]],
        [[" ", " ", "X"], [" ", "X", " "], ["X", " ", " "]],
        [["O", "O", "O"], [" ", " ", " "], [" ", " ", " "]],
        [[" ", " ", " "], ["O", "O", "O"], [" ", " ", " "]],
        [[" ", " ", " "], [" ", " ", " "], ["O", "O", "O"]],
        [["O", " ", " "], ["O", " ", " "], ["O", " ", " "]],
        [[" ", "O", " "], [" ", "O", " "], [" ", "O", " "]],
        [[" ", " ", "O"], [" ", " ", "O"], [" ", " ", "O"]],
        [["O", " ", " "], [" ", "O", " "], [" ", " ", "O"]],
        [[" ", " ", "O"], [" ", "O", " "], ["O", " ", " "]],
    ]

    def setup_method(self, method):
        self.grid = Grid()
        self.rules = XAndORules()

    def set_grid(self, grid):
        self.grid.grid = grid

    def set_cell(self, mark, position):
        self.grid.set_cell(mark, position)

    def assert_no_winner(self):
        assert not self.rules.has_won(self.grid)

    def assert_winner(self):
        assert self.rules.has_won(self.grid)

    def assert_no_draw(self):
        assert not self.rules.has_draw(self.grid)

    def assert_draw(self):
        assert self.rules.has_draw(self.grid)

    def test_has_won_with_empty_grid(self):
        self.assert_no_winner()

    def test_has_won_with_top_row_mix_of_X_and_O(self):
        self.set_cell("X", (0, 0))
        self.set_cell("O", (0, 1))
        self.set_cell("X", (0, 2))

        self.assert_no_winner()

    def test_has_won_with_left_row_mix_of_X_and_O(self):
        self.set_cell("X", (0, 0))
        self.set_cell("O", (1, 0))
        self.set_cell("X", (2, 0))

        self.assert_no_winner()

    def test_win_conditions(self):
        for tested_grid in self.WINNING_TEST_CASES:
            self.grid.grid = tested_grid
            self.assert_winner()

    def test_has_draw_with_empty_grid(self):
        self.assert_no_draw()

    def test_has_draw_with_empty_grid(self):
        self.set_grid([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]])
        self.assert_draw()

    def test_has_draw_with_winning_row(self):
        self.set_grid([["X", "X", "O"], ["X", "O", "O"], ["X", "O", "X"]])
        self.assert_no_draw()

# Variable Grid sizes

    WINNING_SIZE_FOUR_GRIDS = [
        [["X","X","X","X"],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]],
        [[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],["X","X","X","X"]],
        [["X"," "," "," "],["X"," "," "," "],["X"," "," "," "],["X"," "," "," "]],
        [[" "," "," ","X"],[" "," "," ","X"],[" "," "," ","X"],[" "," "," ","X"]],
        [["X"," "," "," "],[" ","X"," "," "],[" "," ","X"," "],[" "," "," ","X"]],
        [[" "," "," ","X"],[" "," ","X"," "],[" ","X"," "," "],["X"," "," "," "]]
    ]


    def test_given_winning_grids_with_size_four_correctly_returns_winner(self):
        self.grid = Grid(size=4)
        for tested_grid in self.WINNING_SIZE_FOUR_GRIDS:
            self.grid.grid = tested_grid
            self.assert_winner()


