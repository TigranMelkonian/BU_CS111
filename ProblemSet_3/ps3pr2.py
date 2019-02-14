#
# ps2pr2.py - Problem Set 3, Problem 2
#
# Algorithm Design


def abs_list_lc(values):
    """uses a list comprehension to create and return a
        list containing the absolute values of the numbers in values.
    """
    return [abs(x) for x in values]


def abs_list_rec(values):
    """uses a recursion to create and return a
        list containing the absolute values of the numbers in values.
    """
    if len(values) == 0:
        return values
    else:
        value_list_rest = abs_list_rec(values[1:])
        return [abs(values[0])] + value_list_rest


def num_vowels(s):
    """ returns the number of vowels in the string s
        input: s is a string of 0 or more lowercase letters
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_vowels(s[1:])
        if s[0] in 'aeiou':
            return 1 + num_in_rest
        else:
            return 0 + num_in_rest


def most_vowels(words):
    """takes a list of strings called words and
        returns the string in the list with the most vowels.
    """
    if len(words) == 1:
        return num_vowels(words[0])
    else:
        max_in_rest = most_vowels(words[1:])
        if max_in_rest > num_vowels(words[0]):
            return max_in_rest
        else:
            return num_vowels(words[0])


def num_multiples(m, values):
    """takes an integer m and a list of integers values and returns
        the number of integers in values that are multiples of m.
    """
    return sum([1 for value in values if value % m == 0])


def message(name, age):
    """takes a string name and an integer age and returns a string that
        is a personalized message based on the values of the two parameters.
    """
    if age <= 0:
        return name + " very funny!"
    elif 1 <= age <= 9:
        return name + " you should not be using a computer!"
    elif 10 <= age <= 14:
        return name + " welcome to the dweeb years!"
    elif 15 <= age <= 17:
        return name + " get ready for the college essays!"
    elif 18 <= age <= 20:
        return name + " you have to wait " + str(21-age) + " more year(s) to be legal!"
    elif age == 21:
        return name + " congrats! But be smart!"
    elif 22 <= age <= 29:
        return name + " downhill from here!"
    elif age >= 30:
        return name + " stinks for you!"


def test():
    """ performs test calls on the functions above """
    print(abs_list_lc([-2, 5, 8, -3]))
    print(abs_list_rec([-2, 5, 8, -3]))
    print(most_vowels(['aba', 'dooooooog', 'cat', 'aeiou']))
    print(num_multiples(5, [2, 15, 10]))
    print(num_multiples(3, [12, 3, 6, 7, 9]))
    print(num_multiples(9, [15, 18]))
    print(message('Tigran', 0))
    print(message('Mike', 18))
    print(message('Jill', 20))
    print(message('Perry', 17))
    print()
    # optional but encouraged: add test calls for your functions below


test()

