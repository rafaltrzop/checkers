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
    destination = {'x': 1, 'y': 1}
    result = gameboard.move(current_position, destination)
    assert result == False
    assert gameboard.board == board

def test_move_dark_piece_down():
    dark_piece = DarkPiece()
    board = [
        [None, dark_piece],
        [None, None],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 1, 'y': 0}
    destination = {'x': 0, 'y': 1}
    result = gameboard.move(current_position, destination)
    assert result == True
    assert gameboard.board == [
        [None, None],
        [dark_piece, None],
    ]

def test_cannot_move_dark_piece_up():
    dark_piece = DarkPiece()
    board = [
        [None, None],
        [dark_piece, None],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 0, 'y': 1}
    destination = {'x': 1, 'y': 0}
    result = gameboard.move(current_position, destination)
    assert result == False
    assert gameboard.board == board

def test_move_light_piece_up():
    light_piece = LightPiece()
    board = [
        [None, None],
        [light_piece, None],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 0, 'y': 1}
    destination = {'x': 1, 'y': 0}
    result = gameboard.move(current_position, destination)
    assert result == True
    assert gameboard.board == [
        [None, light_piece],
        [None, None],
    ]

def test_cannot_move_light_piece_down():
    light_piece = LightPiece()
    board = [
        [None, light_piece],
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

def test_cannot_move_piece_further_than_one_square():
    piece = DarkPiece()
    board = [
        [None, piece, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None]
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 1, 'y': 0}
    destination = {'x': 3, 'y': 2}
    result = gameboard.move(current_position, destination)
    assert result == False
    assert gameboard.board == board

def test_cannot_move_piece_outside_board():
    piece = DarkPiece()
    board = [
        [None, piece],
        [None, None],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 1, 'y': 0}
    destination = {'x': 2, 'y': -1}
    result = gameboard.move(current_position, destination)
    assert result == False
    assert gameboard.board == board

def test_dark_piece_can_capture_light_piece():
    dark_piece = DarkPiece()
    light_piece = LightPiece()
    board = [
        [None, dark_piece, None, None],
        [None, None, light_piece, None],
        [None, None, None, None],
        [None, None, None, None]
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 1, 'y': 0}
    destination = {'x': 3, 'y': 2}
    result = gameboard.move(current_position, destination)
    assert result == True
    assert gameboard.board == [
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, dark_piece],
        [None, None, None, None]
    ]

def test_light_piece_can_capture_dark_piece():
    dark_piece = DarkPiece()
    light_piece = LightPiece()
    board = [
        [None, None, None, None],
        [None, None, None, None],
        [None, dark_piece, None, None],
        [light_piece, None, None, None]
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 0, 'y': 3}
    destination = {'x': 2, 'y': 1}
    result = gameboard.move(current_position, destination)
    assert result == True
    assert gameboard.board == [
        [None, None, None, None],
        [None, None, light_piece, None],
        [None, None, None, None],
        [None, None, None, None]
    ]
