#!/usr/bin/env python3
"""
update the Neural network with calculate the forward propagation
and activation function
"""

import numpy as np


class Neuron:
    """neuron class"""

    def __init__(self, nx):
        """constructor"""
        if not type(nx) is int:
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        return self.__W

    @property
    def b(self):
        return self.__b

    @property
    def A(self):
        return self.__A

    def forward_prop(self, X):
        """
        forward propagation and activation function
        update A
        """
        i = np.matmul(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-i))
        return self.__A
