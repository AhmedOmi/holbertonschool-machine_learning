#!/usr/bin/env python3
"""how to create a function to transpose a matrix"""


def matrix_transpose(matrix):
    mat = [[]]
    for i in matrix:
        for j in matrix:
            mat[i][j].append(matrix[i][j])