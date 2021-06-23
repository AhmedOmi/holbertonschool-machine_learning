#!/usr/bin/env python3
"""
import numpy to init q tables
"""
import numpy as np


def q_init(env):
    """
    q_init objects to our current namespace
    :param env: is the FrozenLakeEnv instance
    :return: the Q-table as a numpy.ndarray of zeros
    """
    table = np.zeros((env.observation_space.n, env.action_space.n))
    return table
