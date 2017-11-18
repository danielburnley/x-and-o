import pytest

from main.grid import Grid, IllegalMoveError

class TestGrid:
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

    def test_given_grid_of_size_four_creates_correct_starting_grid(self):
        self.grid = Grid(size=4)
        assert self.grid.grid == [[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]
