#!/usr/bin/env python3
"""
Word2Vec
"""


def gensim_to_keras(model):
    """
    genism to keras
    """

    return model.wv.get_keras_embedding(train_embeddings=False)
