#!/usr/bin/env python3
""" Contains the inception_block function """

import tensorflow.keras as Keras


def inception_block(A_prev, filters):
    """
    Builds an inception block as described in "Going Deeper with
    """
    F1, F3R, F3, F5R, F5, FPP = filters

    initializer = Keras.initializers.he_normal(seed=None)

    my_layer = Keras.layers.Conv2D(filters=F1,
                                   kernel_size=(1, 1),
                                   padding='same',
                                   activation='relu',
                                   kernel_initializer=initializer,
                                   )(A_prev)

    my_layer1 = Keras.layers.Conv2D(filters=F3R,
                                    kernel_size=(1, 1),
                                    padding='same',
                                    activation='relu',
                                    kernel_initializer=initializer,
                                    )(A_prev)

    my_layer1 = Keras.layers.Conv2D(filters=F3,
                                    kernel_size=(3, 3),
                                    padding='same',
                                    activation='relu',
                                    kernel_initializer=initializer,
                                    )(my_layer1)

    my_layer2 = Keras.layers.Conv2D(filters=F5R,
                                    kernel_size=(1, 1),
                                    padding='same',
                                    activation='relu',
                                    kernel_initializer=initializer,
                                    )(A_prev)

    my_layer2 = Keras.layers.Conv2D(filters=F5,
                                    kernel_size=(5, 5),
                                    padding='same',
                                    activation='relu',
                                    kernel_initializer=initializer,
                                    )(my_layer2)

    my_layer3 = Keras.layers.MaxPool2D(pool_size=(3, 3),
                                       padding='same',
                                       strides=(1, 1)
                                       )(A_prev)

    my_layer3 = Keras.layers.Conv2D(filters=FPP,
                                    kernel_size=(1, 1),
                                    padding='same',
                                    activation='relu',
                                    kernel_initializer=initializer,
                                    )(my_layer3)

    output = Keras.layers.concatenate([my_layer, my_layer1,
                                      my_layer2, my_layer3])

    return output
