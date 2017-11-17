from main.ai import AI
from main.grid import IllegalMoveError
from main.player import Player

class Game():
    def __init__(self, grid, players):
        self.disable_ai = True
        self.grid = grid
        self.players = players
        self.player = self.players[0]

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
            return '  Player ' + str(self.winner()) + ' won!  '

        if self.draw():
            return '       Draw       '

        return 'Move of player ' + str(self.player)

    def move(self, pos, symbol=None):
        if not symbol:
            symbol = self.player.symbols[0]

        self.grid.set_cell(symbol, pos)
        self.player = self.next_player()

        if not self.disable_ai and not self.finished():
            ai = AI(self, self.player)
            ai_move = ai.get_next_move()
            self.grid.set_cell(self.player.symbols[0], ai_move)
            self.player = self.next_player()

    def next_player(self):
        return self.players[1] if self.player == self.players[0] else self.players[0]

    def restore(self, game_data):
        self.grid.grid = game_data['grid']
        self.player = game_data['player']
        self.disable_ai = game_data['disable_ai']
        self.players = [Player(player['name'], player['symbols']) for player in game_data['players']]
        self.player = Player(game_data['player']['name'], game_data['player']['symbols'])

    def to_dict(self):
        return {
            'grid': self.grid.grid,
            'players': self.build_player_dict(),
            'player': self.player.to_dict(),
            'disable_ai': self.disable_ai
        }

    def build_player_dict(self):
        return [player.to_dict() for player in self.players]
