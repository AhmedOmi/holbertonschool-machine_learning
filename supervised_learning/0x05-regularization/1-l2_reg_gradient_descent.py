#!/usr/bin/env python3
"""
Updates the weights of a neural network
"""

import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """
    l2_reg_gradient_descent
    """
    s = Y.shape[1]
    dz = cache['A' + str(L)]
    ddz = dz - Y
    for j in range(L, 0, -1):
        kb = 'b' + str(j)
        Kw = 'W' + str(j)
        k_l_w = weights[Kw]
        kddz = cache['A' + str(j - 1)]
        wcp = weights[Kw]
        derb1 = (1 / s) * (np.sum(ddz, axis=1, keepdims=True))
        derltw = (1 / s) * np.matmul(ddz, kddz.T) + ((lambtha / s) * k_l_w)
        ddz = np.matmul(wcp.T, ddz) * (1 - kddz * kddz)
        weights[Kw] = weights[Kw] - alpha * derltw
        weights[kb] = weights[kb] - alpha * derb1
