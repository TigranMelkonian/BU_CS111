#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game
#

from ps9pr1 import Board
from ps9pr2 import Player
import random


def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
            or player1.checker == player2.checker:
        print('need one X player and one O player.' + '\n')
        return None

    print('Welcome to Connect Four!' + '\n')
    board = Board(6, 7)
    print(board)

    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board


def process_move(player, board):
    """takes two parameters: a Player object for the player whose move
        is being processed, and a Board object for the game that is being played.
        will perform all of the steps involved in processing a single move by the
        specified player on the specified board.
    """
    print('Player ' + player.checker + "'s turn")
    column_to_add = player.next_move(board)  # determine which column current player would like to add to
    board.add_checker(player.checker, column_to_add)
    if board.is_full():
        if board.is_win(player.checker):
            print(board)
            print('Player ' + player.checker + ' wins in ' + str(player.num_moves) + ' moves.')
            print('Congratulations!')
            return True
        else:
            print(board)
            print("It's a tie!")
            return True
    elif board.is_win(player.checker):
        print(board)
        print('Player ' + player.checker + ' wins in ' + str(player.num_moves) + ' moves.')
        print('Congratulations!')
        return True
    else:
        print(board)
        return False


class RandomPlayer(Player):
    """RandomPlayer that can be used for an unintelligent computer player
        that chooses at random from the available columns.
    """

    def next_move(self, board):
        """this version of next_move should choose at random from the columns in the specified board
            that are not yet full, and return the index of that randomly selected column.
        """
        available_columns = []
        if board.is_full():
            print('Sorry the board is full. You are not able to place any more checkers on the board.')
        for col in range(board.width):
            if board.can_add_to(col):
                available_columns += [col]
        self.num_moves += 1
        return random.choice(available_columns)



