#!/usr/bin/env python3
"""
calculates the cost of a neural network with L2 regularization
"""


import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """return the cost"""
    w = 0
    for i in range(1, L + 1):
        w = w + np.linalg.norm(weights['W' + str(i)])
    L2 = cost + (lambtha * (1 / (2 * m))) * w
    return L2
