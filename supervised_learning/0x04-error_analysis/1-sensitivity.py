#!/usr/bin/env python3
""" sensetivity function """
import numpy as np


def sensitivity(confusion):
    """ create sensitivity """
    diagonal = np.diagonal(confusion)
    confusion = np.sum(confusion, axis=1)
    result = diagonal / confusion
    return result
