#!/usr/bin/env python3

import tensorflow.keras as tf


def build_model(nx, layers, activations, lambtha, keep_prob):
    model.add(K.layers.Dense(units=layers[0],
                             activation=activations[0],
                             kernel_regularizer=regularizer,
                             input_shape=(nx,)))

    # creating the subsequent densley-connected layers
    for i in range(1, len(layers)):
        model.add(K.layers.Dropout(1 - keep_prob))
        model.add(K.layers.Dense(units=layers[i],
                                 activation=activations[i],
                                 kernel_regularizer=regularizer))
