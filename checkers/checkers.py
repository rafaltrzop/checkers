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
        gameboard = Gameboard()

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
