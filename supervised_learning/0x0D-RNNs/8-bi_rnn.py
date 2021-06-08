#!/usr/bin/env python3
"""bidirectional RNN"""
import numpy as np


def bi_rnn(bi_cell, X, h_0, h_t):
    """
    forward propagation for a bidirectional RNN
    """
    t, _, i = X.shape
    Hf = []
    Hb = []
    Hsb = h_t
    h_prev = h_0

    for i in range(t):
        h_prev = bi_cell.forward(h_prev, X[i])
        Hsb = bi_cell.backward(Hsb, X[t-i-1])
        Hf.append(h_prev)
        Hb.append(Hsb)

    Hb = [i for i in reversed(Hb)]

    H = np.concatenate((np.array(Hf), np.array(Hb)), axis=-1)
    Y = bi_cell.output(H)
    return H, Y
