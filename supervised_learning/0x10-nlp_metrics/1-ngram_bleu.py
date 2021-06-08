
#!/usr/bin/env python3

"""N-gram BLEU score"""
import numpy as np


def ngram(sentence, references, n):
    """
    ngrams
    """
    sen, sen1 = [], []
    ref, ref1, ref2 = [], [], []

    count = 0
    for token in sentence[:len(sentence)-n+1]:
        sen.append(sentence[count:count+n])
        count = count + 1
    for i in sen:
        sen1.append([' '.join(i)])

    for lst in references:
        count = 0
        for token in lst[:len(lst)-n+1]:
            ref.append(lst[count:count+n])
            count = count + 1
        for i in ref:
            ref1.append([' '.join(i)])
        ref2.append(ref1)
    return sen1, ref2


def ngram_bleu(references, sentence, n):
    """
    n-gram BLEU score
    """

    out_put_len = len(sentence)
    ref_len = np.array([len(r) for r in references])
    ref_len_idx = np.argmin(np.abs(ref_len - out_put_len))
    ref_len = len(references[ref_len_idx])

    if out_put_len > ref_len:
        bp = 1
    else:
        bp = np.exp(1 - ref_len / out_put_len)
    sentence, references = ngram(sentence, references, n)

    flat_list = list(np.concatenate(references).flat)
    sentence = list(np.concatenate(sentence).flat)
    flat_list = set(flat_list)
    wordsin = list(flat_list.intersection(sentence))
    p = len(wordsin) / len(sentence)
    return bp * p
