#!/usr/bin/env python3
"""import numpy"""
import numpy as np
"""Create a Class Neuron Networl"""


class Neuron:
    def __init__(self, nx):
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.W = np.random.rand(1, nx)
        self.A = 0
        self.b = 0
