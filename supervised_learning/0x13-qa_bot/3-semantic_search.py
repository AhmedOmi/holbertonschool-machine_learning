#!/usr/bin/env python3
"""
performs semantic search
"""
import tensorflow_hub as hub
import os
import numpy as np


def semantic_search(corpus_path, sentence):
    """
    the reference text of the document
    """
    dirs = os.listdir(corpus_path)

    documents_list = []
    documents_list.append(sentence)
    for fle in dirs:
        if not fle.endswith('.md'):
            continue
        with open(corpus_path+'/'+fle,   encoding="utf_8") as f:
            text = f.read()
            documents_list.append(text)
    embed = hub.load(
        "https://tfhub.dev/google/universal-sentence-encoder-large/5")

    embeddings = embed(documents_list)
    similarity = np.inner(embeddings, embeddings)

    indx = np.argmax(similarity[0, 1:])
    return(documents_list[indx+1])
