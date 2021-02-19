#!/usr/bin/env python3
"""import tensorflow"""
import tensorflow as tf


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    Builds a neural network with the Keras library
    """
    inputs = tf.keras.Input(shape=(nx,))
    regularizer = tf.keras.regularizers.l2(lambtha)

    # Input layer creation
    outputs = tf.keras.layers.Dense(units=layers[0],
                                    kernel_regularizer=regularizer,
                                    activation=activations[0],
                                    input_shape=(nx,))(inputs)

    # Subsequent layer creation
    for i in range(1, len(layers)):
        outputs = tf.keras.layers.Dropout(1 - keep_prob)(outputs)
        outputs = tf.keras.layers.Dense(units=layers[i],
                                        activation=activations[i],
                                        kernel_regularizer=regularizer)(outputs)

    model = tf.keras.Model(inputs=inputs, outputs=outputs)

    return model

    
