
#!/usr/bin/env python3
"""
decode for machine translation:
"""
import tensorflow as tf
SelfAttention = __import__('1-self_attention').SelfAttention


class RNNDecoder(tf.keras.layers.Layer):
    """
    decode for machine translation:
    """

    def __init__(self, vocab, embedding, units, batch):
        """
        constructor function
        """
        super().__init__()
        self.vocab = vocab
        self.batch = batch
        self.units = units
        self.embedding = tf.keras.layers.Embedding(input_dim=vocab,
                                                   output_dim=embedding)
        self.gru = tf.keras.layers.GRU(units,
                                       recurrent_initializer="glorot_uniform",
                                       return_sequences=True,
                                       return_state=True)
        self.F = tf.keras.layers.Dense(vocab)

    def call(self, x, s_prev, hidden_states):
        """
        call function
        """
        attention = SelfAttention(self.units)
        context_vector, attention_weights = attention(s_prev, hidden_states)
        x = self.embedding(x)
        attention_vector = tf.concat([tf.expand_dims(context_vector, 1), x],
                                     axis=-1)
        output, state = self.gru(attention_vector)
        output = tf.reshape(output, (-1, output.shape[2]))
        x = self.F(output)
        return x, state
