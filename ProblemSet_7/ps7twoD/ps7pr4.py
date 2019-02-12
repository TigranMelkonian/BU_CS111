#
# ps7pr4.py  (Problem Set 7, Problem 4)
#
# Conway's Game of Life
#
#

# IMPORTANT: this file is for your solutions to Problem 4.
# Your solutions to Problem 3 should go in ps7pr3.py instead.

from ps7twoD.ps7pr3 import *
from ps7twoD.gol_graphics import *
import random


def count_neighbors(cellr, cellc, grid):
    """returns the number of alive neighbors of the cell at position [cellr][cellc] in the specified grid."""
    num_neighbors = 0
    for r in range(cellr - 1, cellr + 2):
        for c in range(cellc - 1, cellc + 2):
            if r == cellr and c == cellc:
                num_neighbors += 0
            elif grid[r][c] == 1:
                num_neighbors += 1
    return num_neighbors


def next_gen(grid):
    """takes a 2-D list called grid that represents the current generation of cells, and that uses the rules of the
        Game of Life (see above) to create and return a new 2-D list representing the next generation of cells.
    """
    new_grid = copy(grid)
    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            if count_neighbors(r, c, grid) < 2 or count_neighbors(r, c, grid) > 3:  # loneliness
                new_grid[r][c] = 0
            if count_neighbors(r, c, grid) == 3:  # brought back to life
                new_grid[r][c] = 1
    return new_grid




