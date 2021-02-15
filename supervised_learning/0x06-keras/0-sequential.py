#!/usr/bin/env python3

import tensorflow as tf


def build_model(nx, layers, activations, lambtha, keep_prob):
    x = tf.keras.Sequential(
        [
            tf.keras.layers.Dense(nx, layers, activations, lambtha, keep_prob)
        ]
    )
    return x
