from main.game import Game
from main.grid import Grid
from flask import Flask, render_template, redirect, url_for
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('/tmp/tictactoe.json')

@app.route("/")
def index():
    return render_template('index.html', game = game)

@app.route("/game/new")
def new():
    game = Game(Grid())
    game.disable_ai = False
    id = db.insert(game.to_dict())
    return redirect("/game/" + str(id))

@app.route("/game/new/twoplayer")
def new_two_player():
    game = Game(Grid())
    id = db.insert(game.to_dict())
    return redirect("/game/" + str(id))

@app.route("/game/<id>")
def game(id):
    game_data = db.get(doc_id=int(id))
    game = Game(Grid())
    game.restore(game_data)
    return render_template('game.html', game = game, id=id)

@app.route("/game/<id>/move/<row>/<col>")
def move(id, row, col):
    game_data = db.get(doc_id=int(id))
    game = Game(Grid())
    game.restore(game_data)
    if not game.winner():
        game.move((int(row),int(col)))
        db.update(game.to_dict(), doc_ids=[int(id)])
    return redirect("/game/" + str(id))
