#!/usr/bin/env python3
"""import numpy"""
import numpy as np


class Neuron:
    """Create a Neuron class"""
    def __init__(self, nx):
        """create a constructor"""
        if not type(nx) is int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.W = np.random.rand(1, nx)
        self.b = 0
        self.A = 0
