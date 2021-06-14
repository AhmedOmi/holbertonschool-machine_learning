#!/usr/bin/env python3
"""
dataset for machine translation
"""
import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds


class Dataset:
    """loads and preps a dataset for machine translation"""
    def __init__(self):
        """
        constructor
        """
        self.data_train = tfds.load('ted_hrlr_translate/pt_to_en',
                                    split='train', as_supervised=True)
        self.data_valid = tfds.load('ted_hrlr_translate/pt_to_en',
                                    split='validation', as_supervised=True)

        Portuguese, English = self.tokenize_dataset(self.data_train)
        self.tokenizer_en = English
        self.tokenizer_pt = Portuguese

    def tokenize_dataset(self, data):
        """
        creates sub-word tokenizers for our dataset
        """
        Portuguese = []
        English = []
        for pt, en in data:
            Portuguese.append(pt.numpy())
            English.append(en.numpy())
        tok_pt = tfds.deprecated.text.SubwordTextEncoder.build_from_corpus(
            Portuguese, target_vocab_size=2**15)
        tok_en = tfds.deprecated.text.SubwordTextEncoder.build_from_corpus(
            English, target_vocab_size=2**15)
        return tok_pt, tok_en

    def encode(self, pt, en):
        """
        encodes a translation into tokens
        """
        encoder = self.tokenizer_en
        encoder1 = self.tokenizer_pt
        en_tokens = [encoder.vocab_size] + encoder.encode(en.numpy()) + \
            [encoder.vocab_size+1]
        pt_tokens = [encoder1.vocab_size]+encoder1.encode(pt.numpy()) + \
            [encoder1.vocab_size+1]
        return pt_tokens, en_tokens
