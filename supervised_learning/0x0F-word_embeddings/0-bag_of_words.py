#!/usr/bin/env python3
"""
Bag Of Words
"""
from sklearn.feature_extraction.text import CountVectorizer


def bag_of_words(sentences, vocab=None):
    """
    bag of words function
    """
    vectorizer2 = CountVectorizer(analyzer='word', vocabulary=vocab)
    X2 = vectorizer2.fit_transform(sentences)
    embeddings = X2.toarray()
    features = vectorizer2.get_feature_names()
    return embeddings, features
