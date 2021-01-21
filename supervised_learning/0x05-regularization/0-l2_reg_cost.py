#!/usr/bin/env python3
"""
calculates the cost of a neural network with L2 regularization
"""


import numpy.linalg as nl


def l2_reg_cost(cost, lambtha, weights, L, m):
    """return the cost"""
    w = 0
    for i in range(1, L+1):
        w = w + nl.norm(weights['W' + str(i)])
    return cost + ((lambtha / (2 * m)) * w)


