#!/usr/bin/env python3

import tensorflow as tf


def create_placeholders(nx, classes):
    x = tf.placeholder(nx)
    y = tf.placeholder(classes)
    return x, y
