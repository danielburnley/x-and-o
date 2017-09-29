import pytest

from main.grid import Grid, IllegalMoveError

class TestGrid:
  WINNING_TEST_CASES = [
    [["X","X","X"],["","",""],["","",""]],
    [["","",""],["X","X","X"],["","",""]],
    [["","",""],["","",""],["X","X","X"]],
    [["X","",""],["X","",""],["X","",""]],
    [["","X",""],["","X",""],["","X",""]],
    [["","","X"],["","","X"],["","","X"]],
    [["X","",""],["","X",""],["","","X"]],
    [["","","X"],["","X",""],["X","",""]],
    [["O","O","O"],["","",""],["","",""]],
    [["","",""],["O","O","O"],["","",""]],
    [["","",""],["","",""],["O","O","O"]],
    [["O","",""],["O","",""],["O","",""]],
    [["","O",""],["","O",""],["","O",""]],
    [["","","O"],["","","O"],["","","O"]],
    [["O","",""],["","O",""],["","","O"]],
    [["","","O"],["","O",""],["O","",""]],
  ]

  def test_starting_grid(self):
    assert(Grid().grid == [["","",""],["","",""],["","",""]])

  def test_setting_the_top_left_square_to_X(self):
    grid = Grid()
    grid.set_cell("X", (0, 0))

    assert(grid.grid[0][0] == "X")
    assert(grid.turns == 1)

  def test_setting_the_middle_square(self):
    grid = Grid()
    grid.set_cell("O", (1, 1))

    assert(grid.grid[1][1] == "O")
    assert(grid.turns == 1)

  def test_setting_multiple_cells(self):
    grid = Grid()
    grid.set_cell("X", (0, 0))
    grid.set_cell("X", (0, 1))

    assert(grid.turns == 2)

  def test_has_won_with_empty_grid(self):
    assert(not Grid().has_won())

  def test_has_won_with_top_row_mix_of_X_and_O(self):
    grid = Grid()
    grid.set_cell("X", (0, 0))
    grid.set_cell("O", (0, 1))
    grid.set_cell("X", (0, 2))

    assert(not grid.has_won())

  def test_has_won_with_left_row_mix_of_X_and_O(self):
    grid = Grid()
    grid.set_cell("X", (0, 0))
    grid.set_cell("O", (1, 0))
    grid.set_cell("X", (2, 0))

    assert(not grid.has_won())

  def test_win_conditions(self):
    grid = Grid()
    for tested_grid in self.WINNING_TEST_CASES:
      grid.grid = tested_grid
      assert(grid.has_won())

  def test_has_draw_with_empty_grid(self):
    assert(not Grid().has_draw())

  def test_has_draw_with_empty_grid(self):
    grid = Grid()
    grid.grid = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
    assert(grid.has_draw())

  def test_has_draw_with_winning_row(self):
    grid = Grid()
    grid.grid = [["X", "X", "O"], ["X", "O", "O"], ["X", "O", "X"]]

    assert(not grid.has_draw())


  def test_raises_exception_for_overriding_moves(self):
    grid = Grid()
    grid.set_cell('X', (0, 0))
    with pytest.raises(IllegalMoveError):
          grid.set_cell('X', (0, 0))

  # All possible moves

  def test_one_move_remaining(self):
    grid = Grid()
    grid.grid = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", ""]]

    possible_moves = grid.possible_moves()

    assert(possible_moves == [(2,2)])

  def test_multiple_moves_remaining(self):
    grid = Grid()
    grid.grid = [["", "O", "X"], ["O", "", "O"], ["O", "X", ""]]

    possible_moves = grid.possible_moves()

    assert(possible_moves == [(0,0),(1,1),(2,2)])
