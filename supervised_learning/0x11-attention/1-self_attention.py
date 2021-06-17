#!/usr/bin/env python3
"""
calculate the attention for machine translation
"""
import tensorflow as tf


class SelfAttention(tf.keras.layers.Layer):
    """calculate the attention for machine translation"""
    def __init__(self, units):
        """
        constructor
        """
        super().__init__()
        self.W = tf.keras.layers.Dense(units)
        self.U = tf.keras.layers.Dense(units)
        self.V = tf.keras.layers.Dense(1)

    def call(self, s_prev, hidden_states):
        """
        function call
        """
        query = s_prev
        values = hidden_states

        newaxis_query = tf.expand_dims(query, 1)
        a = self.W(newaxis_query)

        b = self.U(values)
        score = self.V(tf.nn.tanh(a + b))
        score = tf.nn.softmax(score, axis=1)
        weighted_values = score * values
        context = tf.reduce_sum(weighted_values, axis=1)
        return context, score
