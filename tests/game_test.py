from main.game import Game

class GridSpy:
    def __init__(self):
        self.set_cell_called = False
        self.last_position_placed = None
        self.last_value_placed = None
        self.won = False
        self.draw = False
        self.grid = [["F"],["O"],["O"]]

    def set_cell(self, value, pos):
        self.set_cell_called = True
        self.last_position_placed = pos
        self.last_value_placed = value

    def has_won(self):
        return self.won

    def has_draw(self):
        return self.draw

class TestGame:
    def setup_method(self, method):
        self.game = Game(GridSpy())

    def play_move(self, move):
        self.game.move(move)

    def set_game_won(self, has_won):
        self.game.grid.won = has_won

    def assert_current_player(self, expected_player):
        assert self.game.player == expected_player

    def assert_status(self, expected_status):
        assert self.game.status() == expected_status

    def assert_winner(self, expected_winner):
        assert self.game.winner() == expected_winner

    def test_starts_with_player_X(self):
        self.assert_current_player('X')

    def test_player_changed_after_making_a_move(self):
        self.play_move((1, 1))
        self.assert_current_player('O')

    def test_alternating_between_players(self):
        self.play_move((1, 1))
        self.play_move((1, 2))
        self.assert_current_player('X')

    def test_given_move_game_calls_set_cell(self):
        self.play_move((1, 1))
        assert self.game.grid.last_value_placed == 'X'
        assert self.game.grid.set_cell_called

    def test_make_a_move_at_pos(self):
        self.play_move((1, 1))
        assert self.game.grid.last_position_placed == (1, 1)

    def test_winner_returns_none_when_not_won(self):
        self.assert_winner(None)

    def test_winner_returns_next_player_when_won(self):
        self.set_game_won(True)
        self.assert_winner('O')

    def test_status_when_player_is_x(self):
        self.assert_status("Move of player X")

    def test_status_when_player_is_o(self):
        self.play_move((1,1))
        self.assert_status("Move of player O")

    def test_status_when_player_x_won(self):
        self.set_game_won(True)
        self.play_move((1,1))
        self.assert_status("  Player X won!  ")

    def test_status_when_player_o_won(self):
        self.set_game_won(True)
        self.assert_status("  Player O won!  ")

    def test_status_when_player_draw(self):
        self.game.grid.draw = True
        self.assert_status("       Draw       ")

    def test_to_dict(self):
        game_data = self.game.to_dict()
        assert game_data == {'disable_ai': True, 'grid': [['F'], ['O'], ['O']], 'player': 'X'}
