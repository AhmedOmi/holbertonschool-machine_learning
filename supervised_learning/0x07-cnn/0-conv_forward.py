#!/usr/bin/env python3
"""Convlutional forward propagation, manually"""


import numpy as np


def conv_forward(A_prev, W, b, activation, padding="same", stride=(1, 1)):
    """Convolutional forward propagation, manually"""
    if padding == "valid":
        x = A_prev
    else:
        xp = int(W.shape[1] / 2)
        yp = int(W.shape[0] / 2)
        x = np.pad(A_prev, ((0, 0), (yp - 1 + W.shape[1] % 2, yp),
                            (xp - 1 + W.shape[1] % 2, xp), (0, 0)), 'constant')
    bottom = x.shape[1] - W.shape[0] + 1
    right = x.shape[2] - W.shape[1] + 1
    output = np.ndarray((x.shape[0], int((bottom - 1) / stride[0] + 1),
                         int((right - 1) / stride[1] + 1), W.shape[3]))
    y_in = 0
    y_out = 0
    while y_in < bottom:
        x_in = 0
        x_out = 0
        while x_in < right:
            m = W[np.newaxis, ...] * x[:, y_in:y_in + W.shape[0], x_in:x_in + W.shape[1], :, np.newaxis]
            output[:, y_out, x_out] = activation(m.sum(axis=(1, 2, 3)) + b)
            x_in += stride[1]
            x_out += 1
        y_in += stride[0]
        y_out += 1
    return output
