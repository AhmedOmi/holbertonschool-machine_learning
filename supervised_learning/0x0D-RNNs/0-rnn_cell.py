#!/usr/bin/env python3
""" the class RNNCell """
import numpy as np


class RNNCell:
    """  the class RNNCell """
    def __init__(self, i, h, o):
        """
        function constructor
        """
        self.Wh = np.random.normal(size=(i+h, h))
        self.Wy = np.random.normal(size=(h, o))
        self.bh = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def softmax(self, z):
        """ SOFTMAX FUNCTION"""
        t = np.exp(z - np.max(z))
        sf = t / t.sum(axis=1, keepdims=True)
        return sf

    def forward(self, h_prev, x_t):
        """
        forward function
        """
        tanh_input = np.concatenate((h_prev, x_t), axis=1)
        h_next = np.tanh(np.dot(tanh_input, self.Wh) + self.bh)
        yt_pred = self.softmax(np.dot(h_next, self.Wy) + self.by)
        return h_next, yt_pred