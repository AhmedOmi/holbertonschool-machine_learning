#!/usr/bin/env python3
"""function to create a new layer"""
import tensorflow as tf


def dropout_create_layer(prev, n, activation, keep_prob):
    """
    creation de layer
    """
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    regulariz = tf.layers.Dropout(keep_prob)
    layer = tf.layers.Dense(units=n,
                            activation=activation,
                            kernel_initializer=init,
                            kernel_regularizer=regulariz,
                            bias_regularizer=None,
                            name='layer')
    return layer(prev)
