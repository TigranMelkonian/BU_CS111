#
# ps2pr6.py - Problem Set 2, Problem 6
#
# Writing list comprehensions

# Problem 6-1: LC puzzles!
# This code won't work until you complete the list comprehensions!
# If you can't figure out how to complete one of them, please
# comment out the corresponding lines by putting a # at the start
# of the appropriate lines.

# part a
lc1 = [2 * x for x in range(5)]
print(lc1)

# part b
words = ['hello', 'world', 'how', 'goes', 'it?']
lc2 = [w[1] for w in words]
print(lc2)

# part c
lc3 = [word[::-1] * 2 for word in ['hello', 'bye', 'no']]
print(lc3)

# part d
lc4 = [x**2 for x in range(1, 10) if x % 2 == 0]
print(lc4)

# part e
#lc5 = [ for c in 'bu be you']
#print(lc5)


# Problem 5-2: Put your definition of the powers_of() function below.
def powers_of(base, count):
    """uses a list comprehension to construct and return a list containing the first
        count powers of base, beginning with the 0th power.
    """
    power_list = [base ** x for x in range(count)]
    return power_list


# Problem 5-3: Put your definition of the shorter_than() function below.
def shorter_than(n, wordlist):
    """uses a list comprehension to construct and return a list
        consisting of all words from wordlist that are shorter than n.
    """
    words_shorter_than_n = [word for word in wordlist if len(word) < n]
    return words_shorter_than_n


def test():
    """ performs test calls on the functions above """
    print(powers_of(2, 5))
    print(powers_of(3, 4))
    print(shorter_than(4, ['only', 'recursion', 'on', 'the', 'brain']))
    print(shorter_than(7, ['Boston', 'Chicago', 'Washington', 'Houston']))
    print(shorter_than(6, ['Boston', 'Chicago', 'Washington', 'Houston']))
    # optional but encouraged: add test calls for your functions below


test()

