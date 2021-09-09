#!/usr/bin/env python3
"""import pandas and numpy"""
import pandas as pd
import numpy as np


def from_file(filename, delimiter):
    """
    Reads data from file.
    """
    return pd.read_csv(filename, delimiter=delimiter)
