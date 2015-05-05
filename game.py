from _helpers import *
from line     import *
from square   import *

class Game(object):
    def __init__(self):
        self.crnt_plyr = "X"
        self.squares = self.build_grid()
        self.victory = False

        self.start()

    def add_relation(self, line, sqr):
        line.squares.append(sqr)
        sqr.lines.append(line)

    def build_grid(self):
        grid = []

        for i in range(3):
            grid.append([])
            for j in range(3):
                grid[i].append(Square())

        # Make relationships for non-diagonal lines:
        for i in range(3):
            vertical_line   = Line()
            horizontal_line = Line()
            for j in range(3):
                self.add_relation(vertical_line,   grid[i][j])
                self.add_relation(horizontal_line, grid[j][i])
        # Make relationships for diagonal lines
        diagonal_line_top_left  = Line()
        diagonal_line_top_right = Line()
        for i in range(3):
            self.add_relation(diagonal_line_top_left,  grid[i][2 - i])
            self.add_relation(diagonal_line_top_right, grid[i][i])

        return grid

    def check_victory(self, sqr):
        for line in sqr.lines:
            if all(square.mark == self.crnt_plyr for square in line.squares):
                self.victory = True
                return True

        return False


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

        if square.mark != " ":
            print "That square is already marked!"
            return self.prompt_square()

        return self.get_square(usr_in)

    def render_grid(self):
        grid = self.squares
        for x in range(3):
            print grid[x][0].mark + "|" + grid[x][1].mark + "|" + grid[x][2].mark

            if x == 2:
                break

            print "-----"

    def start(self):
        # Until turn_counter == end or victory, turn
        turn_counter = 0
        # Dynamic setting of num_turns allows for different grid size.
        num_turns    = len(self.squares) * len(self.squares)
        while turn_counter < num_turns:
            turn_counter += 1
            self.turn()

            if self.victory:
                print "Player", self.crnt_plyr, "you lose! :P"
                break

        self.render_grid()
        print "Game over."

    def switch_player(self):
        if self.crnt_plyr == "X":
            self.crnt_plyr = "O"
        else: # self.crnt_plyr == "O"
            self.crnt_plyr = "X"

    def turn(self):
        self.render_grid()
        square = self.prompt_square()
        self.mark_square(square)
        self.check_victory(square)
        self.switch_player()