#!/usr/bin/env python3
"""onverts a label vector into a one-hot matrix"""


import tensorflow.keras as K


def one_hot(Y, classes=None):
    """function one hot"""
    if classes is None:
        classes = max(Y) + 1
    return K.utils.to_categorical(Y, classes)
