from main.game import Game
from main.player import Player

class GridSpy:
    def __init__(self):
        self.set_cell_called = False
        self.last_position_placed = None
        self.last_value_placed = None
        self.grid = [["F"],["O"],["O"]]

    def set_cell(self, value, pos):
        self.set_cell_called = True
        self.last_position_placed = pos
        self.last_value_placed = value

class RulesFake:
    def __init__(self):
        self.won = False
        self.draw = False

    def has_won(self, grid):
        return self.won

    def has_draw(self, grid):
        return self.draw

class TestGame:
    def setup_method(self, method):
        self.players = [Player('One', ['X']), Player('Two', ['O'])]
        self.game = Game(GridSpy(), self.players, RulesFake())

    def play_move(self, move):
        self.game.move(move, self.game.player.symbols[0])

    def set_game_won(self, has_won):
        self.game.rules.won = True

    def assert_current_player(self, expected_player):
        assert self.game.player == expected_player

    def assert_status(self, expected_status):
        assert self.game.status() == expected_status

    def assert_winner(self, expected_winner):
        assert self.game.winner() == expected_winner

    def test_starts_with_player_X(self):
        self.assert_current_player(self.players[0])

    def test_player_changed_after_making_a_move(self):
        self.play_move((1, 1))
        self.assert_current_player(self.players[1])

    def test_alternating_between_players(self):
        self.play_move((1, 1))
        self.play_move((1, 2))
        self.assert_current_player(self.players[0])

    def test_given_move_game_calls_set_cell(self):
        self.play_move((1, 1))
        assert self.game.grid.last_value_placed == self.players[0].symbols[0]
        assert self.game.grid.set_cell_called

    def test_make_a_move_at_pos(self):
        self.play_move((1, 1))
        assert self.game.grid.last_position_placed == (1, 1)

    def test_winner_returns_none_when_not_won(self):
        self.assert_winner(None)

    def test_winner_returns_next_player_when_won(self):
        self.set_game_won(True)
        self.assert_winner(self.players[1])

    def test_status_when_player_is_x(self):
        self.assert_status("Move of player One")

    def test_status_when_player_is_o(self):
        self.play_move((1,1))
        self.assert_status("Move of player Two")

    def test_status_when_player_x_won(self):
        self.set_game_won(True)
        self.play_move((1,1))
        self.assert_status("  Player One won!  ")

    def test_status_when_player_o_won(self):
        self.set_game_won(True)
        self.assert_status("  Player Two won!  ")

    def test_status_when_player_draw(self):
        self.game.rules.draw = True
        self.assert_status("       Draw       ")

    def test_to_dict(self):
        game_data = self.game.to_dict()
        assert game_data == {
            'disable_ai': True,
            'grid': [['F'], ['O'], ['O']],
            'players': [
                {'name': 'One', 'symbols': ['X']},
                {'name': 'Two', 'symbols': ['O']}
            ],
            'player': {'name': 'One', 'symbols': ['X']}
        }

    def test_restore(self):
        players = [Player('One', ['D']), Player('Two', ['F'])]
        game_data = {
            'disable_ai': True,
            'grid': [['F'], ['D'], ['D']],
            'players': [
                {'name': 'One', 'symbols': ['D']},
                {'name': 'Two', 'symbols': ['F']}
            ],
            'player': {'name': 'Two', 'symbols': ['F']}
        }
        self.game.restore(game_data)
        assert self.game.disable_ai == game_data['disable_ai']
        assert self.game.grid.grid == game_data['grid']
        assert self.game.players == players
        assert self.game.player == players[1]

    def test_assert_gets_won_from_rules(self):
        self.set_game_won(True)
        assert self.game.has_won()

    def test_assert_gets_won_from_rules(self):
        self.game.rules.draw = True
        assert self.game.has_draw()
