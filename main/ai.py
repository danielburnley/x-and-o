import copy
from main.grid import Grid

class AI():
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.choice = None

    def get_next_move(self):
        if self.is_first_ai_move(self.game):
            return self.first_move(self.game)
        self.minmax(self.game)
        return self.choice

    def is_first_ai_move(self, game):
        flat_grid = [y for x in game.grid.grid for y in x]
        return flat_grid.count(" ") == (len(flat_grid) - 1)

    def first_move(self, game):
        if game.grid.grid[1][1] != " ":
            return (0, 0)
        else:
            return (1, 1)

    def minmax(self, game):
        if game.finished():
            return self.score(game)
        scores = []
        moves = []

        for move in game.grid.possible_moves():
            possible_game = copy.deepcopy(game)
            possible_game.move(move, possible_game.player.symbols[0])
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
