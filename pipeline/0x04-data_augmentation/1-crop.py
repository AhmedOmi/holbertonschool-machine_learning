#!/usr/bin/env python3
"""Data augmentation"""
import tensorflow as tf


def crop_image(image, size):
    """Crops randomly an image to the given size.
    """
    return tf.image.random_crop(image, size=size)