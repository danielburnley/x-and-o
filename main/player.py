class Player:
    def __init__(self, name, symbols):
        self.name = name
        self.symbols = symbols

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'name': self.name,
            'symbols': self.symbols,
        }
