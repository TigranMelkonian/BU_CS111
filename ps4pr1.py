#
# ps4pr1.py - Problem Set 4, Problem 1
#
# From binary to decimal and back!
#


def dec_to_bin(n):
    """that takes a non-negative integer n and uses recursion to convert it from decimal to binary –
        constructing and returning a string version of the binary representation of that number.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return n % 2 + 10 * dec_to_bin(n // 2)


def bin_to_dec(n):
    """that takes a string b that represents a binary number and uses recursion to
        convert the number from binary to decimal, returning the resulting integer.
    """
    if n == "0":
        return 0
    if n == "1":
        return 1
    elif n[-1] == '1':
        return bin_to_dec(n[:-1]) * 2 + 1
    else:
        return bin_to_dec(n[:-1]) * 2


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


test()
