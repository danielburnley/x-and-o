from main.ai import AI
from main.grid import IllegalMoveError

class Game():
    def __init__(self, grid):
        self.disable_ai = True
        self.grid = grid
        self.player = 'X'

    def winner(self):
        if self.grid.has_won():
            return self.next_player()
        return None

    def draw(self):
        return self.grid.has_draw()

    def finished(self):
        return self.grid.has_won() or self.grid.has_draw()

    def status(self):
        if self.winner():
            return '  Player ' + self.winner() + ' won!  '

        if self.draw():
            return '       Draw       '

        return 'Move of player ' + self.player

    def move(self, pos):
        self.grid.set_cell(self.player, pos)
        self.player = self.next_player()

        if not self.disable_ai and not self.finished():
            ai = AI(self, self.player)
            ai_move = ai.get_next_move()
            self.grid.set_cell(self.player, ai_move)
            self.player = self.next_player()

    def next_player(self):
        return 'O' if self.player == 'X' else 'X'

    def restore(self, game_data):
        self.grid.grid = game_data['grid']
        self.player = game_data['player']
        self.disable_ai = game_data['disable_ai']

    def to_dict(self):
        return {'grid': self.grid.grid, 'player': self.player, 'disable_ai': self.disable_ai}
