#!/usr/bin/env python3
"""
add class
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

        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
