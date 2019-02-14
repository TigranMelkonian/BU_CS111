#
# ps1pr6.py - Problem Set 1, Problem 6
#
# Functions on strings and lists, part II
#
# name: Tigran Melkonian


def replace_prefix(word, prefix):
    """returns a string in which the character in prefix replace
        the characters of word (up to the length of prefix
    """
    return prefix + word[len(prefix) :]


def swap_halves(s):
    """returns a string whose first half is s's second half
        and whose second half is s's first half
     """
    half_point = len(s)//2
    if len(s) % 2 == 0:
        return s[half_point:len(s)] + s[0:half_point]
    else:
        return s[half_point + 1:len(s)] + s[0:half_point + 1]


def statistics(list_of_int):
    """returns a list of the following statistics:
        sum, average, min, max in that order
    """
    sum_of_list = 0
    my_min = list_of_int[1]
    my_max = list_of_int[1]

    for i in range(len(list_of_int)):
        sum_of_list += list_of_int[i]
        if list_of_int[i] > my_max:
            my_max = list_of_int[i]
        if list_of_int[i] < my_min:
            my_min = list_of_int[i]

    average_of_list = sum_of_list/len(list_of_int)
    return [sum_of_list] + [average_of_list] + [my_min] + [my_max]


def test():
    """ performs test calls on the functions above """
    print(replace_prefix('undo', 're'))
    print(replace_prefix('this!ismyword', 'cs111'))
    print(swap_halves('homework'))
    print(swap_halves('rugerrats'))
    print(statistics([2, 8, 7]))
    print(statistics([11, 2, 11]))
    #print()
    # optional but encouraged: add test calls for your functions below
test()
