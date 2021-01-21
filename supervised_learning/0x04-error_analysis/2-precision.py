#!/usr/bin/env python3
""" precision matrix """
import numpy as np


def precision(confusion):
    """ precision """
    diagonal = np.diagonal(confusion)
    confusion = np.sum(confusion, axis=0)
    result = diagonal / confusion
    return result
