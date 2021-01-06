#!/usr/bin/env python3
"""
install and import tensorflow library with pip install tensorflow
"""


import tensorflow as tf


def create_placeholders(nx, classes):
    """
    create placeholders with nx and classes parameters and x,y returns variable
    """
    x = tf.placeholder(name='x', dtype=tf.float32, shape=(None, nx))
    y = tf.placeholder(name='y', dtype=tf.float32, shape=(None, classes))
    return x, y
