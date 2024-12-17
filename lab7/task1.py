def inp():
    user = ""
    vector = []
    while True:
        try:
            user = input("Enter the vector (input format: a b ...): ")
            user = user.split()
            for el in user:
                vector.append(int(el))
            return vector
        except:
            print("Incorrect data, try again.")


def scal(v1, v2):
    if len(v1) != len(v2):
        print("Vectors of different sizes!")
        return 'False'
    product = 0
    for i in range(len(v1)):
        product += v1[i] * v2[i]
    return product


print("First vector.")
vector1 = inp()
print("Second vector.")
vector2 = inp()
scalar_product = scal(vector1, vector2)
if scalar_product != 'False':
    print("The scalar product of vectors =", scalar_product)
