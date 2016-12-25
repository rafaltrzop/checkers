from flask import Flask
from flask import render_template

app = Flask(__name__)

###############################################################################

DARK_PIECE = 'dark'
LIGHT_PIECE = 'light'

class Piece:
    def __init__(self, x, y, color, king=False):
        self.x = x
        self.y = y
        self.color = color
        self.king = king

    def become_king(self):
        self.king = True

class Gameboard:
    board = [
        [None, Piece(1, 0, DARK_PIECE, True), None, Piece(3, 0, DARK_PIECE), None, Piece(5, 0, DARK_PIECE), None, Piece(7, 0, DARK_PIECE)],
        [Piece(0, 1, DARK_PIECE), None, Piece(2, 1, DARK_PIECE), None, Piece(4, 1, DARK_PIECE), None, Piece(6, 1, DARK_PIECE), None],
        [None, Piece(1, 2, DARK_PIECE), None, Piece(3, 2, DARK_PIECE), None, Piece(5, 2, DARK_PIECE), None, Piece(7, 2, DARK_PIECE)],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [Piece(0, 5, LIGHT_PIECE), None, Piece(2, 5, LIGHT_PIECE), None, Piece(4, 5, LIGHT_PIECE), None, Piece(6, 5, LIGHT_PIECE), None],
        [None, Piece(1, 6, LIGHT_PIECE), None, Piece(3, 6, LIGHT_PIECE), None, Piece(5, 6, LIGHT_PIECE), None, Piece(7, 6, LIGHT_PIECE)],
        [Piece(0, 7, LIGHT_PIECE, True), None, Piece(2, 7, LIGHT_PIECE), None, Piece(4, 7, LIGHT_PIECE), None, Piece(6, 7, LIGHT_PIECE), None]
    ]

    def __init__(self, size=8):
        self.size = size
        # self.board = self.generate_board(size)

    # def move_piece():
    #     pass

###############################################################################

@app.route('/')
def index():
    board = Gameboard().board
    return render_template('index.html', board=board)
