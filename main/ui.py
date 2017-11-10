import functools
from tkinter import *
from grid import *
from game import *
from player import *

class UI():
    def __init__(self):
        self.root = Tk()
        self.players = [Player('One', ['X']), Player('Two', ['O'])]
        self.game = Game(Grid(), self.players)
        self.game.disable_ai = False
        self.main = Frame(self.root)
        self.bar = Frame(self.root)

    def run(self):
        self._add_grid()
        self._add_status()
        self.root.mainloop()

    def callback(self, event, row, col):
        if self.game.winner() or self.game.draw():
            return

        self.game.move((row, col))
        self.main.grid_forget()
        self.bar.grid_forget()

        self._add_grid()
        self._add_status()

    def _getStatusText(self):
        return self.game.status()

    def _add_status(self):
        label = Label(self.bar,
            text=self._getStatusText(),
            font=('Courier', 32),
            borderwidth=1,
        )
        label.grid(row=0)
        self.bar.grid(row=0)

    def _add_grid(self):
        for (r_index, row) in enumerate(self.game.grid.grid):
            for (c_index, col) in enumerate(row):
                label = Label(self.main,
                    relief="solid",
                    text=col,
                    font=('Courier', 200),
                    borderwidth=1,
                )
                label.bind("<Button-1>", functools.partial(self.callback, row=r_index, col=c_index))
                label.grid(row=r_index, column=c_index)

        self.main.grid(row=1)


if __name__ == '__main__':
    UI().run()
