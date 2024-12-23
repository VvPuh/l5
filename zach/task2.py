import os


def read_matrix(matrix):
    matrix = []
    matrix_file = os.path.join('data', "matrix.txt")
    if not os.path.isfile(matrix_file):
        print("Файл matrix.txt не существует")
        return []
    with open(matrix_file, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            matrix.append(line.split())
    if not matrix:
        print("Пустая матрица.")
        return []
    for line in matrix:
        if len(line) != len(matrix):
            print("В файле не матрица.")
            return []
        for element in line:
            if not element.isdigit():
                print("В файле не матрица.")
                return []
    return matrix


def turn_matrix(matrix):
    matrix_size = len(matrix)
    t_matrix = [['' for _ in range(matrix_size)] for _ in range(matrix_size)]
    for i in range(matrix_size):
        for j in range(matrix_size):
            t_matrix[i][j] = matrix[matrix_size - 1 - j][i]
    return t_matrix


def write_matrix(matrix):
    matrix_file = os.path.join('data', "res.txt")
    with open(matrix_file, 'w+', encoding="utf-8") as f:
        for line in matrix:
            f.write(' '.join(el for el in line) + '\n')


user_matrix = []
user_matrix = read_matrix(user_matrix)
if not len(user_matrix):
    exit()
user_matrix = turn_matrix(user_matrix)
write_matrix(user_matrix)
