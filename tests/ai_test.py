from main.ai import AI
from main.game import Game
from main.grid import Grid

class TestAI:
    def get_new_game(self, grid, player='X'):
        game = Game(Grid())
        game.grid.grid = grid
        game.player = player
        return game

    def get_ai_for_game(self, game, player):
        return AI(game, player)

    def assert_score(self, ai, game, expected_score):
        assert ai.score(game) == expected_score

    def assert_number_of_possible_moves(self, ai, game, expected_number_of_moves):
        assert len(ai.get_possible_moves(game)) == expected_number_of_moves

    def assert_minmax_score(self, ai, game, expected_score):
        assert ai.minmax(game) == expected_score

    def assert_next_move(self, ai, expected_move):
        assert ai.get_next_move() == expected_move

    def test_score_when_AI_has_not_won(self):
        game = self.get_new_game([["O","O","O"],[" ", " ", " "],[" ", " ", " "]])
        ai = self.get_ai_for_game(game, "X")
        self.assert_score(ai, game, -10)

    def test_score_when_AI_has_won(self):
        game = self.get_new_game([["O","O","O"],[" ", " ", " "],[" ", " ", " "]])
        ai = self.get_ai_for_game(game, "O")
        self.assert_score(ai, game, 10)

    def test_score_when_everyone_lose(self):
        game = self.get_new_game([["O","X","O"],[" ", " ", " "],[" ", " ", " "]])
        ai = self.get_ai_for_game(game, "O")
        self.assert_score(ai, game, 0)

    def test_get_possible_moves_when_only_one_move(self):
        game = self.get_new_game([["O","X","O"],["X", " ", "X"],["X", "O", "X"]], 'O')
        ai = self.get_ai_for_game(game, "O")
        self.assert_number_of_possible_moves(ai, game, 1)
        assert ai.get_possible_moves(game)[0].grid.grid == [["O", "X", "O"], ["X", "O", "X"], ["X", "O", "X"]]

    def test_get_possible_moves_when_only_one_move(self):
        game = self.get_new_game([["O"," ","O"],["X", " ", "X"],["X", " ", "X"]], "O")
        ai = self.get_ai_for_game(game, "O")
        self.assert_number_of_possible_moves(ai, game, 3)

    def test_get_possible_moves_when_only_one_move(self):
        game = self.get_new_game([["O","X","O"],["X", "O", "X"],["X", "O", "X"]], "O")
        ai = self.get_ai_for_game(game, "O")
        self.assert_number_of_possible_moves(ai, game, 0)

    def test_returns_score_for_draw(self):
        game = self.get_new_game([["O","X","O"],["X", "O", "X"],["X", "O", "X"]], "O")
        ai = self.get_ai_for_game(game, "O")
        self.assert_minmax_score(ai, game, 0)

    def test_returns_score_for_AI_won(self):
        game = self.get_new_game([["O","O","O"],["X", "O", "X"],["X", "O", "X"]])
        ai = self.get_ai_for_game(game, "O")
        self.assert_minmax_score(ai, game, 10)

    def test_returns_score_for_AI_lose(self):
        game = self.get_new_game([["O","X","O"],["X", "X", "X"],["X", "X", "X"]], "O")
        ai = self.get_ai_for_game(game, "O")
        self.assert_minmax_score(ai, game, -10)

    def test_next_move(self):
        game = self.get_new_game([["O","X","O"],["X", " ", "X"],["X", "O", "X"]], "O")
        ai = self.get_ai_for_game(game, "O")
        self.assert_next_move(ai, (1, 1))

    def test_next_move_with_one_losing_move(self):
        game = self.get_new_game([[" ","X","O"],["X","X","O"],["X","O"," "]], "O")
        ai = self.get_ai_for_game(game, "O")
        self.assert_next_move(ai, (2, 2))

    def test_given_first_go_with_player_in_center(self):
        game = self.get_new_game([[" "," "," "],[" ","X"," "],[" "," "," "]], "O")
        ai = self.get_ai_for_game(game, "O")
        self.assert_next_move(ai, (0, 0))

    def test_given_first_go_with_player_not_in_center(self):
        game = self.get_new_game([["X"," "," "],[" "," "," "],[" "," "," "]], "O")
        ai = self.get_ai_for_game(game, "O")
        self.assert_next_move(ai, (1, 1))
