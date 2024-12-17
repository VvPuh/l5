def inp_mnk():
    x = ""
    while True:
        try:
            x = int(input("Enter size of matrix(>0): "))
            return x
        except:
            print("Incorrect data, try again.")


def inp(lines, columns):
    user = ""
    matr = []
    while True:
        try:
            for i in range(lines):
                matr.append([])
                user = input()
                user = user.split()
                for j in range(columns):
                    matr[i].append(int(user[j]))
            break
        except:
            print("Incorrect data, try again.")
    return matr


def product(matrix1, matrix2):
    product_matr = []
    for i in range(len(matrix1)):
        product_matr.append([])
        for j in range(len(matrix2[0])):
            product_matr[i].append(0)
            for k_index in range(len(matrix2)):
                product_matr[i][j] += matrix1[i][k_index] * matrix2[k_index][j]
    return product_matr


def print_matr(matr):
    for i in range(len(matr)):
        for j in range(len(matr[0])):
            print(matr[i][j], end=' ')
        print('')


print("MxK and KxN size matrices.")
print("M size of matrix.")
m = inp_mnk()
print("K size of matrix.")
k = inp_mnk()
print("N size of matrix.")
n = inp_mnk()
print("Enter first matrix:")
matr1 = inp(m, k)
print("Enter second matrix:")
matr2 = inp(k, n)
print("Product matrix:")
print_matr(product(matr1, matr2))
