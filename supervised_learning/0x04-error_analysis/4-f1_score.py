#!/usr/bin/env python3
""" f1 score """
sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """ calculate f1 score """
    p = precision(confusion)
    s = sensitivity(confusion)
    f = 2 * (p * s) / (p + s)
    return f
