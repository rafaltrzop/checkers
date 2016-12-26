from checkers.game import *

def test_cannot_move_piece_to_white_square():
    piece = DarkPiece()
    board = [
        [WHITE_SQUARE, piece],
        [BLACK_SQUARE, WHITE_SQUARE],
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
        [WHITE_SQUARE, piece],
        [BLACK_SQUARE, WHITE_SQUARE],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 1, 'y': 0}
    destination = {'x': 0, 'y': 1}
    result = gameboard.move(current_position, destination)
    assert result == True
    assert gameboard.board == [
        [WHITE_SQUARE, BLACK_SQUARE],
        [piece, WHITE_SQUARE],
    ]

def test_cannot_move_dark_piece_up():
    piece = DarkPiece()
    board = [
        [WHITE_SQUARE, BLACK_SQUARE],
        [piece, WHITE_SQUARE],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 0, 'y': 1}
    destination = {'x': 1, 'y': 0}
    result = gameboard.move(current_position, destination)
    assert result == False
    assert gameboard.board == [
        [WHITE_SQUARE, BLACK_SQUARE],
        [piece, WHITE_SQUARE],
    ]

def test_move_light_piece_up():
    piece = LightPiece()
    board = [
        [WHITE_SQUARE, BLACK_SQUARE],
        [piece, WHITE_SQUARE],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 0, 'y': 1}
    destination = {'x': 1, 'y': 0}
    result = gameboard.move(current_position, destination)
    assert result == True
    assert gameboard.board == [
        [WHITE_SQUARE, piece],
        [BLACK_SQUARE, WHITE_SQUARE],
    ]

def test_cannot_move_light_piece_down():
    piece = LightPiece()
    board = [
        [WHITE_SQUARE, piece],
        [BLACK_SQUARE, WHITE_SQUARE],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 1, 'y': 0}
    destination = {'x': 0, 'y': 1}
    result = gameboard.move(current_position, destination)
    assert result == False
    assert gameboard.board == [
        [WHITE_SQUARE, piece],
        [BLACK_SQUARE, WHITE_SQUARE],
    ]
