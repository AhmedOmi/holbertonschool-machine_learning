#!/usr/bin/env python3
"""Buimd model Neural Network with keras"""


import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """function to build neural networks with inputs"""
    reg = K.regularizers.l2(lambtha)
    inputs = K.Input(shape=(nx,))
    x = K.layers.Dense(layers[0], activation=activations[0],
                       kernel_regularizer=reg)(inputs)
    for layer, act in zip(layers[1:], activations[1:]):
        x = K.layers.Dropout(1 - keep_prob)(x)
        x = K.layers.Dense(layer, activation=act,
                           kernel_regularizer=reg)(x)
    model = K.Model(inputs=inputs, outputs=x)
    return model
