#!/usr/bin/env python3
"""
inherits from tensorflow.keras.layers.Layer
"""
import tensorflow as tf


class RNNEncoder(tf.keras.layers.Layer):
    """
    inherits from tensorflow.keras.layers.Layer
    """

    def __init__(self, vocab, embedding, units, batch):
        """
        def init constructor
        """
        super().__init__()
        self.batch = batch
        self.units = units
        self.embedding = tf.keras.layers.Embedding(input_dim=vocab,
                                                   output_dim=embedding)
        self.gru = tf.keras.layers.GRU(units,
                                       recurrent_initializer="glorot_uniform",
                                       return_sequences=True,
                                       return_state=True)

    def initialize_hidden_state(self):
        """
        Initializes the hidden states
        """

        initializer = tf.keras.initializers.Zeros()
        hidden_states = initializer(shape=(self.batch, self.units))
        return hidden_states

    def call(self, x, initial):
        """
        the last hidden state of the encoder
        """
        embedding = self.embedding(x)
        encoder_outputs, state_h = self.gru(embedding, initial_state=initial)
        return encoder_outputs, state_h
