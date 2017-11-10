from main.player import Player

class TestPlayer:
    def setup_method(self, method):
        self.player = Player('Test name', ['x'])

    def test_player_to_string_prints_player_name(self):
        assert str(self.player) == 'Test name'

    def test_player_symbol_returns_symbol(self):
        assert self.player.symbols == ['x']

    def test_to_dict(self):
        assert self.player.to_dict() == { 'name': 'Test name', 'symbols': ['x'] }

    def test_equality(self):
        other = Player('Test name', ['x'])
        assert self.player == other
