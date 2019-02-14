#
# ps2pr2.py - Problem Set 2, Problem 2
#
# More practice with writing functions


def mirror(s):
    """returns a mirrored version of
        s that is twice the length of the original string.
    """
    return s + s[::-1]


def is_mirror(s):
    """returns True if s is a mirrored string (i.e., a string that could have
        been produced by your mirror function) and False otherwise.
    """
    half_point = len(s)//2
    if len(s) % 2 != 0:
        return False
    elif s[0:half_point] == s[len(s):half_point-1:-1]:
        return True
    else:
        return False


def test():
    """ performs test calls on the functions above """
    print(mirror('bacon'))
    print(mirror('XYZ'))
    print(mirror('yes'))
    print(is_mirror('baconnocab'))
    print(is_mirror('baconnoca'))
    print(is_mirror('yessey'))
    # optional but encouraged: add test calls for your functions below
test()
