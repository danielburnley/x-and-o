from main.ai import AI
from main.game import Game
from main.grid import Grid

class TestAI:
    def test_score_when_AI_has_not_won(self):
        game = Game(Grid())
        game.grid.grid = [["O","O","O"],[" ", " ", " "],[" ", " ", " "]]
        ai = AI(game=game, player="X")
        assert ai.score(game) == -10

    def test_score_when_AI_has_won(self):
        game = Game(Grid())
        game.grid.grid = [["O","O","O"],[" ", " ", " "],[" ", " ", " "]]
        ai = AI(game=game, player="O")
        assert ai.score(game) == 10

    def test_score_when_everyone_lose(self):
        game = Game(Grid())
        game.grid.grid = [["O","X","O"],[" ", " ", " "],[" ", " ", " "]]
        ai = AI(game=game, player="O")
        assert ai.score(game) == 0

    def test_get_possible_moves_when_only_one_move(self):
        game = Game(Grid())
        game.grid.grid = [["O","X","O"],["X", " ", "X"],["X", "O", "X"]]
        game.player = "O"
        ai = AI(game=game, player="O")
        assert len(ai.get_possible_moves(game)) == 1
        assert ai.get_possible_moves(game)[0].grid.grid == [["O", "X", "O"], ["X", "O", "X"], ["X", "O", "X"]]

    def test_get_possible_moves_when_only_one_move(self):
        game = Game(Grid())
        game.grid.grid = [["O"," ","O"],["X", " ", "X"],["X", " ", "X"]]
        game.player = "O"
        ai = AI(game=game, player="O")
        assert len(ai.get_possible_moves(game)) == 3

    def test_get_possible_moves_when_only_one_move(self):
        game = Game(Grid())
        game.grid.grid = [["O","X","O"],["X", "O", "X"],["X", "O", "X"]]
        game.player = "O"
        ai = AI(game=game, player="O")
        assert len(ai.get_possible_moves(game)) == 0

    def test_returns_score_for_draw(self):
        game = Game(Grid())
        game.grid.grid = [["O","X","O"],["X", "O", "X"],["X", "O", "X"]]
        game.player = "O"
        ai = AI(game=game, player="O")
        assert ai.minmax(game) == 0

    def test_returns_score_for_AI_won(self):
        game = Game(Grid())
        game.grid.grid = [["O","O","O"],["X", "O", "X"],["X", "O", "X"]]
        game.player = "X"
        ai = AI(game=game, player="O")
        assert ai.minmax(game) == 10

    def test_returns_score_for_AI_lose(self):
        game = Game(Grid())
        game.grid.grid = [["O","X","O"],["X", "X", "X"],["X", "X", "X"]]
        game.player = "O"
        ai = AI(game=game, player="O")
        assert ai.minmax(game) == -10

    def test_next_move(self):
        game = Game(Grid())
        game.grid.grid = [["O","X","O"],["X", " ", "X"],["X", "O", "X"]]
        game.player = "O"
        ai = AI(game=game, player="O")
        assert ai.get_next_move() == (1, 1)

    def test_next_move_with_one_losing_move(self):
        game = Game(Grid())
        game.grid.grid = [
            [" ","X","O"],
            ["X","X","O"],
            ["X","O"," "]]
        game.player = "O"
        ai = AI(game=game, player="O")
        assert ai.get_next_move() == (2, 2)

    def test_given_first_go_with_player_in_center(self):
        game = Game(Grid())
        game.grid.grid = [
            [" "," "," "],
            [" ","X"," "],
            [" "," "," "]]
        game.player = "O"
        ai = AI(game=game, player="O")
        assert ai.get_next_move() == (0, 0)

    def test_given_first_go_with_player_not_in_center(self):
        game = Game(Grid())
        game.grid.grid = [
            ["X"," "," "],
            [" "," "," "],
            [" "," "," "]]
        game.player = "O"
        ai = AI(game=game, player="O")
        assert ai.get_next_move() == (1, 1)
