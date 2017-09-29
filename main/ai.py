from main.grid import Grid

class AI:
  def next_move(self, grid: Grid):
    if grid.turns == 1:
      if grid.grid[0][0] == "X":
        return (1, 1)
    return grid.possible_moves()[0]
