from _helpers import *
from line     import *
from square   import *

class Game(object):
    def __init__(self):
        self.crnt_plyr = "X"
        self.squares = self.build_grid()
        self.victory = False
        self.display_instruct()

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

    def display_instruct(self):
        print(
        """
        Welcome to Tic-Tac-Toe.
        You will make your move known by entering a number, 0-8. The
        number will correspond to the board position as shown below:
                    7   |   8   |   9
                    -----------------
                    4   |   5   |   6
                    -----------------
                    1   |   2   |   3
        Prepare yourself. Muahahaaa!! >:}} \n
        """
        )

    def get_square(self, usr_in):
        num = convert_number(usr_in)

        if num == 1:
            return self.squares[0][2]
        elif num == 2:
            return self.squares[1][2]
        elif num == 3:
            return self.squares[2][2]
        elif num == 4:
            return self.squares[0][1]
        elif num == 5:
            return self.squares[1][1]
        elif num == 6:
            return self.squares[2][1]
        elif num == 7:
            return self.squares[0][0]
        elif num == 8:
            return self.squares[1][0]
        elif num == 9:
            return self.squares[2][0]

    def is_usr_in_valid(self, usr_in):
        if len(usr_in) != 1:
            return False

        num = convert_number(usr_in)

        if num == None or num < 0 or num > 9:
            return False

        return True

    def mark_square(self, sqr):
        sqr.mark = self.crnt_plyr

    def prompt_square(self):
        print "Please select your square..."
        usr_in = raw_input("> ")

        if not self.is_usr_in_valid(usr_in):
            print "I cannot find a square matching that input."
            return self.prompt_square()

        square = self.get_square(usr_in)

        if square.mark != " ":
            print "That square is already marked!"
            return self.prompt_square()

        return square

    def render_grid(self):
        grid = self.squares
        for y in range(3):
            print("\n\t" + grid[0][y].mark + "\t|\t" + grid[1][y].mark +
                                                    "\t|\t" + grid[2][y].mark)

            if y == 2:
                break

            print("\n\t--------------------------------------")

    def start(self):
        # Until turn_counter == end or victory, turn
        turn_counter = 0
        # Dynamic setting of num_turns allows for different grid size.
        num_turns    = len(self.squares) * len(self.squares)
        while turn_counter < num_turns:
            turn_counter += 1
            self.turn()

            if self.victory:
                print "Player '" + self.crnt_plyr + "', you lose! :P"
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