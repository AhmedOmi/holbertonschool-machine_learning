#!/usr/bin/env python3

"""
class neural network
"""

import numpy as np


class NeuralNetwork:
    """ Class NeuralNetwork"""

    def __init__(self, nx, nodes):
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.W1 = np.random.randn(nodes, nx)
        self.W2 = np.random.randn(1, nodes)
        self.b1 = np.zeros((nodes, 1))
        self.b2 = 0
        self.A1 = 0
        self.A2 = 0
