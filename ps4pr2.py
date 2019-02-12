#
# ps4pr1.py - Problem Set 4, Problem 2
#
# Using your conversion functions
#
from ps4pr1 import *


def mul_bin(b1, b2):
    """ takes as inputs two strings b1 and b2 that represent binary numbers. The function should multiply the
        numbers and return the result in the form of a string that represents a binary number.
    """
    num1 = bin_to_dec(b1)
    num2 = bin_to_dec(b2)
    bin_num = str(dec_to_bin(num1 * num2))
    return bin_num


def add_bytes(b1, b2):
    """takes as inputs two strings b1 and b2 that represent bytes. The function should compute the sum
        of the two bytes and return that sum in the form of a string that represents an 8-bit binary number.
    """
    num1 = bin_to_dec(b1)
    num2 = bin_to_dec(b2)
    bin_num = str(dec_to_bin(num1 + num2))
    if len(bin_num) < 8:
        num_preceding_zeros = 8 - len(bin_num)
        bin_num = ('0' * num_preceding_zeros) + bin_num
        return bin_num
    elif len(bin_num) > 8:
        return bin_num[-8:]
    else:
        return bin_num


def test():
    """test functions above"""

    print(dec_to_bin(4))
    print(dec_to_bin(7))
    print(dec_to_bin(10))
    print(dec_to_bin(111))
    print(dec_to_bin(100))
    print(bin_to_dec('1110'))
    print(bin_to_dec('1100'))
    print(bin_to_dec('00011010'))
    print(bin_to_dec('111'))
    print(add_bytes('10000011', '11000001'))
    print(add_bytes('00011100', '00011110'))
    print(add_bytes('00000011', '00000001'))
    print(mul_bin('11', '10'))
    print(mul_bin('1001', '101'))


test()

