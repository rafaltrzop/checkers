from .piece import *

dark_piece_king = DarkPiece()
dark_piece_king.become_king()
light_piece_king = LightPiece()
light_piece_king.become_king()

KINGS_BOARD = [
    [None, dark_piece_king, None, dark_piece_king, None, dark_piece_king, None, dark_piece_king],
    [dark_piece_king, None, dark_piece_king, None, dark_piece_king, None, dark_piece_king, None],
    [None, dark_piece_king, None, dark_piece_king, None, dark_piece_king, None, dark_piece_king],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [light_piece_king, None, light_piece_king, None, light_piece_king, None, light_piece_king, None],
    [None, light_piece_king, None, light_piece_king, None, light_piece_king, None, light_piece_king],
    [light_piece_king, None, light_piece_king, None, light_piece_king, None, light_piece_king, None]
]

class Gameboard:
    def __init__(self, board=None, size=8):
        if board == None:
            self.board = self.__generate_board(size)
            self.size = size
        else:
            self.board = self.__ensure_valid_board(board)
            self.size = len(board)

    def move(self, current_position, destination):
        cur_x = current_position['x']
        cur_y = current_position['y']
        dst_x = destination['x']
        dst_y = destination['y']

        dst_is_legal_move = self.__is_legal_move(current_position, destination)

        if dst_is_legal_move and type(self.board[dst_y][dst_x]) not in (LightPiece, DarkPiece):
            self.board[cur_y][cur_x], self.board[dst_y][dst_x] = self.board[dst_y][dst_x], self.board[cur_y][cur_x]
            return True
        else:
            return False

    def __generate_board(self, size):
        board = []
        board_top = []
        board_bottom = []

        if size == 1:
            gap = 1
        elif size % 2 == 0:
            gap = 2
        else:
            gap = 3

        for i in range((size-gap)//2):
            board_top.append([None]*size)
            board_bottom.append([None]*size)

        for y, row in enumerate(board_top):
            for x, square in enumerate(row):
                if y % 2 == 0 and x % 2 == 1:
                    board_top[y][x] = DarkPiece()
                if y % 2 == 1 and x % 2 == 0:
                    board_top[y][x] = DarkPiece()

        for y, row in enumerate(board_bottom):
            for x, square in enumerate(row):
                if (int((size / 2)) + gap) % 2 == 1:
                    if y % 2 == 0 and x % 2 == 1:
                        board_bottom[y][x] = LightPiece()
                    if y % 2 == 1 and x % 2 == 0:
                        board_bottom[y][x] = LightPiece()
                else:
                    if y % 2 == 0 and x % 2 == 0:
                        board_bottom[y][x] = LightPiece()
                    if y % 2 == 1 and x % 2 == 1:
                        board_bottom[y][x] = LightPiece()

        board.extend(board_top)
        for i in range(gap):
            board.append([None]*size)
        board.extend(board_bottom)

        return board

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

    def __is_legal_move(self, current_position, destination):
        cur_x = current_position['x']
        cur_y = current_position['y']
        dst_x = destination['x']
        dst_y = destination['y']

        if self.__is_move_within_bounds_of_board(dst_x, dst_y):
            dst_is_white_square = (dst_y % 2 == 0 and dst_x % 2 == 0) or (dst_y % 2 == 1 and dst_x % 2 == 1)
            if dst_is_white_square:
                return False

            piece = self.board[cur_y][cur_x]
            if piece.king:
                pass
            elif dst_x == cur_x-2:
                if piece.color == COLOR_LIGHT:
                    if dst_y == cur_y - 2 and type(self.board[cur_y-1][cur_x-1]) is DarkPiece:
                        self.board[cur_y-1][cur_x-1] = None
                        return True
                if piece.color == COLOR_DARK:
                    if dst_y == cur_y + 2 and type(self.board[cur_y+1][cur_x-1]) is LightPiece:
                        self.board[cur_y+1][cur_x-1] = None
                        return True
            elif dst_x == cur_x+2:
                if piece.color == COLOR_LIGHT:
                    if dst_y == cur_y - 2 and type(self.board[cur_y-1][cur_x+1]) is DarkPiece:
                        self.board[cur_y-1][cur_x+1] = None
                        return True
                if piece.color == COLOR_DARK:
                    if dst_y == cur_y + 2 and type(self.board[cur_y+1][cur_x+1]) is LightPiece:
                        self.board[cur_y+1][cur_x+1] = None
                        return True
            elif dst_x in (cur_x-1, cur_x+1):
                if piece.color == COLOR_LIGHT:
                    if dst_y == cur_y - 1:
                        return True
                if piece.color == COLOR_DARK:
                    if dst_y == cur_y + 1:
                        return True

        return False

    def __is_move_within_bounds_of_board(self, dst_x, dst_y):
        if dst_x in range(self.size) and dst_y in range(self.size):
            return True
        else:
            return False
