from ex1 import gen_grades


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


if __name__ == '__main__':
    matrix = gen_grades(min=0, max=9)

    print(matrix, "\n\n")
    print(gauss_elimination(matrix))
