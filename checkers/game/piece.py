class Piece:
    def __init__(self, color, king=False):
        self.color = color
        self.king = king

class LightPiece(Piece):
    def __init__(self, color='light', king=False):
        super().__init__(color, king)

class DarkPiece(Piece):
    def __init__(self, color='dark', king=False):
        super().__init__(color, king)
