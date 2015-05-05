from _helpers import *
from line     import *
from square   import *

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

        self.start()

    def add_relation(self, line, sqr):
        line.squares.append(sqr)
        sqr.lines.append(line)

    def check_square(self, sqr):
        pass

    def check_victory(self):
        pass

    def get_square(self, usr_in):
        x = convert_number(usr_in[0])
        y = convert_number(usr_in[1])
        return self.squares[x][y]

    def is_usr_in_no_square(self, usr_in):
        if len(usr_in) < 2:
            return True

        x = convert_number(usr_in[0])
        y = convert_number(usr_in[1])

        if   x == None or x < 0 or x > len(self.squares):
            return True
        elif y == None or y < 0 or y > len(self.squares):
            return True
        else:
            return False

    def mark_square(self, sqr):
        sqr.mark = self.crnt_plyr

    def prompt_square(self):
        print "Please select your square..."
        usr_in = raw_input("> ")

        if self.is_usr_in_no_square(usr_in):
            print "I cannot find a square matching that input."
            return self.prompt_square()

        square = self.get_square(usr_in)

        if square.mark != None:
            print "That square is already marked!"
            return self.prompt_square()

        return self.get_square(usr_in)

    def start(self):
        # Until turn_counter == end or victory, turn
        turn_counter = 0
        # Dynamic setting of num_turns allows for different grid size.
        num_turns    = len(self.squares) * len(self.squares)
        while turn_counter < num_turns:
            turn_counter += 1
            self.turn()

        print "Game over. There are no more free squares."

    def switch_player(self):
        if self.crnt_plyr == "X":
            self.crnt_plyr = "O"
        else: # self.crnt_plyr == "O"
            self.crnt_plyr = "X"

    def turn(self):
        square = self.prompt_square()
        self.mark_square(square)
        # check_victory
        self.switch_player()