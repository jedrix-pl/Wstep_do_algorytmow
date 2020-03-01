import numpy as np


def gauss_elimination(MATRIX):

    lenght_matrix = len(MATRIX)

    for k in range(lenght_matrix-1):
        for i in range(k+1, lenght_matrix):
            if MATRIX[i, k] == 0:
                continue

            factor = MATRIX[k, k] / MATRIX[i, k]

            for j in range(k, lenght_matrix):
                MATRIX[i, j] = MATRIX[k, j] - MATRIX[i, j]*factor

    return MATRIX


matrix = np.array([[3, -2, 5, 0],
                  [0, 5, 8, 1],
                  [1, 0, 2, 1],
                  [0, 7, 6, 1]], float)


print(matrix, "\n\n")
print(gauss_elimination(matrix))
