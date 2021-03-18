#!/usr/bin/env python3
"""
function that calculates the definiteness of a matrix
"""
import numpy as np


def definiteness(matrix):
    """
    calculates definiteness of a matrix
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if not np.all(np.transpose(matrix) == matrix):
        return None
    if len(matrix.shape) != 2:
        return None
    if matrix.shape[0] != matrix.shape[1]:
        return None
    definite = (np.linalg.eigvals(matrix))

    if all(definite == 0):
        return None
    if all(definite > 0):
        return "Positive definite"
    if all(definite < 0):
        return "Negative definite"
    if any(definite > 0) and any(definite == 0):
        return "Positive semi-definite"
    if any(definite < 0) and any(definite == 0):
        return "Negative semi-definite"
    elif not (any(definite < 0)
              and any(definite == 0) and any(definite > 0)):
        return "Indefinite"
    else:
        return "None"


def inverse(matrix):
    """
    calculate the inverse of a function
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    for m in matrix:
        if not isinstance(m, list):
            raise TypeError("matrix must be a list of lists")
        if len(m) != len(matrix):
            raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return [[1 / (matrix[0][0])]]

    invMatrix = adjugate(matrix)
    determinantNum = determinant(matrix)
    if determinantNum == 0:
        return None
    for i in range(len(invMatrix)):
        for j in range(len(invMatrix)):
            invMatrix[i][j] = invMatrix[i][j] / (determinantNum)
    return invMatrix


def adjugate(matrix):
    """
    calculates the adjugate of given matrix
    """
    return transpose_matrix(cofactor(matrix))


def transpose_matrix(matrix):
    """
    transpose given matrix
    """
    return [[row[m] for row in matrix] for m in range(len(matrix[0]))]


def cofactor(matrix):
    """
    calculate the cofactor of a matrix
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    for m in matrix:
        if not isinstance(m, list):
            raise TypeError("matrix must be a list of lists")
        if len(m) != len(matrix):
            raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return [[1]]

    cfMatrix = []
    for row in range(len(matrix)):
        newMatrix = []
        for col in range(len(matrix[row])):
            sub_minr = [[matrix[i][j] for j in range(len(matrix))
                         if (j != col and i != row)]
                        for i in range(len(matrix))]
            sub_minr = [i for i in sub_minr if len(i) == len(matrix) - 1]

            newMatrix.append((-1) ** (row + col) * determinant(sub_minr))

        cfMatrix.append(newMatrix)
    return cfMatrix


def minor(matrix):
    """
    calclulate the minor of a matrix
    """
    # check if is list and check if is square matrix
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    for m in matrix:
        if not isinstance(m, list):
            raise TypeError("matrix must be a list of lists")
        if len(m) != len(matrix):
            raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return [[1]]

    minorMatrix = []
    for row in range(len(matrix)):
        newMatrix = []
        for col in range(len(matrix[row])):
            sub_minr = [[matrix[i][j] for j in range(len(matrix))
                         if (j != col and i != row)]
                        for i in range(len(matrix))]
            sub_minr = [i for i in sub_minr if len(i) == len(matrix) - 1]

            newMatrix.append(determinant(sub_minr))

        minorMatrix.append(newMatrix)
    return minorMatrix


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


def adjugate(matrix):
    """
    calculates the adjugate of given matrix
    """
    return transpose_matrix(cofactor(matrix))


def transpose_matrix(matrix):
    """
    transpose given matrix
    """
    return [[row[m] for row in matrix] for m in range(len(matrix[0]))]


def cofactor(matrix):
    """
    calculate the cofactor of a matrix
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    for m in matrix:
        if not isinstance(m, list):
            raise TypeError("matrix must be a list of lists")
        if len(m) != len(matrix):
            raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return [[1]]

    cfMatrix = []
    for row in range(len(matrix)):
        newMatrix = []
        for col in range(len(matrix[row])):
            sub_minr = [[matrix[i][j] for j in range(len(matrix))
                         if (j != col and i != row)]
                        for i in range(len(matrix))]
            sub_minr = [i for i in sub_minr if len(i) == len(matrix) - 1]

            newMatrix.append((-1) ** (row + col) * determinant(sub_minr))

        cfMatrix.append(newMatrix)
    return cfMatrix


def minor(matrix):
    """
    calclulate the minor of a matrix
    """
    # check if is list and check if is square matrix
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    for m in matrix:
        if not isinstance(m, list):
            raise TypeError("matrix must be a list of lists")
        if len(m) != len(matrix):
            raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return [[1]]

    minorMatrix = []
    for row in range(len(matrix)):
        newMatrix = []
        for col in range(len(matrix[row])):
            sub_minr = [[matrix[i][j] for j in range(len(matrix))
                         if (j != col and i != row)]
                        for i in range(len(matrix))]
            sub_minr = [i for i in sub_minr if len(i) == len(matrix) - 1]

            newMatrix.append(determinant(sub_minr))

        minorMatrix.append(newMatrix)
    return minorMatrix


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
