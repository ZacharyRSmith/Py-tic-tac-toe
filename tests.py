from game   import *
from line   import *
from square import *

def assert_equal(arg1, arg2):
    if arg1 == arg2:
        print "T"
    else: # arg1 != arg2
        print "FALSE"

game = Game()
def test_game_start_player():
    assert_equal(game.crnt_plyr, "X")
test_game_start_player()