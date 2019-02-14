#
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# name: Tigran Melkonian

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below
def cube(x):
    """returns the cube of its input
        (i.e., x raised to the power of 3
    """
    return x**3

def compare(num1, num2):
    """returns a value that is
        based on how the numbers compare.
    """
    if(num1 > num2):
        return 1
    elif(num1 < num2):
        return -1
    else:
        return 0

def convert_from_inches(inches):
    """returns a list of three integers in which that length has
        been broken up into yards, feet, and inches
    """
    yards = inches // 36
    inches = inches - (yards * 36)
    feet = inches // 12
    inches = inches - (feet * 12)
    return [yards] + [feet] + [inches]

# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))
    print(convert_from_inches(75))
    print(cube(2))
    print(cube(-5))
    print(compare(5, 2))
    print(compare(2, 5))
    print(compare(5, 5))
    # optional but encouraged: add test calls for your functions below
