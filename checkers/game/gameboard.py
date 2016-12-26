from .piece import *

WHITE_SQUARE = 'WHITE_SQUARE'
BLACK_SQUARE = 'BLACK_SQUARE'

class Gameboard:
    def __init__(self, board):
        self.board = board

    def move(self, current_position, destination):
        piece = self.board[current_position['y']][current_position['x']]
        destination_is_black_square = (destination['y'] % 2 == 0 and destination['x'] % 2 == 1) or (destination['y'] % 2 == 1 and destination['x'] % 2 == 0)
        moving_down = current_position['y'] < destination['y']
        moving_up = current_position['y'] > destination['y']

        if destination_is_black_square and ((piece.color == COLOR_DARK and moving_down) or (piece.color == COLOR_LIGHT and moving_up)):
            self.board[current_position['y']][current_position['x']], self.board[destination['y']][destination['x']] = self.board[destination['y']][destination['x']], self.board[current_position['y']][current_position['x']]
            return True
        else:
            return False
