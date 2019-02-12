#
# ps6pr4.py (Problem Set 6, Problem 4)
#
# Estimating the value of pi
#
#

import random
import math


def throw_dart():
    """ Simulates the throwing of a random dart at a 2 x 2 square that.
        is centered on the origin. Returns True if the dart hits a circle
        inscribed in the square, and False if the dart misses the circle.
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <= 1.0:
        return True
    else:
        return False


def est_pi1(n):
    """takes a positive integer n and returns an estimate of π that is based on n randomly thrown darts."""
    hits = 0
    throws = 0
    for i in range(n):
        if throw_dart():
            hits += 1
            throws += 1
            pi = (hits * 4) / throws
            print(str(hits) + ' hit(s) out of ' + str(throws) + ' so that pi is ' + str(pi))
        else:
            throws += 1
            pi = (hits * 4) / throws
            print(str(hits) + ' hit(s) out of ' + str(throws) + ' so that pi is ' + str(pi))
    return pi


def est_pi2(error):
    """takes a positive floating-point input error and returns the number of dart throws needed to
        produce an estimate of π that is less than error away from the “actual” value of π
    """
    hits = 0
    throws = 0
    est_pi = 0
    difference = abs(math.pi - est_pi)
    while difference > error:
        if throw_dart():
            hits += 1
            throws += 1
            est_pi = (hits * 4) / throws
            difference = abs(math.pi - est_pi)
            print(str(hits) + ' hit(s) out of ' + str(throws) + ' so that pi is ' + str(est_pi))
        else:
            throws += 1
            est_pi = (hits * 4) / throws
            difference = abs(math.pi - est_pi)
            print(str(hits) + ' hit(s) out of ' + str(throws) + ' so that pi is ' + str(est_pi))
    return est_pi


### IMPORTANT NOTES:
###  - One of your functions must use a for loop, and the other function
###    must use a while loop. You should decide which type of loop is
###    more appropriate for each function.
###
###  - Each function must call throw_dart() from inside its loop.
###    For full credit, each function must have *EXACTLY ONE* line of
###    code that calls throw_dart(). If a given function has fewer
###    or more than one line of code that calls throw_dart(), you
###    will lose points.
###
###    In addition, your functions must *NOT* make their own calls
###    to random.uniform(), and you will lose points if they do so.


def test():
    """test functions above"""
    print(throw_dart())
    print(est_pi2(0.1))
    print()
    print()


test()
