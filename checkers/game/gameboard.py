from .piece import *

class Gameboard:
    @classmethod
    def build(self, size=8):
        """Builds custom size board."""

        board = self.__generate_board(size)
        return Gameboard(board)

    @classmethod
    def __generate_board(self, size):
        """Generates inital state of the board with pieces."""

        board_top = []
        board_gap = []
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
                if (y % 2 == 0 and x % 2 == 1) or (y % 2 == 1 and x % 2 == 0):
                    board_top[y][x] = DarkPiece()

        for i in range(gap):
            board_gap.append([None]*size)

        for y, row in enumerate(board_bottom):
            for x, square in enumerate(row):
                if ((size // 2) + gap) % 2 == 1:
                    if (y % 2 == 0 and x % 2 == 1) or (y % 2 == 1 and x % 2 == 0):
                        board_bottom[y][x] = LightPiece()
                else:
                    if (y % 2 == 0 and x % 2 == 0) or (y % 2 == 1 and x % 2 == 1):
                        board_bottom[y][x] = LightPiece()

        board = board_top + board_gap + board_bottom
        return board

    def __init__(self, board):
        self.board = self.__ensure_valid_board(board)
        self.size = len(board)

    def move(self, current_position, destination):
        """Moves piece from current position to destination on the board."""

        cur_x = current_position['x']
        cur_y = current_position['y']
        dst_x = destination['x']
        dst_y = destination['y']
        dst_is_legal_move = self.__is_legal_move(current_position, destination)

        if dst_is_legal_move and type(self.board[dst_y][dst_x]) not in (LightPiece, DarkPiece):
            dst_is_last_row_of_board = dst_y in (0, self.size-1)
            if dst_is_last_row_of_board:
                self.board[cur_y][cur_x].become_king()

            self.board[cur_y][cur_x], self.board[dst_y][dst_x] = self.board[dst_y][dst_x], self.board[cur_y][cur_x]

            return True
        else:
            return False

    def __ensure_valid_board(self, board):
        """Ensures that board is a square and pieces are set on the black squares."""

        board_size = len(board)

        for y, row in enumerate(board):
            if len(row) != board_size:
                raise ValueError('cannot use non square board')

            for x, square in enumerate(row):
                if type(square) in (LightPiece, DarkPiece):
                    legal_square = self.__is_legal_square(x, y)
                    if not legal_square:
                        raise ValueError('cannot set piece on white square')

        return board

    def __is_legal_square(self, x, y):
        """Checks if given square is black."""

        return (y % 2 == 0 and x % 2 == 1) or (y % 2 == 1 and x % 2 == 0)

    def __is_legal_move(self, current_position, destination):
        """Checks if given move is possible and then performs it."""

        cur_x = current_position['x']
        cur_y = current_position['y']
        dst_x = destination['x']
        dst_y = destination['y']

        if self.__is_move_within_bounds_of_board(dst_x, dst_y):
            dst_is_white_square = (dst_y % 2 == 0 and dst_x % 2 == 0) or (dst_y % 2 == 1 and dst_x % 2 == 1)
            if dst_is_white_square:
                return False

            piece = self.board[cur_y][cur_x]
            jumping_on_diagonals = abs(dst_x - cur_x) == abs(dst_y - cur_y)
            if piece.king and jumping_on_diagonals:
                next_x = cur_x
                next_y = cur_y
                diagonal_pieces_count = 0
                opponent_x = None
                opponent_y = None
                while True:
                    if cur_x < dst_x:
                        next_x += 1
                    else:
                        next_x -= 1

                    if cur_y < dst_y:
                        next_y += 1
                    else:
                        next_y -= 1

                    next_piece = self.board[next_y][next_x]
                    if type(next_piece) in (LightPiece, DarkPiece):
                        diagonal_pieces_count += 1
                        if diagonal_pieces_count > 1:
                            return False

                        if piece.color == next_piece.color:
                            return False
                        else:
                            opponent_x = next_x
                            opponent_y = next_y

                    if next_x == dst_x and next_y == dst_y:
                        break

                if opponent_x and opponent_y:
                    self.board[opponent_y][opponent_x] = None

                return True
            elif dst_x == cur_x-2:
                if piece.color == COLOR_LIGHT and dst_y == cur_y - 2 and type(self.board[cur_y-1][cur_x-1]) is DarkPiece:
                    self.board[cur_y-1][cur_x-1] = None
                    return True
                if piece.color == COLOR_DARK and dst_y == cur_y + 2 and type(self.board[cur_y+1][cur_x-1]) is LightPiece:
                    self.board[cur_y+1][cur_x-1] = None
                    return True
            elif dst_x == cur_x+2:
                if piece.color == COLOR_LIGHT and dst_y == cur_y - 2 and type(self.board[cur_y-1][cur_x+1]) is DarkPiece:
                    self.board[cur_y-1][cur_x+1] = None
                    return True
                if piece.color == COLOR_DARK and dst_y == cur_y + 2 and type(self.board[cur_y+1][cur_x+1]) is LightPiece:
                    self.board[cur_y+1][cur_x+1] = None
                    return True
            elif dst_x in (cur_x-1, cur_x+1):
                if piece.color == COLOR_LIGHT and dst_y == cur_y - 1:
                    return True
                if piece.color == COLOR_DARK and dst_y == cur_y + 1:
                    return True

        return False

    def __is_move_within_bounds_of_board(self, dst_x, dst_y):
        """Checks if given move is within bounds of the board."""
        
        if dst_x in range(self.size) and dst_y in range(self.size):
            return True
        else:
            return False
