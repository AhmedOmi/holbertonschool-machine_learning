#!/usr/bin/env python3


"""TENSORFLOW"""
import tensorflow as tf


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """RMSProp operation"""
    return tf.train.\
        RMSPropOptimizer(alpha, beta2, epsilon=epsilon).minimize(loss)
