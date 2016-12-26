from .piece import *

class Gameboard:
    def __init__(self, board):
        self.board = board

    def move(self, current_position, destination):
        cur_x = current_position['x']
        cur_y = current_position['y']
        dst_x = destination['x']
        dst_y = destination['y']

        piece = self.board[cur_y][cur_x]
        dst = self.board[dst_y][dst_x]
        dst_is_black_square = (dst_y % 2 == 0 and dst_x % 2 == 1) or (dst_y % 2 == 1 and dst_x % 2 == 0)
        moving_down = cur_y < dst_y
        moving_up = cur_y > dst_y

        if dst_is_black_square and type(dst) not in (LightPiece, DarkPiece) and ((piece.color == COLOR_DARK and moving_down) or (piece.color == COLOR_LIGHT and moving_up)):
            self.board[cur_y][cur_x], self.board[dst_y][dst_x] = self.board[dst_y][dst_x], self.board[cur_y][cur_x]
            return True
        else:
            return False
