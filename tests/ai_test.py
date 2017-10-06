from main.ai import AI
from main.grid import Grid

class TestAI:
  pass
  # def test_only_one_move_possible(self):
  #   grid = Grid()
  #   ai = AI()

  #   grid.grid = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", ""]]
  #   assert(ai.next_move(grid) == (2,2))

  #   grid.grid = [["X", "", "X"], ["O", "X", "O"], ["O", "X", "O"]]
  #   assert(ai.next_move(grid) == (0,1))

  # def test_all_moves_possible(self):
  #   assert(AI().next_move(Grid()) == (0,0))

  # def test_other_player_started_not_in_center(self):
  #   grid = Grid()
  #   ai = AI()

  #   grid.set_cell("X", (0, 0))
  #   assert(ai.next_move(grid) == (1,1))

