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
        self.__W1 = np.random.randn(nodes, nx)
        self.__W2 = np.random.randn(1, nodes)
        self.__b1 = np.zeros((nodes, 1))
        self.__b2 = 0
        self.__A1 = 0
        self.__A2 = 0

    @property
    def W1(self):
        return self.__W1

    @property
    def W2(self):
        return self.__W2

    @property
    def b1(self):
        return self.__b1

    @property
    def b2(self):
        return self.__b2

    @property
    def A1(self):
        return self.__A1

    @property
    def A2(self):
        return self.__A2

    def forward_prop(self, X):
        """ Calculates the forward propagation"""
        i = np.matmul(self.__W1, X) + self.__b1
        self.__A1 = 1 / (1 + np.exp(-i))
        j = np.matmul(self.__W2, self.__A1) + self.__b2
        self.__A2 = 1 / (1 + np.exp(-j))
        return self.__A1, self.__A2

    def cost(self, Y, A):
        """ Calculate cost function"""
        cost = - (np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)))
        cost /= Y.shape[1]
        return cost

    def evaluate(self, X, Y):
        """Function to evaluate neural network"""
        b, f = self.forward_prop(X)
        cost = self.cost(Y, f)
        return np.where(f >= 0.5, 1, 0), cost
