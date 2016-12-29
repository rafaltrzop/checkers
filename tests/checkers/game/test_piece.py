from checkers.game import *

def test_ligth_piece_color():
    light_piece = LightPiece()
    assert light_piece.color == COLOR_LIGHT

def test_dark_piece_color():
    dark_piece = DarkPiece()
    assert dark_piece.color == COLOR_DARK

def test_ligth_piece_is_kind_of_piece():
    assert issubclass(LightPiece, Piece)

def test_dark_piece_is_kind_of_piece():
    assert issubclass(DarkPiece, Piece)

def test_piece_is_not_a_king():
    dark_piece = DarkPiece()
    light_piece = LightPiece()
    assert dark_piece.king == False
    assert light_piece.king == False

def test_piece_becomes_king():
    dark_piece = DarkPiece()
    light_piece = LightPiece()
    dark_piece.become_king()
    light_piece.become_king()
    assert dark_piece.king == True
    assert light_piece.king == True
