import numpy as np
from math import sqrt


def euclidean_distance(matrix1, matrix2):
    if matrix1.shape == matrix2.shape:
        A = 0
        for d in range(len(matrix1)):
            for f in range(len(matrix1)):
                if matrix1.ndim and matrix2.ndim > 1:
                    A += (matrix1[d][f] - matrix2[d][f])**2
                else:
                    A += (matrix1[d] - matrix2[d]) ** 2

        A = sqrt(A)

        print(A)
    else:
        print(f"Identical shape required! {matrix1.shape}, {matrix2.shape} given")


if __name__ == '__main__':
    matrix1 = np.random.randint(low=0, high=5, size=(6, 6))
    matrix2 = np.random.randint(low=0, high=5, size=(6, 6))

    print(f"MATRIX 1:\n{matrix1}\n")
    print(f"MATRIX 2:\n{matrix2}\n")

    euclidean_distance(matrix1, matrix2)
