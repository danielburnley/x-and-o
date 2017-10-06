import random
import time
from grid import IllegalMoveError

class Game:
    def __init__(self, grid):
        self.grid = grid
        self.player = 'X'

    def winner(self):
        if self.grid.has_won():
            return self.next_player()
        return None

    def draw(self):
        return self.grid.has_draw()

    def status(self):
        if self.winner():
            return '  Player ' + self.winner() + ' won!  '

        if self.draw():
            return '       Draw       '

        return 'Move of player ' + self.player

    def move(self, pos):
        self.grid.set_cell(self.player, pos)
        self.player = self.next_player()
        if not self.winner() and not self.draw():
            self.ai_move()
            self.player = self.next_player()

    def ai_move(self):
        row = random.randint(0,2)
        col = random.randint(0,2)
        try:
            self.grid.set_cell(self.player, (row, col))
        except IllegalMoveError:
            self.ai_move()

    def next_player(self):
        return 'O' if self.player == 'X' else 'X'
