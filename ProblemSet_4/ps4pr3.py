#
# ps4pr3.py - Problem Set 4, Problem 3
#
# Recursive operations on binary numbers
#


def bitwise_and(b1, b2):
    """takes as inputs two strings b1 and b2 that represent binary numbers. The function should use
        recursion to compute the bitwise AND of the two numbers and return the result in the form of a string.
    """
    if b1 == '' and b2 == '':
        return ''
    elif b1 == '' and b2 != '':
        return '0' * len(b2)
    elif b2 == '' and b1 != '':
        return '0' * len(b1)
    elif len(b1) > len(b2):
        to_recurse = bitwise_and(b1[:-1], b2[:-1])
        if b1[-1] == b2[-1]:
            return to_recurse + '1'
        else:
            return to_recurse + '0'
    elif len(b2) > len(b1):
        to_recurse = bitwise_and(b1[:-1], b2[:-1])
        if b1[-1] == b2[-1]:
            return to_recurse + '1'
        else:
            return to_recurse + '0'
    else:
        to_recurse = bitwise_and(b1[:-1], b2[:-1])
        if b1[-1] == b2[-1]:
            return to_recurse + '1'
        else:
            return to_recurse + '0'


def add_bitwise(b1, b2):
    """adds two binary numbers. This function should use recursion to perform the bitwise, “elementary-school”
        addition algorithm that we discussed in lecture, and it should return the result.
    """
    if b1 == '' and b2 == '':
        return ''
    if b1 == '' and b2 != '':
        return b2
    if b2 == '' and b1 != '':
        return b1
    else:
        to_recurse = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1] == '0':
            return to_recurse + b2[-1]
        elif b2[-1] == '0':
            return to_recurse + '1'
        else:
            return add_bitwise(to_recurse, '1') + '0'

