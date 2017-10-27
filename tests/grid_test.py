import pytest

from main.grid import Grid, IllegalMoveError

class TestGrid:
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

    def set_cell(self, mark, position):
        self.grid.set_cell(mark, position)

    def assert_value_at_position(self, position, expected_value):
        assert self.grid.grid[position[0]][position[1]] == expected_value

    def assert_turns_passed(self, expected_value):
        assert self.grid.turns == expected_value

    def assert_possible_moves(self, expected_moves):
        assert self.grid.possible_moves() == expected_moves

    def set_grid(self, grid):
        self.grid.grid = grid

    def test_starting_grid(self):
        assert self.grid.grid == [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def test_setting_the_top_left_square_to_X(self):
        self.set_cell("X", (0, 0))

        self.assert_value_at_position((0, 0), "X")
        self.assert_turns_passed(1)

    def test_setting_the_middle_square(self):
        self.set_cell("O", (1, 1))

        self.assert_value_at_position((1, 1), "O")
        self.assert_turns_passed(1)

    def test_setting_multiple_cells(self):
        self.set_cell("X", (0, 0))
        self.set_cell("X", (0, 1))

        self.assert_turns_passed(2)

    def test_has_won_with_empty_grid(self):
        assert not self.grid.has_won()

    def test_has_won_with_top_row_mix_of_X_and_O(self):
        self.set_cell("X", (0, 0))
        self.set_cell("O", (0, 1))
        self.set_cell("X", (0, 2))

        assert not self.grid.has_won()

    def test_has_won_with_left_row_mix_of_X_and_O(self):
        self.set_cell("X", (0, 0))
        self.set_cell("O", (1, 0))
        self.set_cell("X", (2, 0))

        assert not self.grid.has_won()

    def test_win_conditions(self):
        for tested_grid in self.WINNING_TEST_CASES:
            self.grid.grid = tested_grid
            assert self.grid.has_won()

    def test_has_draw_with_empty_grid(self):
        assert not self.grid.has_draw()

    def test_has_draw_with_empty_grid(self):
        self.set_grid([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]])
        assert self.grid.has_draw()

    def test_has_draw_with_winning_row(self):
        self.set_grid([["X", "X", "O"], ["X", "O", "O"], ["X", "O", "X"]])

        assert not self.grid.has_draw()

    def test_raises_exception_for_overriding_moves(self):
        self.set_cell('X', (0, 0))
        with pytest.raises(IllegalMoveError):
            self.set_cell('X', (0, 0))

# All possible moves

    def test_one_move_remaining(self):
        self.set_grid([["X", "O", "X"], ["O", "X", "O"], ["O", "X", " "]])

        self.assert_possible_moves([(2,2)])

    def test_multiple_moves_remaining(self):
        self.set_grid([[" ", "O", "X"], ["O", " ", "O"], ["O", "X", " "]])

        self.assert_possible_moves([(0,0),(1,1),(2,2)])
