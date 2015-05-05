from line   import *
from square import *

class Game(object):
    def __init__(self):
        self.crnt_plyr = "X"

        self.squares = []
        for i in range(3):
            self.squares.append([])
            for j in range(3):
                self.squares[i].append(Square())

        # Make relationships for non-diagonal lines:
        for i in range(3):
            vertical_line   = Line()
            horizontal_line = Line()
            for j in range(3):
                self.add_relation(vertical_line,   self.squares[i][j])
                self.add_relation(horizontal_line, self.squares[j][i])
        # Make relationships for diagonal lines
        diagonal_line_top_left  = Line()
        diagonal_line_top_right = Line()
        for i in range(3):
            self.add_relation(diagonal_line_top_left,  self.squares[i][2 - i])
            self.add_relation(diagonal_line_top_right, self.squares[i][i])

        # Until turn_counter == end or victory, turn

    def add_relation(self, line, sqr):
        line.squares.append(sqr)
        sqr.lines.append(line)

    def check_victory(self):
        pass

    def mark_square(self):
        pass

    def prompt_square(self):
        pass

    def switch_player(self):
        pass

    def turn(self):
        pass
        # Switch player
        # prompt_sqr
        # mark_sqr
        # check_victory