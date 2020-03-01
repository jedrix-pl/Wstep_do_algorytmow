import numpy as np
from math import sqrt

matrix1 = np.random.randint(low=0, high=5, size=(4, 4))
matrix2 = np.random.randint(low=0, high=5, size=(4, 4))

print(f"MATRIX 1:\n{matrix1}\n")
print(f"MATRIX 2:\n{matrix2}\n")


def euclidean_distance(matrix1, matrix2):
    if len(matrix1) == len(matrix2):
        A = 0
        for d in range(len(matrix1)):
            try:
                A += (matrix1[d][d] - matrix2[d][d])**2
            except IndexError:
                A += (matrix1[d] - matrix2[d]) ** 2

        A = sqrt(A)

        return A

print(euclidean_distance(matrix1, matrix2))