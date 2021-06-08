#!/usr/bin/env python3
"""
Train Word2Vec
creates and trains a gensim word2vec model
"""
from gensim.models import Word2Vec


def word2vec_model(sentences, size=100, min_count=5, window=5,
                   negative=5, cbow=True, iterations=5, seed=0, workers=1):
    """
    word2vec_model
    """
    w2v_model = Word2Vec(size=size, min_count=min_count, window=window,
                         negative=negative, sg=cbow,
                         seed=seed, workers=workers)
    w2v_model.build_vocab(sentences)
    w2v_model.train(sentences, total_examples=w2v_model.corpus_count,
                    epochs=iterations)
    return w2v_model
