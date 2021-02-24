#!/usr/bin/env python3
""" Pooling Backpropagation """
import numpy as np


def pool_backward(dA, A_prev, kernel_shape,
                  stride=(1, 1), mode='max'):
    """ pooling layer of function backward """
    m, h_new, w_new, c_new = dA.shape
    m, h_prev, w_prev, c = A_prev.shape
    kh, kw = kernel_shape
    sh, sw = stride

    dA_prev = np.zeros(A_prev.shape)
    for z in range(m):
        for i in range(h_new):
            for j in range(w_new):
                for k in range(c_new):
                    h_init = i * sh
                    h_end = i * sh + kh
                    w_init = j * sw
                    w_end = j * sw + kw
                    if mode == 'max':
                        value = np.max(A_prev[z,
                                              h_init:h_end,
                                              w_init:w_end,
                                              k])
                        mask = np.where(A_prev[z,
                                               h_init:h_end,
                                               w_init:w_end,
                                               k] == value, 1, 0)
                        mask = mask * dA[z, i, j, k]
                    elif mode == 'avg':
                        mask = np.ones(kernel_shape) * (dA[z, i, j, k] /
                                                        (kh * kw))
                    dA_prev[z, h_init:h_end,
                            w_init:w_end, k] += mask
    return dA_prev