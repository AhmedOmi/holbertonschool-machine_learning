#!/usr/bin/env python3


"""using tensorflow"""
import tensorflow as tf


def create_Adam_op(loss, alpha, beta1, beta2, epsilon):
    """create function"""
    return tf.train.AdamOptimizer(alpha, beta1, beta2, epsilon).minimize(loss)
