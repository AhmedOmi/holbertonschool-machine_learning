#!/usr/bin/env python3
""" Moving Average """


def moving_average(data, beta):
    """ Moving Average """
    V = [0]
    W = []
    for i in range(len(data)):
        V.append((1 - beta) * data[i] + beta * V[i])
        W.append(V[i+1] / (1 - beta ** (i+1)))
    return W
