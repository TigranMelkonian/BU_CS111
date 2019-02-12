#
# ps7pr3.py (Problem Set 7, Problem 3)
#
# 2-D Lists
#
import random


def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []
    
    for r in range(height):
        row = [0] * width     # a row containing width 0s
        grid += [row]

    return grid


def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line, and nothing between values.
        input: grid is a 2-D list. We assume that all of the cell
               values are integers between 0 and 9.
    """
    height = len(grid)
    width = len(grid[0])
    
    for r in range(height):
        for c in range(width):
            print(grid[r][c], end='')   # print nothing between values
        print()                         # at end of row, go to next line


def inner_grid(height, width, digit):
    """ creates and returns a height x width grid in which the inner cells
        are set to digit, and cells on the outer border are all 0.
        inputs: height and width are positive integers
                digit is an integer
    """
    grid = create_grid(height, width)   # initially all 0s

    for r in range(1, height - 1):
        for c in range(1, width - 1):
            grid[r][c] = digit

    return grid


def diagonal_grid(height, width):
    """ creates and returns a height x width grid in which the cells
        on the diagonal are set to 1, and all other cells are 0.
        inputs: height and width are non-negative integers
    """
    grid = create_grid(height, width)   # initially all 0s

    for r in range(height):
        for c in range(width):
            if r == c:
                grid[r][c] = 1

    return grid


def random_grid(height, width):
    """creates and returns a 2-D list of height rows and width columns in which the inner cells
        are randomly assigned either 0 or 1, but the cells on the outer border are all 0.
    """
    grid = create_grid(height, width)  # initially all 0s
    for r in range(1, height-1):
        for c in range(1, width-1):
            grid[r][c] = random.choice([0, 1])
    return grid


def copy(grid):
    """creates and returns a deep copy of grid–a new, separate 2-D
        list that has the same dimensions and cell values as grid.
    """
    deep_copied_grid = create_grid(len(grid), len(grid[0]))
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            deep_copied_grid[r][c] = grid[r][c]
    return deep_copied_grid


def increment(grid):
    """takes an existing 2-D list of digits and increments each digit by 1. If incrementing a given digit causes it
        to become a 10 (i.e., if the original digit was a 9), then the new digit should “wrap around” and become a 0.
    """
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] += 1
            if grid[r][c] > 9:
                grid[r][c] = 0



