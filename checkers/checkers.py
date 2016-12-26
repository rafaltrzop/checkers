from flask import Flask
from flask import render_template
from .game import *

app = Flask(__name__)

@app.route('/')
def index():
    default_board = [
        [WHITE_SQUARE, DarkPiece(), WHITE_SQUARE, DarkPiece(), WHITE_SQUARE, DarkPiece(), WHITE_SQUARE, DarkPiece()],
        [DarkPiece(), WHITE_SQUARE, DarkPiece(), WHITE_SQUARE, DarkPiece(), WHITE_SQUARE, DarkPiece(), WHITE_SQUARE],
        [WHITE_SQUARE, DarkPiece(), WHITE_SQUARE, DarkPiece(), WHITE_SQUARE, DarkPiece(), WHITE_SQUARE, DarkPiece()],
        [BLACK_SQUARE, WHITE_SQUARE, BLACK_SQUARE, WHITE_SQUARE, BLACK_SQUARE, WHITE_SQUARE, BLACK_SQUARE, WHITE_SQUARE],
        [WHITE_SQUARE, BLACK_SQUARE, WHITE_SQUARE, BLACK_SQUARE, WHITE_SQUARE, BLACK_SQUARE, WHITE_SQUARE, BLACK_SQUARE],
        [LightPiece(), WHITE_SQUARE, LightPiece(), WHITE_SQUARE, LightPiece(), WHITE_SQUARE, LightPiece(), WHITE_SQUARE],
        [WHITE_SQUARE, LightPiece(), WHITE_SQUARE, LightPiece(), WHITE_SQUARE, LightPiece(), WHITE_SQUARE, LightPiece()],
        [LightPiece(), WHITE_SQUARE, LightPiece(), WHITE_SQUARE, LightPiece(), WHITE_SQUARE, LightPiece(), WHITE_SQUARE]
    ]
    board = Gameboard(default_board).board
    return render_template('index.html', board=board)
