from flask import Flask
from flask import render_template
from .game import *

app = Flask(__name__)

@app.route('/')
def index():
    default_board = [
        [None, DarkPiece(), None, DarkPiece(), None, DarkPiece(), None, DarkPiece()],
        [DarkPiece(), None, DarkPiece(), None, DarkPiece(), None, DarkPiece(), None],
        [None, DarkPiece(), None, DarkPiece(), None, DarkPiece(), None, DarkPiece()],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [LightPiece(), None, LightPiece(), None, LightPiece(), None, LightPiece(), None],
        [None, LightPiece(), None, LightPiece(), None, LightPiece(), None, LightPiece()],
        [LightPiece(), None, LightPiece(), None, LightPiece(), None, LightPiece(), None]
    ]
    board = Gameboard(default_board).board
    return render_template('index.html', board=board)
