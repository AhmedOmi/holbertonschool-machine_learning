#!/usr/bin/env python3

""" 0. Unigram BLEU score"""
import numpy as np


def uni_bleu(references, sentence):
    """
   calculates the unigram BLEU
    """
    out_put_len = len(sentence)
    ref_len = np.array([len(r) for r in references])
    ref_len_idx = np.argmin(np.abs(ref_len - out_put_len))
    ref_len = len(references[ref_len_idx])

    if out_put_len > ref_len:
        bp = 1
    else:
        bp = np.exp(1 - ref_len / out_put_len)
    flat_list = list(np.concatenate(references).flat)
    flat_list = set(flat_list)
    wordsin = list(flat_list.intersection(sentence))
    p = len(wordsin) / out_put_len
    return bp * p
