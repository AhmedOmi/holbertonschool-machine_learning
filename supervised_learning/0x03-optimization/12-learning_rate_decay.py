#!/usr/bin/env python3


""" using tensorflow"""
import tensorflow as tf


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """ created function to learning"""
    return tf.train.inverse_time_decay(
        alpha, global_step, decay_step, decay_rate, staircase=True)
