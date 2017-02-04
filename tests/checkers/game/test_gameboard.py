import pytest
from checkers.game import *

def test_cannot_init_gameboard_with_piece_on_white_square():
    piece = DarkPiece()
    board = [
        [piece, None],
        [None, None],
    ]
    with pytest.raises(ValueError) as excinfo:
        Gameboard(board)
    assert 'cannot set piece on white square' in str(excinfo.value)

def test_cannot_init_gameboard_with_non_square_board():
    board = [
        [None, None, None],
        [None, None],
        [None, None]
    ]
    with pytest.raises(ValueError) as excinfo:
        Gameboard(board)
    assert 'cannot use non square board' in str(excinfo.value)

def test_cannot_move_piece_to_white_square():
    piece = DarkPiece()
    board = [
        [None, piece],
        [None, None],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 1, 'y': 0}
    destination = {'x': 1, 'y': 1}
    move = gameboard.move(current_position, destination)
    assert move.result == False
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
    move = gameboard.move(current_position, destination)
    assert move.result == True
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
    move = gameboard.move(current_position, destination)
    assert move.result == False
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
    move = gameboard.move(current_position, destination)
    assert move.result == True
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
    move = gameboard.move(current_position, destination)
    assert move.result == False
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
    move = gameboard.move(current_position, destination)
    assert move.result == False
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
    move = gameboard.move(current_position, destination)
    assert move.result == False
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
    move = gameboard.move(current_position, destination)
    assert move.result == False
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
    move = gameboard.move(current_position, destination)
    assert move.result == False
    assert gameboard.board == board

def test_dark_piece_captures_light_piece():
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
    move = gameboard.move(current_position, destination)
    assert move.result == True
    assert gameboard.board == [
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, dark_piece],
        [None, None, None, None]
    ]

def test_light_piece_captures_dark_piece():
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
    move = gameboard.move(current_position, destination)
    assert move.result == True
    assert gameboard.board == [
        [None, None, None, None],
        [None, None, light_piece, None],
        [None, None, None, None],
        [None, None, None, None]
    ]

def test_dark_piece_becomes_king():
    dark_piece = DarkPiece()
    board = [
        [None, dark_piece],
        [None, None],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 1, 'y': 0}
    destination = {'x': 0, 'y': 1}
    gameboard.move(current_position, destination)
    assert dark_piece.king == True

def test_light_piece_becomes_king():
    light_piece = LightPiece()
    board = [
        [None, None],
        [light_piece, None],
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 0, 'y': 1}
    destination = {'x': 1, 'y': 0}
    gameboard.move(current_position, destination)
    assert light_piece.king == True

def test_build_custom_size_board():
    board_size = 4
    gameboard = Gameboard.build(board_size)

    assert len(gameboard.board) == board_size

    assert gameboard.board[0][0] == None
    assert type(gameboard.board[0][1]) is DarkPiece
    assert gameboard.board[0][2] == None
    assert type(gameboard.board[0][3]) is DarkPiece

    assert gameboard.board[1][0] == None
    assert gameboard.board[1][1] == None
    assert gameboard.board[1][2] == None
    assert gameboard.board[1][3] == None

    assert gameboard.board[2][0] == None
    assert gameboard.board[2][1] == None
    assert gameboard.board[2][2] == None
    assert gameboard.board[2][3] == None

    assert type(gameboard.board[3][0]) is LightPiece
    assert gameboard.board[3][1] == None
    assert type(gameboard.board[3][2]) is LightPiece
    assert gameboard.board[3][3] == None

def test_king_can_jump_multiple_squares():
    piece = DarkPiece()
    piece.become_king()
    board = [
        [None, None, None, piece, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None]
    ]
    gameboard = Gameboard(board)

    current_position = {'x': 3, 'y': 0}
    destination = {'x': 0, 'y': 3}
    gameboard.move(current_position, destination)
    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [piece, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None]
    ]
    assert gameboard.board == board

    current_position = destination
    destination = {'x': 3, 'y': 6}
    gameboard = Gameboard(board)
    gameboard.move(current_position, destination)
    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, piece, None, None, None]
    ]
    assert gameboard.board == board

    current_position = destination
    destination = {'x': 6, 'y': 3}
    gameboard = Gameboard(board)
    gameboard.move(current_position, destination)
    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, piece],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None]
    ]
    assert gameboard.board == board

    current_position = destination
    destination = {'x': 3, 'y': 0}
    gameboard = Gameboard(board)
    gameboard.move(current_position, destination)
    board = [
        [None, None, None, piece, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None]
    ]
    assert gameboard.board == board

def test_king_cannot_capture_piece_of_the_same_color():
    piece1 = DarkPiece()
    piece1.become_king()
    piece2 = DarkPiece()
    board = [
        [None, piece1, None, None],
        [None, None, piece2, None],
        [None, None, None, None],
        [None, None, None, None]
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 1, 'y': 0}
    destination = {'x': 3, 'y': 2}
    move = gameboard.move(current_position, destination)
    assert move.result == False
    assert gameboard.board == board

def test_king_captures_opponent():
    light_piece = LightPiece()
    light_piece.become_king()
    dark_piece = DarkPiece()
    board = [
        [None, light_piece, None, None, None],
        [None, None, dark_piece, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None]
    ]
    gameboard = Gameboard(board)
    current_position = {'x': 1, 'y': 0}
    destination = {'x': 4, 'y': 3}
    move = gameboard.move(current_position, destination)
    assert move.result == True
    assert gameboard.board == [
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, light_piece],
        [None, None, None, None, None]
    ]

def test_piece_cannot_move_twice():
        piece = DarkPiece()
        board = [
            [None, piece, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None]
        ]
        gameboard = Gameboard(board)

        current_position = {'x': 1, 'y': 0}
        destination = {'x': 2, 'y': 1}
        move = gameboard.move(current_position, destination)
        assert move.result == True
        assert gameboard.board == [
            [None, None, None, None],
            [None, None, piece, None],
            [None, None, None, None],
            [None, None, None, None]
        ]

        current_position = destination
        destination = {'x': 1, 'y': 2}
        move = gameboard.move(current_position, destination)
        assert move.result == False
        assert gameboard.board == [
            [None, None, None, None],
            [None, None, piece, None],
            [None, None, None, None],
            [None, None, None, None]
        ]
