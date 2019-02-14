#
# ps2pr2.py - Problem Set 3, Problem 4
#
# More algorithm design!


def rem_last(elem, values):
    """ takes as inputs a value elem and a list values and that uses recursion to create and return a
        version of values in which the last occurrence of elem (if any) has been removed.
     """
    if not values:
        return []
    elif values[len(values) - 1] == elem:
        return values[:-1]
    else:
        result_rest = rem_last(elem, values[:-1])
        return result_rest + [values[-1]]


def jscore(s1, s2):
    """takes two strings s1 and s2 as inputs and returns the Jotto score of s1
        compared with s2 – i.e., the number of characters in s1 that are shared by s2.
    """
    num_in_common = 0
    if s1 == '' or s2 == '':
        return 0
    elif s1[0] in s2:
        return num_in_common + 1 + jscore(s1[1:], s2.replace(s1[0], '', 1))
    else:
        return num_in_common + jscore(s1[1:], s2)


def lcs(s1, s2):
    """takes two strings s1 and s2 and returns the longest common subsequence (LCS) that they share."""
    if s1 == '' or s2 == '':
        return ''
    elif s1[0] == s2[0]:
        longest_string = s1[0] + lcs(s1[1:], s2[1:])
    else:
        result1 = lcs(s1[1:], s2)
        result2 = lcs(s1, s2[1:])
        if len(result1) > len(result2):
            longest_string = result1
        else:
            longest_string = result2
    return longest_string


def test():
    """ performs test calls on the functions above """
    print(rem_last(3, [2, 3, 1, 3, 4, 3, 5]))
    print(rem_last(0, [1, 0, 1, 0, 0]))
    print(rem_last(1, [1, 0, 1, 0, 0]))
    print(jscore('recursion', 'excursion'))
    print(jscore('always', 'bananas'))
    print(lcs('', 'whew'))
    print(lcs('gattaca', 'tacgaacta'))
    print(lcs('abcdefgh', 'efghabcd'))
    print(lcs('human', 'chimp'))
    # optional but encouraged: add test calls for your functions below


test()

