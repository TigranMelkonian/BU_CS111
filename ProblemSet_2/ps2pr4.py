#
# ps2pr2.py - Problem Set 2, Problem 4
#
# Fun with recursion, part I


def copy(s, n):
    """uses recursion to create and return a string in which
        n copies of s have been concatenated together.
    """
    if s == '' or n == 0:
        return ''
    else:
        to_recurse = copy(s, n-1)
        return to_recurse + s


def sum(values):
    """uses recursion to compute and return the
        sum of all the integers in a list
     """
    if len(values) == 0:
        return 0
    else:
        return values[0] + sum(values[1:])


def test():
    """ performs test calls on the functions above """
    print(copy('yes', 3))
    print(copy('da', 2))
    print(copy('Go BU!', 4))
    print(sum([]))
    print(sum([3, 5, 4]))
    print(sum([1, 3, 4, 2, 5]))
    # optional but encouraged: add test calls for your functions below
test()
