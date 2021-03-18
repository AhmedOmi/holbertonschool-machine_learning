#!/usr/bin/env python3
import numpy as np


def determinant(matrix):
    if matrix is not list:
        raise TypeError('matrix must be a list of lists')
    deter = np.linalg.det(matrix)
    return deter
