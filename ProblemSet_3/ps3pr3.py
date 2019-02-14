#
# ps2pr2.py - Problem Set 3, Problem 3
#
# Caesar cipher and decipher


# A template for a helper function called rot that we recommend you write
# as part of your work on the encipher function.
def rot(c, n):
    """that rotates a single character c forward by n spots in the alphabet."""
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)
    if c.islower():  # lower-case
        new_ord = ord(c) + n
        if new_ord > ord('z'):
            new_ord = new_ord - 26
            return chr(new_ord)
        else:
            return chr(new_ord)
    elif c.isupper():  # upper-case
        new_ord = ord(c) + n
        if new_ord > ord('Z'):
            new_ord = new_ord - 26
            return chr(new_ord)
        else:
            return chr(new_ord)
    else:  # non alpha
        return c


def encipher(s, n):
    """takes as inputs an arbitrary string s and a non-negative integer n between 0 and 25, and that returns a new string in
        which the letters in s have been “rotated” by n characters forward in the alphabet, wrapping around as needed
    """
    assert (type(s) == str)
    new_string = ''
    for i in range(len(s)):
        new_string += rot(s[i], n)
    return new_string


# A helper function that could be useful when assessing
# the "Englishness" of a phrase.
# You do *NOT* need to modify this function.
def letter_prob(c):
    """ if c is the space character (' ') or an alphabetic character,
        returns c's monogram probability (for English);
        returns 1.0 for any other character.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0


def decipher(s):
    """takes as input an arbitrary string s that has already been enciphered by having its characters “rotated” by some amount (possibly 0).
        decipher should return, to the best of its ability, the original English string, which will be some rotation (possibly 0) of the input string s.
    """
    decypherings = [encipher(s, n) for n in range(0, 25)]
    englishiness = [sum([letter_prob(letter) for letter in word])for word in decypherings]
    return decypherings[englishiness.index(max(englishiness))]


def test():
    """ performs test calls on the functions above """
    print(rot('e', 1))
    print(rot('e', 5))
    print(chr(106))
    print(encipher('hello', 1))
    print(decipher('Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla lclyfaopun dl ohcl slhyulk.'))
    print(decipher('Bzdrzq'))
    print(decipher('kwvozibctibqwva izm qv wzlmz nwz iv mfkmttmvb rwj'))
    print(encipher('Caesar cipher? I prefer Caesar salad.', 25))
    print()
    print()
    # optional but encouraged: add test calls for your functions below


test()

