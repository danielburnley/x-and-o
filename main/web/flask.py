from main.game import Game
from main.grid import Grid
from main.player import Player
from flask import Flask, render_template, redirect, url_for
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('/tmp/tictactoe.json')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/game/new")
def new():
    players = [Player('One', ['X']), Player('Two', ['O'])]
    game = Game(Grid(), players)
    game.disable_ai = False
    id = db.insert(game.to_dict())
    return redirect("/game/" + str(id))

@app.route("/game/new/<size>")
def new_with_size(size):
    players = [Player('One', ['X']), Player('Two', ['O'])]
    game = Game(Grid(size=int(size)), players)
    game.disable_ai = True
    id = db.insert(game.to_dict())
    return redirect("/game/" + str(id))

@app.route("/game/new/twoplayer")
def new_two_player():
    players = [Player('One', ['X']), Player('Two', ['O'])]
    game = Game(Grid(), players)
    id = db.insert(game.to_dict())
    return redirect("/game/" + str(id))

@app.route("/game/<id>")
def game(id):
    game_data = db.get(doc_id=int(id))
    game = Game(Grid(), [None])
    game.restore(game_data)
    return render_template('game.html', game = game, id=id)

@app.route("/game/<id>/move/<row>/<col>")
def move(id, row, col):
    game_data = db.get(doc_id=int(id))
    game = Game(Grid(), [None])
    game.restore(game_data)
    if not game.winner():
        game.move((int(row),int(col)))
        db.update(game.to_dict(), doc_ids=[int(id)])
    return redirect("/game/" + str(id))

@app.route("/sos/new")
def new_sos():
    players = [Player('One', ['S', 'O']), Player('Two', ['S', 'O'])]
    game = Game(Grid(), players)
    game.disable_ai = True
    id = db.insert(game.to_dict())
    return redirect("/sos/" + str(id) + "/0")

@app.route("/sos/<id>/")
def sos(id):
    game_data = db.get(doc_id=int(id))
    game = Game(Grid(), [None])
    game.restore(game_data)
    return redirect("/sos/" + str(id)) + "/0"

@app.route("/sos/<id>/<symbol>")
def sos_with_symbol(id, symbol):
    game_data = db.get(doc_id=int(id))
    game = Game(Grid(), [None])
    game.restore(game_data)
    return render_template('sos.html', game=game, id=id, symbol=int(symbol))

@app.route("/sos/<id>/<symbol>/move/<row>/<col>")
def sos_move(id, symbol, row, col):
    game_data = db.get(doc_id=int(id))
    game = Game(Grid(), [None])
    game.restore(game_data)
    if not game.winner():
        player_symbol = game.player.symbols[int(symbol)]
        game.move((int(row),int(col)), player_symbol)
        db.update(game.to_dict(), doc_ids=[int(id)])
    return redirect("/sos/" + str(id) + "/0")
