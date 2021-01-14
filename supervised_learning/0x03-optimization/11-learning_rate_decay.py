#!/usr/bin/env python3
"""
import numpy
"""
import numpy as np


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """ learning rate """
    alpha = alpha / (1 + (decay_rate * np.floor(global_step / decay_step)))
    return alpha
