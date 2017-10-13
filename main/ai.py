import copy
from main.grid import Grid

class AI():
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.choice = None

    def get_next_move(self):
        self.minmax(self.game)
        return self.choice

    def minmax(self, game):
        if game.finished():
            return self.score(game)
        scores = []
        moves = []

        for move in game.grid.possible_moves():
            possible_game = copy.deepcopy(game)
            possible_game.move(move)
            scores.append(self.minmax(possible_game))
            moves.append(move)

        if game.player == self.player:
            max_score_index = scores.index(max(scores))
            self.choice = moves[max_score_index]
            return scores[max_score_index]
        else:
            min_score_index = scores.index(min(scores))
            self.choice = moves[min_score_index]
            return scores[min_score_index]

    def get_possible_moves(self, game):
        moves = game.grid.possible_moves()
        games = []
        for move in moves:
            new_game = copy.deepcopy(game)
            new_game.move(move)
            games.append(new_game)
        return games

    def score(self, game):
        grid = game.grid

        if(grid.has_won()):
            return 10 if game.winner() == self.player else -10
        else:
            return 0
