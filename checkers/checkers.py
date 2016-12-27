from flask import Flask
from flask import render_template
from flask import request
from .game import *

app = Flask(__name__)

@app.route('/')
def index():
    gameboard = Gameboard()
    board = gameboard.board
    return render_template('index.html', board=board)

@app.route('/move', methods=['POST'])
def move():
    if request.method == 'POST':
        gameboard = Gameboard(__prepare_board(request))

        current_position = {
            'x': int(request.form['cur_x']),
            'y': int(request.form['cur_y'])
        }
        destination = {
            'x': int(request.form['dst_x']),
            'y': int(request.form['dst_y'])
        }
        gameboard.move(current_position, destination)

        board = gameboard.board
        return render_template('_gameboard.html', board=board)

def __prepare_board(request):
    prepared_board = deepcopy(EMPTY_BOARD)
    board_size = int(request.form['board_size'])

    for i in range(board_size):
        x = int(request.form['board['+str(i)+'][x]'])
        y = int(request.form['board['+str(i)+'][y]'])
        color = request.form['board['+str(i)+'][color]']
        king = request.form['board['+str(i)+'][king]'] == 'true'

        if color == 'DarkPiece':
            prepared_piece = DarkPiece()
        if color == 'LightPiece':
            prepared_piece = LightPiece()
        if king:
            prepared_piece.become_king()
        prepared_board[y][x] = prepared_piece

    return prepared_board
