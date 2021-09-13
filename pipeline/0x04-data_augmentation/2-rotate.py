#!/usr/bin/env python3
"""Data augmentation"""
import tensorflow as tf


def rotate_image(image):
    """Rotates an image 90 degres anticlockwise
    """
    return tf.image.rot90(image, k=1)
