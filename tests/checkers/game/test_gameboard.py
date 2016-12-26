import pytest
from checkers.game import *

def test_cannot_init_board_with_piece_on_white_square():
    piece = DarkPiece()
    board = [
        [piece, None],
        [None, None],
    ]
    with pytest.raises(ValueError) as excinfo:
        Gameboard(board)
    assert 'cannot set piece on white square' in str(excinfo.value)

def test_cannot_move_piece_to_white_square():
    piece = DarkPiece()
    board = [
        [None, piece],
        [None, None],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 1, 'y': 0}
    destination = {'x': 0, 'y': 0}
    result = gameboard.move(current_position, destination)
    assert result == False
    assert gameboard.board == board

def test_move_dark_piece_down():
    piece = DarkPiece()
    board = [
        [None, piece],
        [None, None],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 1, 'y': 0}
    destination = {'x': 0, 'y': 1}
    result = gameboard.move(current_position, destination)
    assert result == True
    assert gameboard.board == [
        [None, None],
        [piece, None],
    ]

def test_cannot_move_dark_piece_up():
    piece = DarkPiece()
    board = [
        [None, None],
        [piece, None],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 0, 'y': 1}
    destination = {'x': 1, 'y': 0}
    result = gameboard.move(current_position, destination)
    assert result == False
    assert gameboard.board == board

def test_move_light_piece_up():
    piece = LightPiece()
    board = [
        [None, None],
        [piece, None],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 0, 'y': 1}
    destination = {'x': 1, 'y': 0}
    result = gameboard.move(current_position, destination)
    assert result == True
    assert gameboard.board == [
        [None, piece],
        [None, None],
    ]

def test_cannot_move_light_piece_down():
    piece = LightPiece()
    board = [
        [None, piece],
        [None, None],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 1, 'y': 0}
    destination = {'x': 0, 'y': 1}
    result = gameboard.move(current_position, destination)
    assert result == False
    assert gameboard.board == board

def test_cannot_move_light_piece_onto_dark_piece():
    light_piece = LightPiece()
    dark_piece = DarkPiece()
    board = [
        [None, dark_piece],
        [light_piece, None],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 0, 'y': 1}
    destination = {'x': 1, 'y': 0}
    result = gameboard.move(current_position, destination)
    assert result == False
    assert gameboard.board == board

def test_cannot_move_dark_piece_onto_ligth_piece():
    light_piece = LightPiece()
    dark_piece = DarkPiece()
    board = [
        [None, dark_piece],
        [light_piece, None],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 1, 'y': 0}
    destination = {'x': 0, 'y': 1}
    result = gameboard.move(current_position, destination)
    assert result == False
    assert gameboard.board == board
