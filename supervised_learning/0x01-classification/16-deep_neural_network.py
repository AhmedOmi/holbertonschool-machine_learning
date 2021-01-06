#!/usr/bin/env python3

"""
CLASS deep neural network
"""

import numpy as np


class DeepNeuralNetwork:
    """class deeplearning"""
    def __init__(self, nx, layers):
        """costructor"""
        if type(nx) is not int:
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        if type(layers) is not list or not layers:
            raise TypeError('layers must be a list of positive integers')
        self.L = len(layers)
        self.cache = {}
        self.weights = {}
        for i in range(len(layers)):
            if layers[i] <= 0:
                raise TypeError("layers must be a list of positive integers")
            if i == 0:
                v = np.random.randn(layers[i], nx) * np.sqrt(2 / nx)
                self.weights['W' + str(i + 1)
                             ] = v
            else:
                self.weights['W' + str(i + 1)] = \
                    np.random.randn(layers[i], layers[i - 1]) * \
                    np.sqrt(2 / layers[i - 1])
            self.weights['b' + str(i + 1)] = np.zeros((layers[i], 1))
