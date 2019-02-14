#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect Four Player class
#

from ps9pr1 import Board


class Player:
    """ A class that represents a connect 4 Player"""

    # The constructor for the Player class.
    def __init__(self, checker):
        """constructs a new Player object by initializing the following two attributes:an attribute checker –
            a one-character string that represents the game piece for the player, as specified by the parameter checker
            an attribute num_moves – an integer that stores how many moves the player has made so far. This attribute
            should be initialized to zero to signify that the Player object has not yet made any Connect Four moves.
         """
        assert (checker == 'X' or checker == 'O')
        self.num_moves = 0  # initialized to zero to signify that player has not made any moves yet
        self.checker = checker

    def __repr__(self):
        """returns a string representing a Player object. The string returned
            should indicate which checker the Player object is using.
        """
        return 'Player ' + self.checker

    def opponent_checker(self):
        """returns a one-character string representing the checker of the Player object’s opponent."""
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
        """accepts a Board object as a parameter and returns the column where the player wants to make the next move."""
        col = int(input("Enter a column number that represents where you want to place a checker on the board: "))
        if board.is_full():
            print('Sorry the board is full. You are not able to place any more checkers on the board.')
        while not board.can_add_to(col):
            print('Sorry try again!')
            col = int(input("Enter a column number that represents where you want to place a checker on the board. "))
        self.num_moves += 1
        return col
