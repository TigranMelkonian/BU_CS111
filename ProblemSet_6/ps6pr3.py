#
# ps4pr1.py - Problem Set 6, Problem 3
#
# Processing sequences with loops
#


def double(s):
    """ takes an arbitrary string s as input, and that uses a loop to construct
        and return the string formed by doubling each character in the string.
    """
    duplicated_string = ''
    if s == '':
        return ''
    else:
        for character in s:
            duplicated_string += character * 2
        return duplicated_string


def weave(s1, s2):
    """takes as inputs two strings s1 and s2 and uses a loop to construct and return a new string that
        is formed by “weaving” together the characters in the strings s1 and s2 to create a single string.
    """
    weaved_string = ''
    extra_chars = ''
    len_shorter = min(len(s1), len(s2))
    if len(s1) > len(s2):
        extra_chars = s1[len(s2):]
    elif len(s2) > len(s1):
        extra_chars = s2[len(s1):]
    for i in range(len_shorter):
        weaved_string += s1[i] + s2[i]
    return weaved_string + extra_chars


def square_evens(values):
    """takes a list of integers called values, and that modifies the list so that all of its even
        elements are replaced with their squares, but all of its odd elements are left unchanged.
    """
    for i in range(len(values)):
        if values[i] % 2 == 0:
            values[i] = values[i] ** 2
    return values


def index(elem, seq):
    """takes as inputs an element elem and a sequence seq, and that uses a loop to
        find and return the index of the first occurrence of elem in seq.
    """
    for i in range(len(seq)):
        if seq[i] == elem:
            return i
    return -1

