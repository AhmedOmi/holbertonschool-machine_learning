#!/usr/bin/env python3
"""
install and import tensorflow library
pip install tensorflow
"""


import tensorflow as tf


def create_placeholders(nx, classes):
    x = tf.placeholder(name='x', dtype=tf.float32, shape=(None, nx))
    y = tf.placeholder(name='y', dtype=tf.float32, shape=(None, classes))
    return x, y
