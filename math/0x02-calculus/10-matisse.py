#!/usr/bin/env python3

"""
function to calculate the derivative of polynome
"""


def poly_derivative(poly):
    """
    derivabilite of polynome
    """
    """ polynome derivative function"""
    if type(poly) is not list:
        return None
    if len(poly) == 0:
        return None
    if poly == 0 or len(poly) == 1:
        return [0]
    p = poly[:]
    for i in range(len(p)):
        p[i] *= i
    p.pop(0)
    return p
