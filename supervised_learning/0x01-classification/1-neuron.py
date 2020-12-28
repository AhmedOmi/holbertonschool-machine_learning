#!/usr/bin/env python3
"""import numpy"""
import numpy as np
"""Create a Class Neuron Network with private attribute"""


class Neuron:
    def __init__(self, nx):
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.rand(1, nx)
        self.__A = 0
        self.__b = 0

    def get_w(self):
        return self.__W

    def get_A(self):
        return self.__A

    def get_b(self):
        return self.__b
