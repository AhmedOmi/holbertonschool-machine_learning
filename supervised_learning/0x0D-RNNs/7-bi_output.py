#!/usr/bin/env python3
""" bidirectional Cell """

import numpy as np


class BidirectionalCell():
    """class bidirectionalcell"""
    def __init__(self, i, h, o):
        """
        function constructor
        """
        self.Whf = np.random.normal(size=(i + h, h))
        self.Whb = np.random.normal(size=(i + h, h))
        self.Wy = np.random.normal(size=((2 * h), o))
        self.bhf = np.zeros((1, h))
        self.bhb = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """
        forward function
        """
        input_tanh = np.concatenate((h_prev, x_t), axis=1)
        h_next = np.tanh(np.dot(input_tanh, self.Whf) + self.bhf)
        return h_next

    def backward(self, h_next, x_t):
        """
        backward function
        """
        tanh_input = np.concatenate((h_next, x_t), axis=1)
        h_pev = np.tanh(np.dot(tanh_input, self.Whb) + self.bhb)
        return h_pev

    def softmax(self, x):
        """ softmax function """
        return np.exp(x)/np.sum(np.exp(x), axis=1, keepdims=True)

    def output(self, H):
        """
        calculates all outputs for the RNN
        """
        t, m, h = H.shape
        Y = []
        for t_step in range(t):
            y = np.dot(H[t_step], self.Wy) + self.by

            y = self.softmax(y)
            Y.append(y)

        return np.array(Y)
