#!/usr/bin/env python3
"""Data augmentation"""
import tensorflow as tf


def change_hue(image, delta):
    """Adjusts the hue of an image.
    """
    return tf.image.adjust_hue(image, delta)
