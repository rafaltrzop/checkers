COLOR_LIGHT = 'light'
COLOR_DARK = 'dark'

class Piece:
    def __init__(self, color):
        self.color = color
        self.king = False

    def become_king(self):
        """Sets king flag to true."""
        
        self.king = True

class LightPiece(Piece):
    def __init__(self, color=COLOR_LIGHT):
        super().__init__(color)

class DarkPiece(Piece):
    def __init__(self, color=COLOR_DARK):
        super().__init__(color)
