#!/usr/bin/env python3
"""Data augmentation"""
import tensorflow as tf


def change_brightness(image, max_delta):
    """Adjusts image's Brightness
    """
    return tf.image.random_brightness(image, max_delta)
