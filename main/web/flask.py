from main.game import Game
from main.grid import Grid
from main.game_state import GameState
from flask import Flask, render_template, redirect, url_for
from tinydb import TinyDB, Query
DISABLE_AI = False

app = Flask(__name__)
db = TinyDB('/tmp/tictactoe.json')

@app.route("/")
def index():
    return render_template('index.html', game = game)

@app.route("/game/new")
def new():
    game = Game(Grid())
    id = db.insert({'grid': game.grid.grid, 'player': game.player, 'disable_ai': DISABLE_AI})
    return redirect("/game/" + str(id))

@app.route("/game/new/twoplayer")
def new_two_player():
    game = Game(Grid())
    id = db.insert({'grid': game.grid.grid, 'player': game.player, 'disable_ai': True})
    return redirect("/game/" + str(id))

@app.route("/game/<id>")
def game(id):
    game_data = db.get(doc_id=int(id))
    game = Game(Grid())
    game.grid.grid = game_data['grid']
    game.player = game_data['player']
    game.disable_ai = game_data['disable_ai']
    return render_template('game.html', game = game, id=id)

@app.route("/game/<id>/move/<row>/<col>")
def move(id, row, col):
    query = Query()
    game_data = db.get(doc_id=int(id))
    game = Game(Grid())
    game.grid.grid = game_data['grid']
    game.player = game_data['player']
    game.disable_ai = game_data['disable_ai']
    game.move((int(row),int(col)))
    db.update({'grid': game.grid.grid, 'player': game.player, 'disable_ai': game.disable_ai}, doc_ids=[int(id)])
    return redirect("/game/" + str(id))
