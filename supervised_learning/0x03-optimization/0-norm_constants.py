#!/usr/bin/env python3
"""
calculate the normalize constant
"""

import numpy as np


def normalization_constants(X):
    """function normalization"""
    m = X.shape[0]
    mean = np.sum(X / m, axis=0)
    stddev = np.sqrt(np.sum(((X - mean) ** 2), axis=0) / m)
    return mean, stddev
