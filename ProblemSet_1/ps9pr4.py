#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four
#

import random
from ps9pr3 import *


class AIPlayer(Player):
    """this “AI player” will look ahead some number of moves into the future to assess the impact
        of each possible move that it could make for its next move, and it will assign a score to each
        possible move. And since each move corresponds to a column number, it will effectively assign a
        score to each column.

        #-1 for a column that is already full
        #0 for a column that, if chosen as the next move, will result in a loss for the player at some point during
         the number of moves that the player looks ahead.
        #100 for a column that, if chosen as the next move, will result in a win for the player at some point during
         the number of moves that the player looks ahead.
         #50 for a column that, if chosen as the next move, will result in neither a win nor a loss for the player
          at any point during the number of moves that the player looks ahead.
        """

    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert (checker == 'X' or checker == 'O')
        assert (tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert (lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """returns a string representing an AIPlayer object and
            also indicate the player’s tiebreaking strategy and lookahead
        """
        return 'Player ' + self.checker + '(' + self.tiebreak + ',' + str(self.lookahead) + ')'
