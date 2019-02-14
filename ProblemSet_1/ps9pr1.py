#
# ps9pr1.py  (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#


class Board:
    """ A class that represents a connect 4 board"""

    # The constructor for the Board class.
    def __init__(self, height, width):
        """ constructor that initializes the two attributes
            in every Board object (height and width)
        """
        self.height = height  # number of rows in the board
        self.width = width  # number of columns in the board
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """returns a string representing a Board object.
        """
        s = ''  # begin with an empty string
        num_string = [' 0', ' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9']
        # add one row of slots at a time
        for row in range(self.height):
            s += '|'  # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        # and the numbers underneath it.
        s += ' ' + '_ ' * self.width + '\n'
        for i in range(self.width):
            s += num_string[(i % 10)]
        return s

    def add_checker(self, checker, col):
        """accepts two inputs: checker, a one-character string that specifies
            the checker to add to the board (either 'X' or 'O').col, an integer
            that specifies the index of the column to which the checker should
            be added and that adds checker to the appropriate row in column col of the board.
        """
        assert (checker == 'X' or checker == 'O')
        assert (0 <= col < self.width)
        row = self.height - 1
        while self.slots[row][col] != ' ' and row >= 0:
            row -= 1
        if row == -1:
            print('This column is already full! Please add a checker to another column')
        else:
            self.slots[row][col] = checker

    def reset(self):
        """reset the Board object on which it is called by setting all slots to contain a space character."""
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = " "

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
        """
        checker = 'X'  # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """returns True if it is valid to place a checker in the column col
            on the calling Board object. Otherwise, it should return False.
        """
        row = self.height - 1
        if not 0 <= col < self.width:
            return False
        while self.slots[row][col] != ' ' and row >= 0:
            row -= 1
        if row == -1:
            return False
        else:
            return True

    def is_full(self):
        """returns True if the called Board object is completely full of checkers, and returns False otherwise."""
        for col in range(self.width):
            if self.can_add_to(col):
                return False
        return True

    def remove_checker(self, col):
        """removes the top checker from column col of the called Board object.
            If the column is empty, then the method should do nothing.
        """
        assert (0 <= col < self.width)
        if not self.can_add_to(col):
            self.slots[0][col] = ' '
        else:
            row = self.height - 1
            while self.slots[row][col] == ' ' and row > 0:
                row -= 1
            if row == 0 and self.slots[row][col] == ' ':
                print('This column is empty!')
            else:
                self.slots[row][col] = ' '

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                        self.slots[row][col + 1] == checker and \
                        self.slots[row][col + 2] == checker and \
                        self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                        self.slots[row + 1][col] == checker and \
                        self.slots[row + 2][col] == checker and \
                        self.slots[row + 3][col] == checker:
                    return True

        # if we make it here, there were no vertical wins
        return False

    def is_up_diagonal_win(self, checker):
        """ Checks for a up diagonal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                        self.slots[row - 1][col + 1] == checker and \
                        self.slots[row - 2][col + 2] == checker and \
                        self.slots[row - 3][col + 3] == checker:
                    return True

        # if we make it here, there were no u wins
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a down diagonal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                        self.slots[row + 3][col + 3] == checker and \
                        self.slots[row + 2][col + 2] == checker and \
                        self.slots[row + 1][col + 1] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_win(self, checker):
        """accepts a parameter checker that is either 'X' or 'O', and returns True
            if there are four consecutive slots containing checker on the board.
        """
        assert (checker == 'X' or checker == 'O')
        if self.is_up_diagonal_win(checker) or self.is_down_diagonal_win(checker) or self.is_vertical_win(checker) or self.is_horizontal_win(checker):
            return True
        else:
            return False

