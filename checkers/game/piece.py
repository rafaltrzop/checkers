class Piece:
    def __init__(self, color):
        self.color = color
        self.king = False

    def become_king(self):
        self.king = True

class LightPiece(Piece):
    def __init__(self, color='light'):
        super().__init__(color)

class DarkPiece(Piece):
    def __init__(self, color='dark'):
        super().__init__(color)
