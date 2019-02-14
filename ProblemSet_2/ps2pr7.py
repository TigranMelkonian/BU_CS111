#
# ps2pr6.py - Problem Set 2, Problem 7
#
# Fun with recursion, part II

def letter_score(letter):
    """takes a lowercase letter as input and returns the value of
        that letter as a scrabble tile. If letter is not a lowercase
        letter from ‘a’ to ‘z’, the function should return 0.
    """
    one_point = ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']
    two_point = ['d', 'g']
    three_point = ['b', 'c', 'm', 'p']
    four_point = ['f', 'h', 'v', 'w', 'y']
    five_point = ['k']
    eight_point = ['j', 'x']

    assert (len(letter) == 1)  # validates the input for the parameter
    if letter.isupper() or not letter.isalpha():
        return 0
    elif letter in one_point:
        return 1
    elif letter in two_point:
        return 2
    elif letter in three_point:
        return 3
    elif letter in four_point:
        return 4
    elif letter in five_point:
        return 5
    elif letter in eight_point:
        return 8
    else:
        return 10


def scrabble_score(word):
    """uses recursion to compute and return the scrabble score of
        that string – i.e., the sum of the scrabble scores of its letters.
    """
    if len(word) == 0:
        return 0
    else:
        word_score = scrabble_score(word[1:])
        return word_score + letter_score(word[0])


def index(elem, seq):
    """uses recursion to find and return the index of the first occurrence of elem
        in seq. The sequence seq can be either a list or a string.
    """
    if elem == '' or len(seq) == 0:
        return -1
    elif elem == seq[0]:
        return 0
    remaining_seq = index(elem, seq[1:])
    if remaining_seq < 0:
        return remaining_seq
    return remaining_seq + 1


def test():
    """ performs test calls on the functions above """
    print(letter_score('p'))
    print(letter_score('y'))
    print(letter_score('t'))
    print(letter_score('h'))
    print(scrabble_score('python'))
    print(scrabble_score('a'))
    print(scrabble_score('quetzal'))
    print(index('hi', ['hello', 111, 'c']))
    print(index('a', ''))
    print(index(42, []))
    print(index('b', 'banana'))
    print(index(5, [4, 10, 5, 3, 7, 5]))
    print(index('a', 'banana'))
    # optional but encouraged: add test calls for your functions below


test()
