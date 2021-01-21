#!/usr/bin/env python3
""" create the gradient descent function"""
import numpy as np


def dropout_gradient_descent(Y, weights, cache, alpha, keep_prob, L):
    """
    gradient descent
    """
    m = Y.shape[1]
    Z = cache["A" + str(L)] - Y
    for count in range(L, 0, -1):
        B = "b" + str(count)

        W = "W" + str(count)
        A = "A" + str(count - 1)

        CA = cache[A]
        dw = ((1 / m) * np.matmul(Z, CA.T))
        db = (1 / m) * np.sum(Z, axis=1, keepdims=True)

        zb = 1 - np.power(CA, 2)
        if count > 1:
            Z = Z.T * zb
            Z = Z / keep_prob
        else:
            Z = cache["A" + str(L)] - Y
        weights[W] = weights[W] - dw * alpha
        weights[B] = weights[B] - db * alpha
