#!/usr/bin/env python3
""" create layers """
import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    """
    return layer
    """
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    regularize = tf.contrib.layers.l2_regularizer(lambtha)
    layer = tf.layers.Dense(units=n, activation=activation,
                            use_bias=True,
                            kernel_initializer=init,
                            kernel_regularizer=regularize,
                            bias_regularizer=None)
    return layer(prev)
