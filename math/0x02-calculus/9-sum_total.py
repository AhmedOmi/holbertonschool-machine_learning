#!/usr/bin/env python3

""" function calculate sum of squard"""


def summation_i_squared(n):
    """
    if n is not int return none
    or n == 0 return none
    """
    if type(n) == int and n > 0:
        return int(n * (n + 1) * (2 * n + 1) / 6)
    else:
        return None
