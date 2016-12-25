from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    board = Gameboard().board
    return render_template('index.html', board=board)
