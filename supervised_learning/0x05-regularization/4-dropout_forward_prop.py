#!/usr/bin/env python3
""" forward propagation function"""
import numpy as np


def dropout_forward_prop(X, weights, L, keep_prob, cac=None):
    """
    return cache
    """
    cache = {}
    cache['A0'] = X
    for i in range(0, L):
        K_A = 'A' + str(i)
        K_W = 'W' + str(i + 1)
        Al = cache[K_A]
        Ca_w = weights[K_W]
        ca_b = weights['b' + str(i + 1)]
        Z = np.matmul(Ca_w, Al) + ca_b
        if i == L - 1:
            a = np.exp(Z)
            va = a / a.sum(axis=0, keepdims=True)
            cache['A' + str(i + 1)] = va
        else:
            a = (2 / (1 + np.exp(-2 * Z))) - 1
            FN_bin = np.random.binomial(1, keep_prob, (a.shape[0],
                                                       a.shape[1]))
            a = FN_bin * a
            cache['D' + str(i + 1)] = FN_bin
            cache['A' + str(i + 1)] = a / keep_prob
    return cache
