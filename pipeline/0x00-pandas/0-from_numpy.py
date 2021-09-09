#!/usr/bin/env python3
"""Pandas import as pd"""
import pandas as pd
import string


def from_numpy(array):
    """
    from a np.ndarray creates pd.DataFrame 
    """
    _, a = array.shape
    labels = string.ascii_uppercase
    return pd.DataFrame(array, columns=[labels[i] for i in range(a)])
