# Py-tic-tac-toe
Basic tic-tac-toe in Python. Tests include "tests_live", which uses input and
expected output files to assert code's functioning.

To play, run "__init__.py"

There are two sets of tests:
    tests/tests.py, and
    tests/tests_live.py

tests.py needs the self.start() line of Game.__init__() to be commented out
before running. It also needs sys.path to be hard-coded in itself.

With tests_live.py,
Expect an EOL error. If an AssertionError is raised, a test is not passing.