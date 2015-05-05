# To run these tests, first comment out self.start() at the end of 'Game.__init__'
# You might also have to change your PYTHONPATH

from game   import *
from line   import *
from square import *

def assert_equal(arg1, arg2):
    if arg1 == arg2:
        pass
#         print "T"
    else: # arg1 != arg2
        print "FALSE"

game = Game()
all_squares        = { "center_square_ary": [],
                       "corner_squares": [],
                       "other_squares": [] }
all_squares['corner_squares'].append(game.squares[0][0])
all_squares['other_squares'].append(game.squares[0][1])
all_squares['corner_squares'].append(game.squares[0][2])
all_squares['other_squares'].append(game.squares[1][0])
all_squares['center_square_ary'].append(game.squares[1][1])
all_squares['other_squares'].append(game.squares[1][2])
all_squares['corner_squares'].append(game.squares[2][0])
all_squares['other_squares'].append(game.squares[2][1])
all_squares['corner_squares'].append(game.squares[2][2])

print "Test Game starting player:"
assert_equal(game.crnt_plyr, "X")

print "Test Game.squares attr:"
assert_equal(isinstance(game.squares, list), True)
assert_equal(isinstance(game.squares[0], list), True)
assert_equal(isinstance(game.squares[0], Square), False)
assert_equal(isinstance(game.squares[0][1], Square), True)

print "Test Game.squares' line length and lines' length:"
for sqr in all_squares['corner_squares']:
    assert_equal(len(sqr.lines), 3)
    for line in sqr.lines:
        assert_equal(len(line.squares), 3)
for sqr in all_squares['center_square_ary']:
    assert_equal(len(sqr.lines), 4)
    for line in sqr.lines:
        assert_equal(len(line.squares), 3)
for sqr in all_squares['other_squares']:
    assert_equal(len(sqr.lines), 2)
    for line in sqr.lines:
        assert_equal(len(line.squares), 3)