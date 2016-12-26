from .piece import *
from copy import deepcopy

DEFAULT_BOARD = [
    [None, DarkPiece(), None, DarkPiece(), None, DarkPiece(), None, DarkPiece()],
    [DarkPiece(), None, DarkPiece(), None, DarkPiece(), None, DarkPiece(), None],
    [None, DarkPiece(), None, DarkPiece(), None, DarkPiece(), None, DarkPiece()],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [LightPiece(), None, LightPiece(), None, LightPiece(), None, LightPiece(), None],
    [None, LightPiece(), None, LightPiece(), None, LightPiece(), None, LightPiece()],
    [LightPiece(), None, LightPiece(), None, LightPiece(), None, LightPiece(), None]
]

class Gameboard:
    def __init__(self, board=None):
        if board == None:
            board = deepcopy(DEFAULT_BOARD)

        self.board = self.__ensure_valid_board(board)

    def move(self, current_position, destination):
        cur_x = current_position['x']
        cur_y = current_position['y']
        dst_x = destination['x']
        dst_y = destination['y']

        piece = self.board[cur_y][cur_x]
        dst = self.board[dst_y][dst_x]
        dst_is_legal_square = self.__is_legal_square(dst_x, dst_y)
        moving_down = cur_y < dst_y
        moving_up = cur_y > dst_y

        if dst_is_legal_square and type(dst) not in (LightPiece, DarkPiece) and ((piece.color == COLOR_DARK and moving_down) or (piece.color == COLOR_LIGHT and moving_up)):
            self.board[cur_y][cur_x], self.board[dst_y][dst_x] = self.board[dst_y][dst_x], self.board[cur_y][cur_x]
            return True
        else:
            return False

    def __ensure_valid_board(self, board):
        y = 0
        x = 0

        for row in board:
            for square in row:
                if type(square) in (LightPiece, DarkPiece):
                    legal_square = self.__is_legal_square(x, y)
                    if not legal_square:
                        raise ValueError('cannot set piece on white square')
                x += 1
            y += 1
            x = 0

        return board

    def __is_legal_square(self, x, y):
        return (y % 2 == 0 and x % 2 == 1) or (y % 2 == 1 and x % 2 == 0)
