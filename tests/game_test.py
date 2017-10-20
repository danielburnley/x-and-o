from main.game import Game

class GridSpy:
    def __init__(self):
        self.set_cell_called = False
        self.pos = None
        self.player = None
        self.won = False
        self.draw = False
        self.grid = [["F"],["O"],["O"]]

    def set_cell(self, value, pos):
        self.set_cell_called = True
        self.pos = pos
        self.player = value

    def has_won(self):
        return self.won

    def has_draw(self):
        return self.draw

class TestGame:
    def test_starts_with_player_X(self):
        assert Game(GridSpy()).player == 'X'

    def test_player_changed_after_making_a_move(self):
        game = Game(GridSpy())
        game.move((1, 1))
        assert game.player == 'O'

    def test_alternating_between_players(self):
        game = Game(GridSpy())
        game.move((1, 1))
        game.move((1, 2))
        assert game.player == 'X'

    def test_given_move_game_calls_set_cell(self):
        game = Game(GridSpy())
        game.move((1, 1))
        assert game.grid.player == 'X'
        assert game.grid.set_cell_called

    def test_make_a_move_at_pos(self):
        game = Game(GridSpy())
        game.move((1, 1))
        assert game.grid.pos == (1, 1)

    def test_winner_returns_none_when_not_won(self):
        game = Game(GridSpy())
        assert game.winner() == None

    def test_winner_returns_next_player_when_won(self):
        grid = GridSpy()
        grid.won = True
        game = Game(grid)
        assert game.winner() == 'O'

    def test_status_when_player_is_x(self):
        assert Game(GridSpy()).status() == "Move of player X"

    def test_status_when_player_is_o(self):
        game = Game(GridSpy())
        game.move((1,1))
        assert game.status() == "Move of player O"

    def test_status_when_player_x_won(self):
        grid = GridSpy()
        grid.won = True
        game = Game(grid)
        game.move((1,1))
        assert game.status() == "  Player X won!  "

    def test_status_when_player_o_won(self):
        grid = GridSpy()
        grid.won = True
        game = Game(grid)
        assert game.status() == "  Player O won!  "

    def test_status_when_player_draw(self):
        grid = GridSpy()
        grid.draw = True
        game = Game(grid)
        assert game.status() == "       Draw       "

    def test_to_dict(self):
        game = Game(GridSpy())
        game_data = game.to_dict()
        assert game_data == {'disable_ai': True, 'grid': [['F'], ['O'], ['O']], 'player': 'X'}
