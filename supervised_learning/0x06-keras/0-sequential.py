#!/usr/bin/env python3
"""function to build a new model of deeplearning"""


import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """ build model using nx, layers, activations function, lambtha
     keep_prob """
    model = K.Sequential()
    regularizer = K.regularizers.l2(lambtha)

    model.add(K.layers.Dense(units=layers[0],
                             activation=activations[0],
                             kernel_regularizer=regularizer,
                             input_shape=(nx,)))

    for i in range(1, len(layers)):
        model.add(K.layers.Dropout(1 - keep_prob))
        model.add(K.layers.Dense(units=layers[i],
                                 activation=activations[i],
                                 kernel_regularizer=regularizer))
    return model
