#!/usr/bin/env python3
"""
function that calculates the determinant of a matrix
"""


def determinant(matrix):
    """
    Calculation the determinate of the matrix
    """
    tot_returns = 0

    if not isinstance(matrix, list) or len(matrix) < 1:
        raise TypeError("matrix must be a list of lists")
    if ((len(matrix) == 1 and isinstance(matrix[0], list))
            and len(matrix[0]) == 0):
        return 1
    for m in matrix:
        if not isinstance(m, list):
            raise TypeError("matrix must be a list of lists")
        if len(m) != len(matrix[0]) or len(m) != len(matrix):
            raise ValueError("matrix must be a square matrix")

    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2 and len(matrix[0]) == 2:
        matrix_two = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return matrix_two

    for fCol in list(range(len(matrix))):
        matCopy = matrix_copy(matrix)
        matCopy = matCopy[1:]
        mheight = len(matCopy)

        for idx in range(mheight):
            matCopy[idx] = matCopy[idx][0:fCol] + matCopy[idx][fCol + 1:]

        sign = (-1) ** (fCol % 2)
        subMatrix_Det = determinant(matCopy)
        tot_returns += sign * matrix[0][fCol] * subMatrix_Det
    return tot_returns


def zeroMatrix(rows, cols):
    """
    New matrix filled with zeros
    contains row and columns
    """
    matrixZ = []
    while len(matrixZ) < rows:
        matrixZ.append([])
        while len(matrixZ[-1]) < cols:
            matrixZ[-1].append(0.0)
    return matrixZ


def matrix_copy(matrixA):
    """
    matrix copy function
    """
    row = len(matrixA)
    col = len(matrixA[0])

    matrixC = zeroMatrix(row, col)

    for i in range(row):
        for j in range(col):
            matrixC[i][j] = matrixA[i][j]
    return matrixC
