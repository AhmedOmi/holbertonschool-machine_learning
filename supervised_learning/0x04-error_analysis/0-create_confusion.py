#!/usr/bin/env python3
""" confusion matrix function """
import numpy as np


def create_confusion_matrix(labels, logits):
    """ create confusion matrix """
    m, classes = np.shape(labels)
    res = np.zeros((classes, classes))
    for count in range(m):
        i = np.where(labels[count, :] == 1)
        j = np.where(logits[count, :] == 1)
        res[i, j] += 1
    return res
