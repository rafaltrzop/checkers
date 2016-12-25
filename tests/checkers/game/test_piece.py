from checkers.game import *

def test_ligth_piece_color():
    piece = LightPiece()
    assert piece.color == 'light'

def test_dark_piece_color():
    piece = DarkPiece()
    assert piece.color == 'dark'

def test_ligth_piece_is_kind_of_piece():
    assert issubclass(LightPiece, Piece)

def test_dark_piece_is_kind_of_piece():
    assert issubclass(DarkPiece, Piece)

def test_piece_is_not_a_king():
    piece = Piece('color')
    assert piece.king == False

