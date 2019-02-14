#
# ps1pr5.py - Problem Set 1, Problem 5
#
# Functions on strings and lists, part I
#
# name: Tigran Melkonian


def front3(s):
    """retunrs new string of the first three characters
        of given string repeated three times over
    """
    return s[0:4] * 3


def shorter_len(l1, l2):
    """ returns the length of
        the shorter (of the two) lists
     """
    if len(l1) > len(l2):
        return len(l2)
    elif len(l1) == len(l2):
        return len(l1)
    else:
        return len(l1)


def ends_with(word, suffix):
    """returns TRUE if the given word
        ends with the string suffix and false OTW
    """
    if word[-len(suffix):] == suffix:
        return True
    else:
        return False

# test function with a sample test call for function


def test():
    """ performs test calls on the functions above """
    print(shorter_len(['computers', 'compute'],['humans', 'have', 'intelligence']))
    print(shorter_len([5, 'abc', '123', ['cs', 111]], ['I', 'Love', 'cs']))
    print(shorter_len(['begin', 'end'], [['begin', 'middle','end']]))
    print(ends_with('computer', 'ter'))
    print(ends_with('computer', 'tar'))
    print(ends_with('begin', 'in'))
    print(ends_with('begin', 'on'))
    # optional but encouraged: add test calls for your functions below


test()
